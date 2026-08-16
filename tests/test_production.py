from chotaku.production import (
    IdentityMemory,
    LayoutContract,
    LayoutSlot,
    ReaderState,
    RenderCheckpoint,
    RightsRecord,
    identity_drift,
    layout_to_svg,
    validate_layout,
    validate_rights,
)


def test_layout_contract_detects_overflow_and_unknown_panel():
    contract = LayoutContract(
        id="page-1",
        width=100,
        height=100,
        slots=[LayoutSlot("hero", "hero", 80, 80, 40, 40)],
        panel_order=["hero", "missing"],
    )
    codes = {item.code for item in validate_layout(contract)}
    assert "layout-overflow" in codes
    assert "unknown-panel" in codes


def test_rights_gate_blocks_unassessed_subject():
    findings = validate_rights(
        [RightsRecord("asset-rights", "hero", status="unassessed")],
        ["hero"],
    )
    assert findings[0].code == "rights-not-cleared"


def test_identity_drift_uses_approved_anchors():
    identity = IdentityMemory(
        id="hero-v1",
        character_id="hero",
        status="approved",
        visual_anchors=["pink mohawk", "black jacket"],
    )
    findings = identity_drift(identity, ["black jacket"])
    assert findings[0].code == "identity-drift"
    assert "pink mohawk" in findings[0].message


def test_checkpoint_resumes_only_remaining_units():
    checkpoint = RenderCheckpoint(
        id="run-1",
        artifact_id="page-1",
        stage="panels",
        total_units=["p1", "p2"],
    )
    checkpoint.mark_complete("p1", "asset-1")
    assert checkpoint.resumable
    assert checkpoint.remaining_units == ["p2"]
    checkpoint.mark_complete("p2", "asset-2")
    assert checkpoint.status == "complete"
    assert not checkpoint.resumable


def test_layout_exports_declarative_svg():
    contract = LayoutContract(
        id="page-1",
        width=400,
        height=600,
        slots=[LayoutSlot("hero", "hero", 10, 10, 380, 580, label="Hero panel")],
    )
    svg = layout_to_svg(contract)
    assert "<svg" in svg
    assert "Hero panel" in svg


def test_cells_styles_and_text_regions_have_own_contracts():
    from chotaku.production import (
        CellDefinition,
        LayoutStyle,
        TextRegionDefinition,
    )

    contract = LayoutContract(
        "styled-page",
        width=400,
        height=600,
        slots=[LayoutSlot("p1", "hero", 0, 0, 400, 600)],
        styles=[LayoutStyle("noir", family="manga", border="#00ccff")],
        cells=[CellDefinition("cell-1", "p1", role="reveal", style_id="noir", reading_order=1)],
        text_regions=[TextRegionDefinition("caption-1", "cell-1", text="The signal returns.")],
        default_style_id="noir",
    )
    assert validate_layout(contract) == []
    svg = layout_to_svg(contract)
    assert "reveal" in svg
    assert "The signal returns." in svg


def test_visual_language_fixture_pack_is_valid():
    import json
    from pathlib import Path
    from chotaku.production import layout_contract_from_dict

    root = Path(__file__).parents[1] / "fixtures" / "layouts"
    names = {"ltr-grid.json", "rtl-grid.json", "ttb-scroll.json", "dossier-grid.json", "storyboard-shot.json"}
    for name in names:
        contract = layout_contract_from_dict(json.loads((root / name).read_text()))
        assert validate_layout(contract) == []
        assert contract.prompt_manifests[0].template_id.startswith("layout/")
        assert contract.typography_styles
        assert contract.gutter_rhythm


def test_visual_language_validators_report_deterministic_findings():
    from chotaku.production import (
        BalloonStyle,
        CellDefinition,
        TextRegionDefinition,
        TypographyStyle,
        validate_balloon_tails,
        validate_text_overflow,
    )

    contract = LayoutContract(
        "invalid-language",
        slots=[LayoutSlot("p1", "hero", 0, 0, 100, 100)],
        cells=[
            CellDefinition("c1", "p1", role="hero", reading_order=1),
            CellDefinition("c2", "p1", role="detail", reading_order=1),
        ],
        text_regions=[
            TextRegionDefinition("dialogue", "c1", kind="dialogue", text="hello"),
            TextRegionDefinition("caption", "c2", text="this text is intentionally too long", typography_id="tight"),
        ],
        typography_styles=[TypographyStyle("tight", max_characters=5)],
        balloon_styles=[BalloonStyle("speech-balloon")],
    )
    codes = {finding.code for finding in validate_layout(contract)}
    assert "duplicate-reading-order" in codes
    assert "missing-balloon-style" in codes
    assert "text-overflow" in codes
    assert "missing-balloon-tail" not in codes
    assert {finding.code for finding in validate_balloon_tails(contract)} == {"missing-balloon-style"}
    assert {finding.code for finding in validate_text_overflow(contract)} == {"text-overflow"}



def test_visual_contract_references_and_geometry_are_validated():
    from chotaku.production import (
        CellDefinition,
        LayoutStyle,
        PromptManifest,
        SfxDefinition,
        TextRegionDefinition,
        TypographyStyle,
        validate_layout,
    )

    contract = LayoutContract(
        "reference-check",
        width=200,
        height=200,
        slots=[
            LayoutSlot("hero", "hero", 0, 0, 140, 160),
            LayoutSlot("detail", "detail", 100, 100, 80, 80),
        ],
        styles=[LayoutStyle("style", typography_id="type")],
        cells=[
            CellDefinition("hero-cell", "hero", role="hero", reading_order=1, focal_weight=0.9),
            CellDefinition("detail-cell", "detail", role="detail", reading_order=2),
        ],
        text_regions=[
            TextRegionDefinition("caption", "hero-cell", x=0.8, y=0.8, width=0.4, height=0.3, typography_id="type"),
        ],
        typography_styles=[TypographyStyle("type")],
        sfx_definitions=[SfxDefinition("sfx", "missing-cell", "KRAK", typography_id="missing-type")],
        prompt_manifests=[
            PromptManifest(
                "manifest",
                "wrong-artifact",
                "layout/reference-check",
                typography_style_ids=["missing-type"],
            )
        ],
    )
    codes = {finding.code for finding in validate_layout(contract)}
    assert "slot-overlap" in codes
    assert "text-region-out-of-bounds" in codes
    assert "unknown-cell" in codes
    assert "unknown-typography-style" in codes
    assert "manifest-artifact-mismatch" in codes


def test_focal_weight_is_range_checked_and_missing_weight_is_visible():
    from chotaku.production import CellDefinition, validate_focal_cell_dominance

    contract = LayoutContract(
        "focal-check",
        slots=[LayoutSlot("hero", "hero", 0, 0, 100, 100)],
        cells=[CellDefinition("hero-cell", "hero", role="hero", reading_order=1, focal_weight=1.5)],
    )
    findings = validate_focal_cell_dominance(contract)
    assert {finding.code for finding in findings} == {"invalid-focal-weight"}



def test_curse_of_knowing_visual_dry_run_exports_clean_svg():
    import json
    from pathlib import Path
    from chotaku.production import layout_contract_from_dict, layout_to_svg

    path = Path(__file__).parents[1] / "fixtures" / "layouts" / "curse-of-knowing-dry-run.json"
    contract = layout_contract_from_dict(json.loads(path.read_text()))
    findings = validate_layout(contract)
    assert findings == []
    svg = layout_to_svg(contract, title="The Curse of Knowing")
    assert "<svg" in svg
    assert "Meaning over certainty" in svg
    assert "I CHOOSE THE UNKNOWN." in svg

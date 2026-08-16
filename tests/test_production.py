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

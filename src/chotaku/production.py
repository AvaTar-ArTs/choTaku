"""Production contracts for identity, readership, rights, layout, and rendering.

These objects sit between choTaku's semantic storyworld and downstream
providers. They are deterministic and dependency-free by design.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from html import escape
from typing import Any


@dataclass
class IdentityMemory:
    id: str
    character_id: str
    version: str = "1"
    status: str = "provisional"
    visual_anchors: list[str] = field(default_factory=list)
    negative_anchors: list[str] = field(default_factory=list)
    reference_asset_ids: list[str] = field(default_factory=list)
    continuity_notes: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)
    supersedes: str | None = None


@dataclass
class ReaderState:
    id: str
    scene_id: str
    known: list[str] = field(default_factory=list)
    new: list[str] = field(default_factory=list)
    open_questions: list[str] = field(default_factory=list)


@dataclass
class RightsRecord:
    id: str
    subject_id: str
    status: str = "unassessed"
    basis: str = ""
    source_ids: list[str] = field(default_factory=list)
    restrictions: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class TypographyStyle:
    id: str
    semantic_family: str = "hand_lettered_all_caps"
    font_family_id: str = "provider-default"
    case: str = "upper"
    weight: str = "regular"
    tracking: float = 0.0
    line_height: float = 1.2
    max_lines: int | None = None
    max_characters: int | None = None
    fill: str = "#ffffff"
    stroke: str = "none"
    shadow: str = "none"
    alignment: str = "left"
    legibility_minimum: float = 12.0
    language_script: str = "Latn"
    license_status: str = "unknown"
    source_uri: str = ""


@dataclass
class BalloonStyle:
    id: str
    kind: str = "speech"
    shape: str = "oval"
    fill: str = "#ffffff"
    border: str = "#111111"
    border_width: float = 2.0
    tail_mode: str = "speaker"
    tail_target_required: bool = True
    opacity: float = 1.0


@dataclass
class SfxDefinition:
    id: str
    cell_id: str
    text: str
    action: str = ""
    force_direction: str = "radial"
    typography_id: str | None = None
    fill: str = "#ffffff"
    outline: str = "#111111"
    offset: float = 0.0
    rotation: float = 0.0
    warp: str = "none"
    z_index: int = 0


@dataclass
class PromptManifest:
    id: str
    artifact_id: str
    template_id: str
    template_version: str = "1"
    prompt_text: str = ""
    layout_style_ids: list[str] = field(default_factory=list)
    typography_style_ids: list[str] = field(default_factory=list)
    balloon_style_ids: list[str] = field(default_factory=list)
    source_ids: list[str] = field(default_factory=list)
    provider: str = "unassigned"
    model: str = "unassigned"
    seed: str | None = None


@dataclass
class LayoutStyle:
    id: str
    family: str = "comic"
    direction: str = "ltr"
    background: str = "#20252d"
    border: str = "#ff3d9a"
    border_width: float = 4.0
    corner_radius: float = 0.0
    gutter: float = 24.0
    padding: float = 24.0
    typography_id: str | None = None


@dataclass
class LayoutSlot:
    id: str
    role: str
    x: float
    y: float
    width: float
    height: float
    label: str = ""
    required: bool = True
    safe_margin: float = 0.0


@dataclass
class CellDefinition:
    id: str
    slot_id: str
    role: str = "beat"
    scene_id: str | None = None
    shot_id: str | None = None
    style_id: str | None = None
    content_kind: str = "image"
    reading_order: int = 0
    text_region_ids: list[str] = field(default_factory=list)
    asset_id: str | None = None
    focal_weight: float = 0.0


@dataclass
class TextRegionDefinition:
    id: str
    cell_id: str
    kind: str = "caption"
    x: float = 0.0
    y: float = 0.0
    width: float = 1.0
    height: float = 1.0
    text: str = ""
    style_id: str | None = None
    balloon_style_id: str | None = None
    typography_id: str | None = None
    speaker_id: str | None = None
    target_anchor: str | None = None
    z_index: int = 0


@dataclass
class LayoutContract:
    id: str
    target: str = "comic-page"
    width: int = 1600
    height: int = 2400
    slots: list[LayoutSlot] = field(default_factory=list)
    overflow_policy: str = "error"
    panel_order: list[str] = field(default_factory=list)
    styles: list[LayoutStyle] = field(default_factory=list)
    cells: list[CellDefinition] = field(default_factory=list)
    text_regions: list[TextRegionDefinition] = field(default_factory=list)
    default_style_id: str | None = None
    gutter_rhythm: str = "regular"
    layout_family: str = "comic_grid"
    typography_styles: list[TypographyStyle] = field(default_factory=list)
    balloon_styles: list[BalloonStyle] = field(default_factory=list)
    sfx_definitions: list[SfxDefinition] = field(default_factory=list)
    prompt_manifests: list[PromptManifest] = field(default_factory=list)


@dataclass
class RenderCheckpoint:
    id: str
    artifact_id: str
    stage: str
    status: str = "pending"
    completed_units: list[str] = field(default_factory=list)
    total_units: list[str] = field(default_factory=list)
    output_ids: list[str] = field(default_factory=list)
    last_error: str = ""
    attempt: int = 0

    @property
    def remaining_units(self) -> list[str]:
        return [unit for unit in self.total_units if unit not in self.completed_units]

    @property
    def resumable(self) -> bool:
        return self.status in {"pending", "partial", "failed"} and bool(self.remaining_units)

    def mark_complete(self, unit_id: str, output_id: str | None = None) -> None:
        if unit_id not in self.completed_units:
            self.completed_units.append(unit_id)
        if output_id and output_id not in self.output_ids:
            self.output_ids.append(output_id)
        self.last_error = ""
        self.status = "complete" if not self.remaining_units else "partial"


@dataclass
class ProductionFinding:
    code: str
    severity: str
    message: str
    path: str


def layout_contract_from_dict(data: dict[str, Any]) -> LayoutContract:
    return LayoutContract(
        **{
            **data,
            "slots": [LayoutSlot(**item) for item in data.get("slots", [])],
            "styles": [LayoutStyle(**item) for item in data.get("styles", [])],
            "cells": [CellDefinition(**item) for item in data.get("cells", [])],
            "text_regions": [TextRegionDefinition(**item) for item in data.get("text_regions", [])],
            "typography_styles": [TypographyStyle(**item) for item in data.get("typography_styles", [])],
            "balloon_styles": [BalloonStyle(**item) for item in data.get("balloon_styles", [])],
            "sfx_definitions": [SfxDefinition(**item) for item in data.get("sfx_definitions", [])],
            "prompt_manifests": [PromptManifest(**item) for item in data.get("prompt_manifests", [])],
        }
    )


def validate_reading_order(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    orders = [cell.reading_order for cell in contract.cells]
    if len(orders) != len(set(orders)):
        findings.append(ProductionFinding("duplicate-reading-order", "error", "cells must have unique reading_order values", "cells"))
    if orders and sorted(orders) != list(range(1, len(orders) + 1)):
        findings.append(ProductionFinding("non-contiguous-reading-order", "warning", "reading_order should be contiguous starting at 1", "cells"))
    return findings


def validate_balloon_tails(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    balloon_ids = {style.id: style for style in contract.balloon_styles}
    for index, region in enumerate(contract.text_regions):
        if region.kind not in {"dialogue", "speech", "whisper", "thought", "shout", "electronic", "ghost"}:
            continue
        path = f"text_regions[{index}]"
        if not region.balloon_style_id:
            findings.append(ProductionFinding("missing-balloon-style", "error", "dialogue region requires balloon_style_id", path))
            continue
        style = balloon_ids.get(region.balloon_style_id)
        if style is None:
            findings.append(ProductionFinding("unknown-balloon-style", "error", f"unknown balloon style: {region.balloon_style_id}", path))
        elif style.tail_target_required and not (region.speaker_id or region.target_anchor):
            findings.append(ProductionFinding("missing-balloon-tail", "error", "balloon requires speaker_id or target_anchor", path))
    return findings


def validate_text_overflow(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    typography = {style.id: style for style in contract.typography_styles}
    for index, region in enumerate(contract.text_regions):
        style = typography.get(region.typography_id or "")
        if style is None:
            continue
        path = f"text_regions[{index}]"
        if style.max_characters is not None and len(region.text) > style.max_characters:
            findings.append(ProductionFinding("text-overflow", "error", f"text exceeds {style.max_characters} characters", path))
        if style.max_lines is not None and region.text.count("\n") + 1 > style.max_lines:
            findings.append(ProductionFinding("text-overflow", "error", f"text exceeds {style.max_lines} lines", path))
    return findings


def validate_focal_cell_dominance(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    if not contract.cells:
        return findings
    slots = {slot.id: slot for slot in contract.slots}
    focal = [cell for cell in contract.cells if cell.role in {"hero", "splash", "reveal"}]
    if not focal:
        return findings

    def area(cell: CellDefinition) -> float:
        slot = slots.get(cell.slot_id)
        return 0.0 if slot is None else slot.width * slot.height

    largest_area = max(area(cell) for cell in contract.cells)
    focal_area = max(area(cell) for cell in focal)
    if focal_area < largest_area:
        findings.append(ProductionFinding("focal-cell-not-dominant", "warning", "hero/splash/reveal cell should dominate page area", "cells"))
    for index, cell in enumerate(contract.cells):
        if cell.focal_weight < 0 or cell.focal_weight > 1:
            findings.append(ProductionFinding("invalid-focal-weight", "error", "focal_weight must be between 0 and 1", f"cells[{index}].focal_weight"))
    if focal and max(cell.focal_weight for cell in focal) == 0:
        findings.append(ProductionFinding("missing-focal-weight", "warning", "hero/splash/reveal cells should declare focal_weight", "cells"))
    return findings



def validate_slot_overlaps(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    for left_index, left in enumerate(contract.slots):
        for right_index in range(left_index + 1, len(contract.slots)):
            right = contract.slots[right_index]
            separated = (
                left.x + left.width <= right.x
                or right.x + right.width <= left.x
                or left.y + left.height <= right.y
                or right.y + right.height <= left.y
            )
            if not separated:
                findings.append(
                    ProductionFinding(
                        "slot-overlap",
                        "error",
                        f"slots overlap: {left.id} and {right.id}",
                        f"slots[{left_index}]",
                    )
                )
    return findings


def validate_references(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    style_ids = {style.id for style in contract.styles}
    typography_ids = {style.id for style in contract.typography_styles}
    balloon_ids = {style.id for style in contract.balloon_styles}
    cell_ids = {cell.id for cell in contract.cells}
    for index, style in enumerate(contract.styles):
        if style.typography_id and style.typography_id not in typography_ids:
            findings.append(ProductionFinding("unknown-typography-style", "error", f"unknown typography style: {style.typography_id}", f"styles[{index}]"))
    for index, region in enumerate(contract.text_regions):
        path = f"text_regions[{index}]"
        for field_name, value, known, code in (
            ("typography_id", region.typography_id, typography_ids, "unknown-typography-style"),
            ("balloon_style_id", region.balloon_style_id, balloon_ids, "unknown-balloon-style"),
        ):
            if value and value not in known:
                findings.append(ProductionFinding(code, "error", f"unknown {field_name}: {value}", path))
        if not 0 <= region.x <= 1 or not 0 <= region.y <= 1 or region.x + region.width > 1 or region.y + region.height > 1:
            findings.append(ProductionFinding("text-region-out-of-bounds", "error", "normalized text region must stay within 0..1 cell bounds", path))
    for index, sfx in enumerate(contract.sfx_definitions):
        path = f"sfx_definitions[{index}]"
        if sfx.cell_id not in cell_ids:
            findings.append(ProductionFinding("unknown-cell", "error", f"SFX references unknown cell: {sfx.cell_id}", path))
        if sfx.typography_id and sfx.typography_id not in typography_ids:
            findings.append(ProductionFinding("unknown-typography-style", "error", f"SFX references unknown typography: {sfx.typography_id}", path))
        if not sfx.text.strip():
            findings.append(ProductionFinding("empty-sfx", "error", "SFX text cannot be empty", path))
    manifest_ids = {manifest.id for manifest in contract.prompt_manifests}
    for index, manifest in enumerate(contract.prompt_manifests):
        path = f"prompt_manifests[{index}]"
        if manifest.artifact_id != contract.id:
            findings.append(ProductionFinding("manifest-artifact-mismatch", "error", "prompt manifest artifact_id must match contract id", path))
        if not manifest.template_id or not manifest.template_version:
            findings.append(ProductionFinding("incomplete-prompt-template", "error", "prompt manifest requires template_id and template_version", path))
        for style_id in manifest.layout_style_ids:
            if style_id not in style_ids:
                findings.append(ProductionFinding("unknown-style", "error", f"manifest references unknown style: {style_id}", path))
        for typography_id in manifest.typography_style_ids:
            if typography_id not in typography_ids:
                findings.append(ProductionFinding("unknown-typography-style", "error", f"manifest references unknown typography: {typography_id}", path))
        for balloon_id in manifest.balloon_style_ids:
            if balloon_id not in balloon_ids:
                findings.append(ProductionFinding("unknown-balloon-style", "error", f"manifest references unknown balloon: {balloon_id}", path))
    if len(manifest_ids) != len(contract.prompt_manifests):
        findings.append(ProductionFinding("duplicate-prompt-manifest", "error", "prompt manifest IDs must be unique", "prompt_manifests"))
    return findings



def validate_layout(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    slot_ids: set[str] = set()
    style_ids: set[str] = set()
    cell_ids: set[str] = set()
    for index, style in enumerate(contract.styles):
        path = f"styles[{index}]"
        if style.id in style_ids:
            findings.append(ProductionFinding("duplicate-style", "error", f"duplicate layout style: {style.id}", path))
        style_ids.add(style.id)
        if style.border_width < 0 or style.corner_radius < 0 or style.padding < 0:
            findings.append(ProductionFinding("invalid-style-geometry", "error", "style geometry cannot be negative", path))
    if contract.default_style_id and contract.default_style_id not in style_ids:
        findings.append(ProductionFinding("unknown-style", "error", f"unknown default style: {contract.default_style_id}", "default_style_id"))

    for index, slot in enumerate(contract.slots):
        path = f"slots[{index}]"
        if slot.id in slot_ids:
            findings.append(ProductionFinding("duplicate-slot", "error", f"duplicate layout slot: {slot.id}", path))
        slot_ids.add(slot.id)
        if slot.width <= 0 or slot.height <= 0:
            findings.append(ProductionFinding("invalid-slot-size", "error", "slot dimensions must be positive", path))
        if slot.x < 0 or slot.y < 0 or slot.x + slot.width > contract.width or slot.y + slot.height > contract.height:
            findings.append(ProductionFinding("layout-overflow", "error", f"slot exceeds {contract.width}x{contract.height} page", path))
        if slot.safe_margin < 0:
            findings.append(ProductionFinding("invalid-safe-margin", "error", "safe margin cannot be negative", path))
    for panel_id in contract.panel_order:
        if panel_id not in slot_ids:
            findings.append(ProductionFinding("unknown-panel", "error", f"panel_order references unknown slot: {panel_id}", "panel_order"))

    for index, cell in enumerate(contract.cells):
        path = f"cells[{index}]"
        if cell.id in cell_ids:
            findings.append(ProductionFinding("duplicate-cell", "error", f"duplicate cell: {cell.id}", path))
        cell_ids.add(cell.id)
        if cell.slot_id not in slot_ids:
            findings.append(ProductionFinding("unknown-slot", "error", f"cell references unknown slot: {cell.slot_id}", path))
        if cell.style_id and cell.style_id not in style_ids:
            findings.append(ProductionFinding("unknown-style", "error", f"cell references unknown style: {cell.style_id}", path))
    for index, region in enumerate(contract.text_regions):
        path = f"text_regions[{index}]"
        if region.cell_id not in cell_ids:
            findings.append(ProductionFinding("unknown-cell", "error", f"text region references unknown cell: {region.cell_id}", path))
        if region.style_id and region.style_id not in style_ids:
            findings.append(ProductionFinding("unknown-style", "error", f"text region references unknown style: {region.style_id}", path))
        if region.width <= 0 or region.height <= 0:
            findings.append(ProductionFinding("invalid-text-region", "error", "text region dimensions must be positive", path))
    findings.extend(validate_slot_overlaps(contract))
    findings.extend(validate_references(contract))
    findings.extend(validate_reading_order(contract))
    findings.extend(validate_balloon_tails(contract))
    findings.extend(validate_text_overflow(contract))
    findings.extend(validate_focal_cell_dominance(contract))
    return findings


def validate_rights(records: list[RightsRecord], required_subject_ids: list[str]) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    by_subject = {record.subject_id: record for record in records}
    allowed = {"owned", "licensed", "public-domain", "cleared", "original"}
    for subject_id in required_subject_ids:
        record = by_subject.get(subject_id)
        if record is None:
            findings.append(ProductionFinding("missing-rights", "error", f"no rights record for {subject_id}", subject_id))
        elif record.status not in allowed:
            findings.append(ProductionFinding("rights-not-cleared", "error", f"rights status is {record.status}: {subject_id}", subject_id))
    return findings


def identity_drift(identity: IdentityMemory, observed_anchors: list[str]) -> list[ProductionFinding]:
    observed = set(observed_anchors)
    required = set(identity.visual_anchors)
    return [
        ProductionFinding("identity-drift", "warning", f"missing approved visual anchor: {anchor}", identity.character_id)
        for anchor in sorted(required - observed)
    ]


def layout_to_svg(contract: LayoutContract, *, title: str = "choTaku page") -> str:
    findings = validate_layout(contract)
    if any(item.severity == "error" for item in findings):
        raise ValueError("; ".join(item.message for item in findings))
    styles = {item.id: item for item in contract.styles}
    default = styles.get(contract.default_style_id or "")
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{contract.width}" height="{contract.height}" viewBox="0 0 {contract.width} {contract.height}">',
        f'<title>{escape(title)}</title>',
        '<rect width="100%" height="100%" fill="#111"/>',
    ]
    cells_by_slot = {cell.slot_id: cell for cell in contract.cells}
    regions_by_cell: dict[str, list[TextRegionDefinition]] = {}
    for region in contract.text_regions:
        regions_by_cell.setdefault(region.cell_id, []).append(region)
    for index, slot in enumerate(contract.slots, start=1):
        cell = cells_by_slot.get(slot.id)
        style = styles.get(cell.style_id if cell and cell.style_id else "", default)
        fill = style.background if style else "#20252d"
        border = style.border if style else "#ff3d9a"
        stroke = style.border_width if style else 4
        radius = style.corner_radius if style else 0
        label = escape((cell.role if cell else slot.label) or slot.role)
        elements.append(
            f'<g id="{escape(slot.id)}"><rect x="{slot.x}" y="{slot.y}" width="{slot.width}" height="{slot.height}" rx="{radius}" fill="{escape(fill)}" stroke="{escape(border)}" stroke-width="{stroke}"/>'
            f'<text x="{slot.x + 24}" y="{slot.y + 48}" fill="#f5f5f5" font-family="sans-serif" font-size="28">{index}. {label}</text></g>'
        )
        for region in regions_by_cell.get(cell.id if cell else "", []):
            text = escape(region.text)
            elements.append(f'<text x="{slot.x + region.x * slot.width}" y="{slot.y + region.y * slot.height}" fill="#fff" font-family="sans-serif" font-size="22">{text}</text>')
    elements.append("</svg>")
    return "".join(elements)


def as_production_dict(value: Any) -> dict[str, Any]:
    return asdict(value)

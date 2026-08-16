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
        }
    )


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

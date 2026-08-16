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
class LayoutContract:
    id: str
    target: str = "comic-page"
    width: int = 1600
    height: int = 2400
    slots: list[LayoutSlot] = field(default_factory=list)
    overflow_policy: str = "error"
    panel_order: list[str] = field(default_factory=list)


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


def validate_layout(contract: LayoutContract) -> list[ProductionFinding]:
    findings: list[ProductionFinding] = []
    seen: set[str] = set()
    for index, slot in enumerate(contract.slots):
        path = f"slots[{index}]"
        if slot.id in seen:
            findings.append(ProductionFinding("duplicate-slot", "error", f"duplicate layout slot: {slot.id}", path))
        seen.add(slot.id)
        if slot.width <= 0 or slot.height <= 0:
            findings.append(ProductionFinding("invalid-slot-size", "error", "slot dimensions must be positive", path))
        if slot.x < 0 or slot.y < 0 or slot.x + slot.width > contract.width or slot.y + slot.height > contract.height:
            findings.append(ProductionFinding("layout-overflow", "error", f"slot exceeds {contract.width}x{contract.height} page", path))
        if slot.safe_margin < 0:
            findings.append(ProductionFinding("invalid-safe-margin", "error", "safe margin cannot be negative", path))
    for panel_id in contract.panel_order:
        if panel_id not in seen:
            findings.append(ProductionFinding("unknown-panel", "error", f"panel_order references unknown slot: {panel_id}", "panel_order"))
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
    missing = sorted(required - observed)
    return [
        ProductionFinding("identity-drift", "warning", f"missing approved visual anchor: {anchor}", identity.character_id)
        for anchor in missing
    ]


def layout_to_svg(contract: LayoutContract, *, title: str = "choTaku page") -> str:
    findings = validate_layout(contract)
    if any(item.severity == "error" for item in findings):
        messages = "; ".join(item.message for item in findings)
        raise ValueError(messages)
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{contract.width}" height="{contract.height}" viewBox="0 0 {contract.width} {contract.height}">',
        f'<title>{escape(title)}</title>',
        f'<rect width="100%" height="100%" fill="#111"/>',
    ]
    for index, slot in enumerate(contract.slots, start=1):
        label = escape(slot.label or slot.role)
        elements.append(
            f'<g id="{escape(slot.id)}"><rect x="{slot.x}" y="{slot.y}" width="{slot.width}" height="{slot.height}" fill="#20252d" stroke="#ff3d9a" stroke-width="4"/>'
            f'<text x="{slot.x + 24}" y="{slot.y + 48}" fill="#f5f5f5" font-family="sans-serif" font-size="28">{index}. {label}</text></g>'
        )
    elements.append("</svg>")
    return "".join(elements)


def as_production_dict(value: Any) -> dict[str, Any]:
    return asdict(value)

"""Core semantic models for the choTaku storyworld compiler.

The models intentionally use only the Python standard library so provider,
database, UI, and MCP layers can evolve independently.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from .production import (
    IdentityMemory,
    LayoutContract,
    layout_contract_from_dict,
    ReaderState,
    RenderCheckpoint,
    RightsRecord,
)


@dataclass
class Character:
    id: str
    name: str
    role: str = "supporting"
    goals: list[str] = field(default_factory=list)
    fears: list[str] = field(default_factory=list)
    wounds: list[str] = field(default_factory=list)
    contradictions: list[str] = field(default_factory=list)
    visual_anchors: list[str] = field(default_factory=list)


@dataclass
class Location:
    id: str
    name: str
    description: str = ""
    sensory_motifs: list[str] = field(default_factory=list)


@dataclass
class LoreEntry:
    id: str
    title: str
    statement: str
    status: str = "provisional"
    sources: list[str] = field(default_factory=list)


@dataclass
class Evidence:
    id: str
    label: str
    kind: str
    description: str = ""
    consequence: str = ""
    discovered: bool = False


@dataclass
class Relationship:
    id: str
    source_id: str
    target_id: str
    kind: str
    tension: str = ""
    history: str = ""
    status: str = "ongoing"
    load_bearing: bool = False


@dataclass
class GraphEdge:
    source_id: str
    target_id: str
    kind: str
    weight: float = 1.0
    notes: str = ""


@dataclass
class SourceRecord:
    id: str
    uri: str
    title: str = ""
    source_type: str = "unknown"
    quality: str = "unassessed"
    accessed_at: str | None = None
    notes: str = ""


@dataclass
class DecisionRecord:
    id: str
    subject: str
    decision: str
    rationale: str = ""
    status: str = "proposed"
    source_ids: list[str] = field(default_factory=list)
    supersedes: str | None = None


@dataclass
class Event:
    id: str
    title: str
    summary: str
    sequence: int
    participants: list[str] = field(default_factory=list)
    location_id: str | None = None
    evidence_ids: list[str] = field(default_factory=list)


@dataclass
class SceneContract:
    id: str
    event_id: str
    purpose: str
    emotional_turn: str
    visual_motif: str
    required_characters: list[str] = field(default_factory=list)
    required_evidence: list[str] = field(default_factory=list)
    continuity_notes: list[str] = field(default_factory=list)


@dataclass
class ShotPlan:
    id: str
    scene_id: str
    shot_type: str
    camera: str = ""
    duration_seconds: float | None = None
    action: str = ""
    dialogue: str = ""
    panel_role: str = "beat"


@dataclass
class StoryWorld:
    id: str
    title: str
    logline: str
    themes: list[str] = field(default_factory=list)
    style_tags: list[str] = field(default_factory=list)
    characters: list[Character] = field(default_factory=list)
    locations: list[Location] = field(default_factory=list)
    lore: list[LoreEntry] = field(default_factory=list)
    evidence: list[Evidence] = field(default_factory=list)
    relationships: list[Relationship] = field(default_factory=list)
    edges: list[GraphEdge] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)
    scene_contracts: list[SceneContract] = field(default_factory=list)
    shots: list[ShotPlan] = field(default_factory=list)
    source_records: list[SourceRecord] = field(default_factory=list)
    decisions: list[DecisionRecord] = field(default_factory=list)
    identity_memories: list[IdentityMemory] = field(default_factory=list)
    reader_states: list[ReaderState] = field(default_factory=list)
    rights_records: list[RightsRecord] = field(default_factory=list)
    layout_contracts: list[LayoutContract] = field(default_factory=list)
    render_checkpoints: list[RenderCheckpoint] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "StoryWorld":
        def many(key: str, typ: type) -> list[Any]:
            return [typ(**item) for item in data.get(key, [])]

        return cls(
            id=data["id"],
            title=data["title"],
            logline=data["logline"],
            themes=data.get("themes", []),
            style_tags=data.get("style_tags", []),
            characters=many("characters", Character),
            locations=many("locations", Location),
            lore=many("lore", LoreEntry),
            evidence=many("evidence", Evidence),
            relationships=many("relationships", Relationship),
            edges=many("edges", GraphEdge),
            events=many("events", Event),
            scene_contracts=many("scene_contracts", SceneContract),
            shots=many("shots", ShotPlan),
            source_records=many("source_records", SourceRecord),
            decisions=many("decisions", DecisionRecord),
            identity_memories=many("identity_memories", IdentityMemory),
            reader_states=many("reader_states", ReaderState),
            rights_records=many("rights_records", RightsRecord),
            layout_contracts=[layout_contract_from_dict(item) for item in data.get("layout_contracts", [])],
            render_checkpoints=many("render_checkpoints", RenderCheckpoint),
            sources=data.get("sources", []),
            metadata=data.get("metadata", {}),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

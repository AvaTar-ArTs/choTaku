"""Core semantic models.

The models intentionally use only the Python standard library so provider,
database, UI, and MCP layers can evolve independently.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


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
    events: list[Event] = field(default_factory=list)
    scene_contracts: list[SceneContract] = field(default_factory=list)
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
            events=many("events", Event),
            scene_contracts=many("scene_contracts", SceneContract),
            sources=data.get("sources", []),
            metadata=data.get("metadata", {}),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

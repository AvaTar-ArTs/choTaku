"""Continuity and reference validation for storyworlds."""

from __future__ import annotations

from dataclasses import dataclass

from .models import StoryWorld


@dataclass
class Finding:
    code: str
    severity: str
    message: str
    path: str


def validate_storyworld(world: StoryWorld) -> list[Finding]:
    """Return deterministic findings without mutating the storyworld."""
    findings: list[Finding] = []
    character_ids = {item.id for item in world.characters}
    location_ids = {item.id for item in world.locations}
    evidence_ids = {item.id for item in world.evidence}
    event_ids = {item.id for item in world.events}
    scene_ids = {item.id for item in world.scene_contracts}
    known_ids = character_ids | location_ids | evidence_ids | event_ids | scene_ids
    source_ids = {item.id for item in world.source_records}

    def missing(value: str, allowed: set[str], code: str, path: str, label: str):
        if value not in allowed:
            findings.append(Finding(code, "error", f"unknown {label} reference: {value}", path))

    for index, event in enumerate(world.events):
        for participant in event.participants:
            missing(participant, character_ids, "unknown-character", f"events[{index}].participants", "character")
        if event.location_id:
            missing(event.location_id, location_ids, "unknown-location", f"events[{index}].location_id", "location")
        for evidence_id in event.evidence_ids:
            missing(evidence_id, evidence_ids, "unknown-evidence", f"events[{index}].evidence_ids", "evidence")

    for index, scene in enumerate(world.scene_contracts):
        missing(scene.event_id, event_ids, "unknown-event", f"scene_contracts[{index}].event_id", "event")
        for character_id in scene.required_characters:
            missing(character_id, character_ids, "unknown-character", f"scene_contracts[{index}].required_characters", "character")
        for evidence_id in scene.required_evidence:
            missing(evidence_id, evidence_ids, "unknown-evidence", f"scene_contracts[{index}].required_evidence", "evidence")

    for index, relation in enumerate(world.relationships):
        missing(relation.source_id, character_ids, "unknown-character", f"relationships[{index}].source_id", "character")
        missing(relation.target_id, character_ids, "unknown-character", f"relationships[{index}].target_id", "character")

    for index, edge in enumerate(world.edges):
        missing(edge.source_id, known_ids, "unknown-node", f"edges[{index}].source_id", "node")
        missing(edge.target_id, known_ids, "unknown-node", f"edges[{index}].target_id", "node")

    for index, shot in enumerate(world.shots):
        missing(shot.scene_id, scene_ids, "unknown-scene", f"shots[{index}].scene_id", "scene")

    for index, decision in enumerate(world.decisions):
        for source_id in decision.source_ids:
            missing(source_id, source_ids, "unknown-source", f"decisions[{index}].source_ids", "source")

    sequences = [event.sequence for event in world.events]
    if len(sequences) != len(set(sequences)):
        findings.append(Finding("duplicate-sequence", "warning", "events share a sequence number", "events"))

    return findings

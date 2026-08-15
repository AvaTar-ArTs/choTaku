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

    sequences = [event.sequence for event in world.events]
    if len(sequences) != len(set(sequences)):
        findings.append(Finding("duplicate-sequence", "warning", "events share a sequence number", "events"))

    return findings

"""Deterministic storyworld compilation."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

from .models import SceneContract, StoryWorld


def _stable_hash(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def compile_storyworld(world: StoryWorld, *, target: str = "comic") -> dict[str, Any]:
    """Compile canon and events into a provider-neutral artifact plan.

    The compiler does not call a model or generate media. It creates the
    semantic contract that downstream providers must satisfy.
    """
    events = sorted(world.events, key=lambda event: event.sequence)
    contracts = {scene.event_id: scene for scene in world.scene_contracts}
    characters = {character.id: character for character in world.characters}
    evidence = {item.id: item for item in world.evidence}
    locations = {location.id: location for location in world.locations}

    scenes: list[dict[str, Any]] = []
    warnings: list[str] = []

    for event in events:
        contract = contracts.get(event.id)
        if contract is None:
            contract = SceneContract(
                id=f"scene-{event.id}",
                event_id=event.id,
                purpose=event.summary,
                emotional_turn="unspecified",
                visual_motif=world.style_tags[0] if world.style_tags else "establishing image",
                required_characters=event.participants,
                required_evidence=event.evidence_ids,
            )
            warnings.append(f"event {event.id} has no explicit scene contract")

        scene_characters = [
            {"id": cid, "name": characters[cid].name, "anchors": characters[cid].visual_anchors}
            for cid in contract.required_characters
            if cid in characters
        ]
        scene_evidence = [
            {"id": eid, "label": evidence[eid].label, "discovered": evidence[eid].discovered}
            for eid in contract.required_evidence
            if eid in evidence
        ]
        location = locations.get(event.location_id) if event.location_id else None

        scenes.append({
            "id": contract.id,
            "event_id": event.id,
            "sequence": event.sequence,
            "purpose": contract.purpose,
            "emotional_turn": contract.emotional_turn,
            "visual_motif": contract.visual_motif,
            "continuity": {
                "characters": scene_characters,
                "location": None if location is None else {
                    "id": location.id,
                    "name": location.name,
                    "motifs": location.sensory_motifs,
                },
                "evidence": scene_evidence,
                "notes": contract.continuity_notes,
            },
            "generation": {
                "prompt_seed": f"{world.id}:{contract.id}:{target}",
                "provider": "unassigned",
                "model": "unassigned",
            },
        })

    plan = {
        "schema_version": "0.1",
        "world": {"id": world.id, "title": world.title, "logline": world.logline},
        "target": target,
        "canon": {
            "themes": world.themes,
            "style_tags": world.style_tags,
            "lore_ids": [item.id for item in world.lore],
            "source_refs": world.sources,
        },
        "scenes": scenes,
        "quality_gates": [
            "time continuity",
            "space continuity",
            "character identity continuity",
            "event and plot continuity",
            "style continuity",
            "theme and purpose continuity",
            "provenance manifest present",
        ],
        "warnings": warnings,
        "provenance": {
            "compiler": "chotaku",
            "compiler_version": "0.1.0",
            "compiled_at": datetime.now(timezone.utc).isoformat(),
            "input_hash": _stable_hash(world.to_dict()),
        },
    }
    plan["plan_hash"] = _stable_hash(plan)
    return plan

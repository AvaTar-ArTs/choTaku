"""Source-ledger and artifact-lineage helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .models import StoryWorld


def source_ledger(world: StoryWorld) -> list[dict[str, Any]]:
    """Return normalized source records, preserving legacy URI strings."""
    records = [
        {
            "id": record.id,
            "uri": record.uri,
            "title": record.title,
            "source_type": record.source_type,
            "quality": record.quality,
            "accessed_at": record.accessed_at,
            "notes": record.notes,
        }
        for record in world.source_records
    ]
    known = {record["uri"] for record in records}
    for index, uri in enumerate(world.sources):
        if uri not in known:
            records.append({
                "id": f"legacy-source-{index + 1}",
                "uri": uri,
                "title": "",
                "source_type": "legacy",
                "quality": "unassessed",
                "accessed_at": None,
                "notes": "Imported from StoryWorld.sources.",
            })
    return records


def decision_ledger(world: StoryWorld) -> list[dict[str, Any]]:
    return [
        {
            "id": decision.id,
            "subject": decision.subject,
            "decision": decision.decision,
            "rationale": decision.rationale,
            "status": decision.status,
            "source_ids": decision.source_ids,
            "supersedes": decision.supersedes,
        }
        for decision in world.decisions
    ]


def manifest(*, world: StoryWorld, plan_hash: str, target: str) -> dict[str, Any]:
    return {
        "manifest_version": "0.1",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "world_id": world.id,
        "target": target,
        "plan_hash": plan_hash,
        "sources": source_ledger(world),
        "decisions": decision_ledger(world),
        "lineage": {
            "characters": [item.id for item in world.characters],
            "locations": [item.id for item in world.locations],
            "events": [item.id for item in world.events],
            "scene_contracts": [item.id for item in world.scene_contracts],
        },
    }

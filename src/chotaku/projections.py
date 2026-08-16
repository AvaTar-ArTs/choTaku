"""Storyboard and page projections from compiled artifact plans."""

from __future__ import annotations

from typing import Any

from .production import LayoutContract


def storyboard_projection(plan: dict[str, Any]) -> dict[str, Any]:
    """Create a readable storyboard projection without changing the plan."""
    rows: list[dict[str, Any]] = []
    for scene in plan.get("scenes", []):
        shots = scene.get("shots") or [{
            "id": f"{scene.get('id')}-panel",
            "panel_role": "beat",
            "action": scene.get("purpose", ""),
            "dialogue": "",
        }]
        for index, shot in enumerate(shots, start=1):
            rows.append({
                "sequence": len(rows) + 1,
                "scene_id": scene.get("id"),
                "shot_id": shot.get("id"),
                "panel_role": shot.get("panel_role", "beat"),
                "action": shot.get("action", ""),
                "dialogue": shot.get("dialogue", ""),
                "emotional_turn": scene.get("emotional_turn", ""),
                "visual_motif": scene.get("visual_motif", ""),
                "continuity": scene.get("continuity", {}),
                "generation": scene.get("generation", {}),
            })
    return {
        "view": "storyboard",
        "target": plan.get("target"),
        "world": plan.get("world"),
        "rows": rows,
        "count": len(rows),
    }


def page_projection(
    plan: dict[str, Any],
    contract: LayoutContract,
    *,
    asset_ids: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Bind storyboard units to declarative layout slots."""
    storyboard = storyboard_projection(plan)
    assets = asset_ids or {}
    bindings: list[dict[str, Any]] = []
    for index, slot in enumerate(contract.slots):
        row = storyboard["rows"][index] if index < len(storyboard["rows"]) else None
        bindings.append({
            "slot_id": slot.id,
            "role": slot.role,
            "geometry": {
                "x": slot.x,
                "y": slot.y,
                "width": slot.width,
                "height": slot.height,
            },
            "storyboard_unit": None if row is None else row["shot_id"],
            "asset_id": None if row is None else assets.get(row["shot_id"]),
            "required": slot.required,
        })
    return {
        "view": "page",
        "layout_id": contract.id,
        "target": contract.target,
        "dimensions": {"width": contract.width, "height": contract.height},
        "bindings": bindings,
    }

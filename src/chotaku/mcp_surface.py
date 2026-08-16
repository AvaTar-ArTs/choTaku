"""Read-only MCP-shaped functions for choTaku integrations.

A transport server can expose these functions over MCP without moving semantic
authority out of choTaku.
"""

from __future__ import annotations

from typing import Any, Callable

from .compiler import compile_storyworld
from .graph import graph_summary, timeline_view
from .models import StoryWorld
from .validation import validate_storyworld


def _load(payload: dict[str, Any]) -> StoryWorld:
    return StoryWorld.from_dict(payload)


def inspect_storyworld(payload: dict[str, Any]) -> dict[str, Any]:
    world = _load(payload)
    return {
        "id": world.id,
        "title": world.title,
        "logline": world.logline,
        "counts": {
            "characters": len(world.characters),
            "locations": len(world.locations),
            "events": len(world.events),
            "scenes": len(world.scene_contracts),
            "shots": len(world.shots),
            "sources": len(world.source_records) + len(world.sources),
            "layouts": len(world.layout_contracts),
        },
        "graph": graph_summary(world),
        "timeline": timeline_view(world),
    }


def validate_storyworld_payload(payload: dict[str, Any]) -> dict[str, Any]:
    findings = validate_storyworld(_load(payload))
    return {
        "valid": not any(item.severity == "error" for item in findings),
        "findings": [item.__dict__ for item in findings],
    }


def compile_storyworld_payload(payload: dict[str, Any], target: str = "comic") -> dict[str, Any]:
    return compile_storyworld(_load(payload), target=target)


def tool_manifest() -> list[dict[str, Any]]:
    return [
        {"name": "inspect_storyworld", "mutating": False},
        {"name": "validate_storyworld", "mutating": False},
        {"name": "compile_storyworld", "mutating": False},
    ]


def dispatch(name: str, payload: dict[str, Any], *, target: str = "comic") -> Any:
    handlers: dict[str, Callable[..., Any]] = {
        "inspect_storyworld": inspect_storyworld,
        "validate_storyworld": validate_storyworld_payload,
        "compile_storyworld": lambda value: compile_storyworld_payload(value, target=target),
    }
    if name not in handlers:
        raise KeyError(f"unknown read-only choTaku tool: {name}")
    return handlers[name](payload)

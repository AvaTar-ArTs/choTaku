"""Graph and projection helpers for storyworld authoring views."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from .models import GraphEdge, StoryWorld


def graph_summary(world: StoryWorld) -> dict[str, Any]:
    nodes = []
    for collection, kind in (
        (world.characters, "character"),
        (world.locations, "location"),
        (world.lore, "lore"),
        (world.evidence, "evidence"),
        (world.events, "event"),
    ):
        nodes.extend({"id": item.id, "kind": kind} for item in collection)

    edges = [
        {
            "source": edge.source_id,
            "target": edge.target_id,
            "kind": edge.kind,
            "weight": edge.weight,
            "notes": edge.notes,
        }
        for edge in world.edges
    ]
    edges.extend({
        "source": relation.source_id,
        "target": relation.target_id,
        "kind": relation.kind,
        "weight": 1.0,
        "notes": relation.tension,
    } for relation in world.relationships)

    return {"nodes": nodes, "edges": edges}


def timeline_view(world: StoryWorld) -> list[dict[str, Any]]:
    return [
        {
            "id": event.id,
            "sequence": event.sequence,
            "title": event.title,
            "summary": event.summary,
            "participants": event.participants,
            "location_id": event.location_id,
        }
        for event in sorted(world.events, key=lambda item: item.sequence)
    ]


def adjacency(world: StoryWorld) -> dict[str, list[GraphEdge]]:
    result: dict[str, list[GraphEdge]] = defaultdict(list)
    result.update({node["id"]: [] for node in graph_summary(world)["nodes"]})
    result.update()
    for edge in world.edges:
        result[edge.source_id].append(edge)
    return dict(result)

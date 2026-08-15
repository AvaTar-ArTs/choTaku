import json
from pathlib import Path

from chotaku.compiler import compile_storyworld
from chotaku.models import DecisionRecord, GraphEdge, Relationship, SourceRecord, StoryWorld


def load_example():
    path = Path(__file__).parents[1] / "examples" / "crimson-curse-master.json"
    return StoryWorld.from_dict(json.loads(path.read_text()))


def test_compiler_preserves_event_order_and_contract():
    plan = compile_storyworld(load_example(), target="manga")
    assert plan["target"] == "manga"
    assert plan["scenes"][0]["event_id"] == "the-first-choosing"
    assert plan["scenes"][0]["emotional_turn"] == "confidence becomes intimate dread"
    assert plan["scenes"][0]["continuity"]["evidence"][0]["id"] == "living-sigil"


def test_compiler_warns_when_contract_is_missing():
    world = load_example()
    world.scene_contracts = []
    plan = compile_storyworld(world)
    assert "event the-first-choosing has no explicit scene contract" in plan["warnings"]


def test_compilation_includes_research_graph_and_manifest():
    world = load_example()
    world.relationships.append(Relationship(
        id="self-curse",
        source_id="curse-master",
        target_id="curse-master",
        kind="haunted-by",
        tension="he cannot tell whether the curse is instrument or author",
        load_bearing=True,
    ))
    world.edges.append(GraphEdge(
        source_id="the-first-choosing",
        target_id="living-sigil",
        kind="reveals",
    ))
    world.source_records.append(SourceRecord(
        id="source-1",
        uri="https://example.invalid/research",
        title="Research note",
        source_type="academic",
        quality="secondary",
    ))
    world.decisions.append(DecisionRecord(
        id="decision-1",
        subject="curse-agency",
        decision="The curse can choose before the ritual is complete.",
        rationale="Preserves reciprocal agency.",
        status="canon",
        source_ids=["source-1"],
    ))
    plan = compile_storyworld(world)
    assert plan["views"]["graph"]["edges"][0]["kind"] == "haunted-by"
    assert plan["research"]["decisions"][0]["status"] == "canon"
    assert plan["artifact_manifest"]["plan_hash"] == plan["plan_hash"]


def test_compilation_is_hashable_and_provider_neutral():
    plan = compile_storyworld(load_example())
    assert len(plan["provenance"]["input_hash"]) == 64
    assert plan["scenes"][0]["generation"]["provider"] == "unassigned"
    assert len(plan["plan_hash"]) == 64

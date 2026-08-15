import json
from pathlib import Path

from chotaku.compiler import compile_storyworld
from chotaku.models import StoryWorld


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


def test_compilation_is_hashable_and_provider_neutral():
    plan = compile_storyworld(load_example())
    assert len(plan["provenance"]["input_hash"]) == 64
    assert plan["scenes"][0]["generation"]["provider"] == "unassigned"
    assert len(plan["plan_hash"]) == 64

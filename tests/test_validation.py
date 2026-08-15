import json
from pathlib import Path

from chotaku.models import StoryWorld
from chotaku.validation import validate_storyworld


def load_example():
    path = Path(__file__).parents[1] / "examples" / "crimson-curse-master.json"
    return StoryWorld.from_dict(json.loads(path.read_text()))


def test_example_has_no_reference_errors():
    assert validate_storyworld(load_example()) == []


def test_unknown_reference_is_reported():
    world = load_example()
    world.events[0].participants.append("missing-character")
    findings = validate_storyworld(world)
    assert findings[0].code == "unknown-character"
    assert findings[0].severity == "error"

"""Command-line interface for choTaku."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .compiler import compile_storyworld
from .models import StoryWorld


def main() -> int:
    argv = sys.argv[1:]
    if argv and argv[0] == "compile":
        argv = argv[1:]

    parser = argparse.ArgumentParser(description="Compile a choTaku storyworld.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--target",
        default="comic",
        choices=["comic", "manga", "webtoon", "graphic-novel", "storyboard", "video"],
    )
    args = parser.parse_args(argv)

    world = StoryWorld.from_dict(json.loads(args.input.read_text(encoding="utf-8")))
    plan = compile_storyworld(world, target=args.target)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    print(f"compiled {world.title!r}: {len(plan['scenes'])} scenes → {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

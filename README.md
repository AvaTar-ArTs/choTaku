# choTaku

## The story does not begin with a prompt.

**choTaku** is AvatarArts’ provider-neutral storyworld compiler: a system for turning context, research, character psychology, lore, evidence, and creative intent into reproducible narrative artifacts.

It is the implementation home for the ideas developed across:

- **Origin Story** — reverse-engineering, research comprehension, source ledgers, and capability synthesis
- **Chozen Land** — context → meaning → canon → graph → narrative → artifacts
- **AvatarArts Comic Creator Matrix** — comic, manga, webtoon, graphic-novel, cinematic, and animated production
- **AvatarArts Forge** — evidence-to-artifact compilation, continuity, provenance, and quality gates

choTaku is not another “prompt-to-comic” wrapper. It owns the semantic layer that most creator tools leave implicit.

## Core pipeline

```text
Context
  ↓
Meaning
  ↓
Canon + psychology + lore + evidence
  ↓
Story graph + timeline + scene contracts
  ↓
Narrative / panel / shot plans
  ↓
Provider adapters
  ↓
Artifacts: comic · manga · webtoon · graphic novel · storyboard · video
  ↓
Continuity, provenance, critique, publication
```

## What the first kernel provides

- Typed storyworld, character, location, lore, event, scene, and artifact-plan models
- A deterministic compiler from storyworld data to an artifact plan
- Research-led source and decision ledgers with quality and supersession fields
- Typed relationships, graph edges, timelines, and cinematic shot plans
- Explicit scene contracts for visual and narrative continuity
- Provider-neutral generation boundaries
- Agent-role and skill-capability manifests
- Provenance manifests for prompts, models, providers, inputs, outputs, and decisions
- JSON Schema for interoperable storyworld data
- A CLI suitable for later MCP, web, notebook, or batch adapters

## Design principles

1. **Canon before generation.** Generated assets are downstream of structured world knowledge.
2. **Psychology is causal.** Goals, fears, wounds, contradictions, and costs shape scenes.
3. **Evidence changes state.** Clues, relics, rituals, discoveries, and consequences are first-class.
4. **Continuity is testable.** Time, space, character, event, style, and theme receive explicit checks.
5. **Providers are replaceable.** No model vendor owns the story.
6. **Every artifact has ancestry.** Outputs carry a manifest linking them to sources, decisions, prompts, and versions.
7. **One semantic core, many surfaces.** Comics, manga, novels, animation, games, and websites are render targets.
8. **Adapt patterns; do not copy systems wholesale.** Research informs architecture while choTaku remains proprietary.

## Quick start

```bash
python -m pip install -e ".[dev]"

chotaku compile examples/crimson-curse-master.json \
  --output build/crimson-curse-plan.json

pytest
```

## Repository map

```text
src/chotaku/
  models.py       typed semantic objects
  compiler.py     deterministic storyworld → artifact compilation
  graph.py        graph, timeline, and authoring-view projections
  provenance.py   source ledger, decision ledger, and manifests
  validation.py   continuity and reference checks
  cli.py          command-line entrypoint
schemas/
  storyworld.schema.json
agents/
  manifest.yaml   role cards and handoff contracts
skills/
  manifest.yaml   reusable capability lenses
docs/
  architecture.md research-derived architecture and boundaries
  mcp-contract.md transport-neutral tool and resource contracts
  creative-history-audit.md evidence-bounded conversation and creative-system audit
  visual-layout-stabilization.md layout contracts, slot rules, and prompt grammar
  expanded-repository-scan-2026-08.md further comics, manga, graphic-book, and storyboard research
  visual-language-research-2026-08-15.md typography, lettering, cell grammar, and prompt templates
  visual-reference-template-atlas-2026-08-15.md vision-derived dossier, comic, manga, light-novel, spread, and webtoon templates
  first-party-invokeai-audit.md first-party visual-generation substrate audit
  mcp-integration-map.md MCP transport and provider-boundary map
  avatararts-repository-constellation-audit-2026-08-15.md full first-party repository ecosystem audit
  hidden-python-systems-audit-2026-08-15.md recursive Python capability and subsystem audit
  research-derived-production-features.md implemented identity, rights, checkpoint, layout, and SVG contracts
  research-to-implementation.md research → implementation map
examples/
  crimson-curse-master.json
  choosing-to-be-chosen.json  creation fixture: the Curse of Knowing
fixtures/
  layouts/          LTR, RTL, vertical-scroll, dossier, storyboard, signal, origin, and Curse of Knowing dry-run contracts
tests/
  test_compiler.py
```

## Visual reference atlas

The visual reference atlas documents eight supplied first-party reference images as reusable layout families: signal dossier board, signal profile sheet, volume taxonomy board, origin comic page, system-breach irregular page, open-book spread, and webtoon transformation stack. It also records prompt templates, stabilization rules, external research links, and the mapping to TypographyStyle, BalloonStyle, SfxDefinition, and PromptManifest.

Read [docs/visual-reference-template-atlas-2026-08-15.md](docs/visual-reference-template-atlas-2026-08-15.md).

## Generated visual atlas series

The generated visual atlas series is preserved under [assets/visual-atlas](assets/visual-atlas) with provenance and intended-use notes in [docs/generated-visual-atlas-series.md](docs/generated-visual-atlas-series.md). It covers six-world universe DNA, genre grammars, layout systems, sequential page systems, cross-format style variation, and genre-specific page rhythm.

## Visual contract dry run

The executable [Curse of Knowing dry-run fixture](fixtures/layouts/curse-of-knowing-dry-run.json) renders the story premise “choosing to be chosen” through the origin-comic layout family. Its regression test validates the contract, checks references and geometry, and produces a deterministic SVG preview.

## Creative-history audit

The repository includes an evidence-bounded audit of the AvatarArts, Chozen Land, Origin Story, ichoTaKu, TrashCat, HeartBreak Alley, and multimodal production history in [docs/creative-history-audit.md](docs/creative-history-audit.md).

## Status

choTaku begins as a compact, inspectable kernel. Planned expansions include:

- bidirectional graph editing
- source-ledger ingestion and evidence confidence
- panel and shot grammar
- visual identity/reference adapters
- typography, balloon, caption, SFX, reading-order, focal-weight, overlap, and reference-integrity contracts
- image, audio, video, lettering, and layout providers
- MCP tools
- web authoring surface
- asset catalog and search
- continuity and reader-simulation gates
- publication and localization adapters

## License

To be determined by the repository owner.

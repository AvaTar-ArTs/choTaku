# choTaku architecture

## Why choTaku exists

Research across comic generators, storyworld tools, agentic planners, visual-story authoring systems, creator platforms, and multimodal production pipelines showed a repeated pattern: useful projects exist at individual layers, but their semantic boundaries are usually implicit.

choTaku makes those boundaries explicit.

## Layer model

| Layer | Owns | Must not own |
|---|---|---|
| Context | briefs, sources, references, constraints | canon decisions made without trace |
| Meaning | themes, questions, interpretation, intent | provider-specific prompts |
| Canon | entities, lore, psychology, relationships, rules | final pixels |
| Graph | timeline, event dependencies, spatial and causal links | untracked edits |
| Narrative | beats, scene purpose, emotional turns | arbitrary visual drift |
| Artifact plan | panels, pages, scrolls, shots, lettering, audio | vendor credentials |
| Provider adapter | model calls, rendering, transformation | story authority |
| Provenance | lineage, hashes, prompts, versions, decisions | unverifiable claims |
| Quality gate | continuity, safety, craft, publication checks | silent mutation |

## Research-derived decisions

### From visual story authoring

Stories should be editable through multiple synchronized views:

- entity view for characters, objects, and places
- spatial view for location and composition
- timeline view for sequence and duration
- action/event view for causality and change

choTaku starts with an interchange representation that can support those views later.

### From worldbuilding and planning systems

Long-form consistency requires explicit state. A character is not just a prompt description; a character has identity, psychology, relationships, knowledge, injuries, possessions, and change over time.

### From creator pipelines

Rendering, colorization, layout, lettering, video, and publishing should be adapters downstream of a stable artifact plan. That keeps the semantic core independent from any one model or application.

### From Origin Story

Reverse-engineering and research claims need a source ledger, confidence, decision record, and explicit distinction between observed behavior, interpretation, and proposed adaptation.

## First implementation boundary

The first kernel is intentionally small:

```text
JSON storyworld
  → typed models
  → deterministic scene contracts
  → provider-neutral artifact plan
  → provenance and quality-gate declarations
```

No model call occurs inside the compiler. This makes it testable, reproducible, and safe to connect to MCP or external providers later.

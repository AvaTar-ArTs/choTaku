# Research-derived production features

This document records the first implementation slice derived from the expanded comic, manga, storyboard, novel-to-comic, visual-canvas, character-memory, and declarative-markup research.

## Implemented contracts

- IdentityMemory: approved visual anchors, negative anchors, reference assets, versions, and continuity notes.
- ReaderState: what the reader already knows, what is newly revealed, and what remains unresolved.
- RightsRecord: ownership, licensing, public-domain, clearance, restrictions, and pre-generation gating.
- LayoutStyle: reusable visual grammar for a page or cell, including family, direction, colors, borders, gutters, padding, and typography references.
- LayoutContract and LayoutSlot: declarative page geometry, panel order, safe boundaries, and overflow validation.
- CellDefinition: the semantic unit inside a slot, including role, scene/shot binding, content kind, asset identity, style reference, and reading order.
- TextRegionDefinition: explicit caption, dialogue, title, sound, or metadata region with normalized geometry and style reference.
- RenderCheckpoint: resumable stage/unit execution with remaining work and output lineage.
- identity_drift: deterministic fixture-friendly identity evaluation.
- layout_to_svg: dependency-free declarative SVG page projection that resolves slot, cell, style, reading-order, and text-region definitions.

A layout slot is therefore only geometry. A cell defines what the slot is for; a layout style defines how it is rendered; a text region defines where words live; and the contract defines how the reader traverses the page.

## Adaptation principles

The external systems contributed patterns, not product architecture:

- persistent identity memory becomes a typed semantic record;
- page and storyboard tools become layout contracts;
- novel-to-comic workflows become rights, bible, script, brief, QC, and export stages;
- agentic video systems become resumable checkpoints and stage projections;
- comic markup becomes a provider-neutral SVG projection;
- reader-state fields become part of scene design rather than an afterthought;
- panel templates become explicit cell roles and reusable layout styles rather than hidden renderer conventions.

## Next layer

The next implementation should connect these contracts to StoryWorld and compiler output:

1. load production records from JSON;
2. emit identity, rights, reader, and layout sections in artifact plans;
3. block generation when required rights are not cleared;
4. create character-drift and layout-overflow fixture packs;
5. add PDF/CBZ adapters downstream of the SVG/page contract;
6. expose read-only inspection and validation through MCP;
7. retain every render checkpoint in Evoked-compatible records.

The system should preserve the core rule: approved identity memory + story-first planning + declarative layout + resumable production + provenance-aware export.

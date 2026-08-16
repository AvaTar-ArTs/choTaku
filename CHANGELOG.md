## 2026-08-15 — Generated visual atlas series

### Added

- Six compressed JPEG concept atlases under assets/visual-atlas.
- Provenance guide connecting generated references to visual-language research and the AvatarArts creative corpus.
- Cross-world layout references for Heart Break Alley, Signal Garden, Dominion Parade, ichoTAKU, Woolie/Thread Benders, and altered-state mythology.
- Genre, page-rhythm, cross-format, and sequential-art examples for future LayoutContract fixtures and prompt manifests.

# Changelog

## 2026-08-15 — Vision-derived visual reference atlas

### Added

- Vision-derived layout atlas for eight supplied AvatarArts reference images.
- Reusable signal dossier, signal profile, volume taxonomy, origin comic, system-breach, open-book spread, and webtoon transformation families.
- Prompt templates that lock cell count, slot order, focal dominance, text-safe zones, identity memory, gutters, and reading direction.
- Research links covering comic page anatomy, manga flow, lettering, speech balloons, webtoon pacing, and light-novel profile presentation.
- Example fixtures for signal_dossier_board and origin_comic_page with exact style IDs, semantic cells, text regions, SFX, and prompt manifests.

### Architectural implications

- Cell geometry and visual grammar are now treated as reusable template families rather than one generic comic grid.
- Gutter rhythm is semantic: regular for clarity, wide for pause, stepped for escalation, and scroll-pause for mobile reveal.
- Character boards and light-novel profiles require identity repetition across portrait, full-body, prop, detail, silhouette, and emblem cells.
- External references inform composition vocabulary; supplied first-party imagery remains the evidence source for AvatarArts-specific signal-punk signatures.

See docs/visual-reference-template-atlas-2026-08-15.md.

## 2026-08-15 — Visual language contracts

### Added

- TypographyStyle, BalloonStyle, SfxDefinition, and PromptManifest dataclasses.
- Text-region balloon, typography, speaker, target-anchor, and z-index fields.
- Layout gutter rhythm, layout family, typography, balloon, SFX, and prompt-manifest collections.
- Deterministic reading-order, balloon-tail, text-overflow, and focal-cell dominance validators.
- Executable ltr_grid, rtl_grid, ttb_scroll, dossier_grid, and storyboard_shot fixtures.
- Regression tests and CI compilation coverage for the visual-language fixture pack.

## 2026-08-15 — Creation test: The Curse of Knowing

### Added

- Full storyworld fixture for “choosing to be chosen” and the Curse of Knowing.
- Character psychology, reciprocal curse lore, evidence, relationships, five-scene arc, reader states, identity memories, rights records, render checkpoint, manga layout, cells, and text regions.
- Compiler regression test proving the fixture produces five ordered scenes and a production contract.

### Narrative premise

The protagonist is not gifted with generic omniscience. They are forced to see probable consequences while remaining unable to know why a choice is worth making. The dramatic resolution is choosing meaning after certainty.

## 2026-08-15 — Visual language research and prompt stabilization

### Added

- Research dossier for comic, manga, graphic-novel, webtoon, storyboard, and otaku visual grammar.
- Font and lettering taxonomy with semantic font-family contracts.
- Balloon, caption, metadata, title, and sound-effect definitions.
- Panel, cell, block, gutter, splash, dossier, storyboard, and vertical-scroll patterns.
- Explicit reading-direction guidance for LTR print, RTL manga, TTB webtoon, and custom layouts.
- AvatarArts signal-punk, hidden-signal broadcast, and dark anime evidence-wall signatures derived from supplied first-party imagery.
- Prompt templates for layout stability, identity consistency, lettering placement, SFX, signal-punk boards, and quality control.
- YAML contract sketch showing how styles, cells, slots, and text regions work together.
- Font ecosystem research, licensing boundaries, and typography manifest fields.
- Source-quality classification and research caveats.

### Architectural implications

- Layout geometry, cell semantics, visual style, typography, balloon voice, SFX behavior, and provenance should remain independently addressable.
- Numeric platform heuristics must live in target profiles rather than the semantic core.
- Text overflow, reading-order ambiguity, balloon misattribution, and identity drift should be blocking or reviewable findings.
- Future contracts should add TypographyStyle, BalloonStyle, and SfxDefinition.

### Sources

See docs/visual-language-research-2026-08-15.md for the complete source list, evidence boundary, and adaptation notes.

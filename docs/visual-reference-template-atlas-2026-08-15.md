# Visual Reference Template Atlas — 2026-08-15

This atlas converts eight supplied AvatarArts reference images into reusable, provider-neutral layout families for choTaku. It combines visual inspection of the supplied files with external composition and lettering research. The supplied images are treated as first-party visual evidence, not as claims about an external standard.

## Evidence boundary

| Evidence | What it supports | Confidence |
| --- | --- | --- |
| Supplied images 1–8 | Observable geometry, hierarchy, palette roles, typography behavior, information blocks, signature motifs | High for visual description |
| Comic and manga composition references | General panel/page/spread vocabulary, reading direction, gutters, splash and grid patterns | Medium; instructional sources vary |
| Webtoon references | Vertical-scroll pacing, mobile-first sequencing, variable gutter rhythm | Medium; platform conventions change |
| Light-novel profile references | Character-card, stat-card, volume-index and editorial-board patterns | Medium; examples are format inspiration |
| Font foundries and lettering guides | Semantic lettering roles, licensing/provenance concerns | High for the cited foundry or guide; not a universal font prescription |

## Research synthesis

A useful visual compiler needs three scales: cell, page, and spread. The page is not merely a collection of rectangles; panel size, gutters, direction, captions, balloons, SFX, and focal dominance jointly control pacing and navigation. Manga pages commonly use right-to-left flow and variable cinematic panel sizes; Western comic pages commonly use left-to-right tiered grids; webtoon pages turn vertical spacing into timing; a light-novel character page often combines portrait, name, attributes, and editorial metadata.

Useful external references:

- [VCU: Text as Art](https://gallery.library.vcu.edu/exhibits/show/considering-comics/text-as-art) — lettering, display text, balloons, and SFX are compositional marks.
- [Todd Klein: Balloon Placement](https://kleinletters.com/BalloonPlacement.html) — balloon position and tail direction affect the read.
- [Clip Studio: Speech balloons](https://tips.clip-studio.com/en-us/articles/4811) — balloon construction and lettering are separable production concerns.
- [Clip Studio: Webtoon paneling](https://tips.clip-studio.com/en-us/articles/9420) — vertical-scroll paneling requires a different pacing model.
- [Creative Bloq: Comic panels](https://www.creativebloq.com/art/how-to-draw-comic-panels) — thumbnailing is a layout discovery pass before finish work.
- [MangaFlow: Paneling basics](https://mangaflow.studio/blog/manga-panels-paneling-basics) — panel size, gutters, and sequence shape reader rhythm.
- [Comic Template Maker](https://gettemplated.com/comic-template/) — reusable page grids and print-oriented presets.
- [Comistitch: Vertical-scroll paneling](https://comistitch.com/blog/webtoon-vertical-scroll-paneling-guide/) — gutters can be treated as deliberate pauses in mobile reading.
- [Creative Review: Marvel by Design](https://www.creativereview.co.uk/marvel-by-design-book-liz-stinson/) — page anatomy, tiers, balloons, captions, SFX, and eye path.
- [Adobe Comicraft](https://fonts.adobe.com/foundries/comicraft) and [Adobe Blambot](https://fonts.adobe.com/foundries/blambot) — lettering is a semantic role and a licensing decision, not an afterthought.

## Vision-derived templates

### 1. Signal Dossier Board

Evidence: supplied images 1 and 4; related prior choTaku/TrashCat boards.

- Target: landscape graphic novel, character dossier, worldbuilding evidence wall.
- Canvas: 3:2 landscape.
- Structure: title/broadcast band across the top; dominant hero cell at roughly 45–50% of page area; right-side file card and close-up/action evidence; lower-right notes, frequency, and transmission log; bottom sequence strip with six numbered cells; signature footer.
- Reading order: title → file card/hero → action evidence → notes/log → sequence strip → signature.
- Signature features: near-black ground, hot magenta primary, white text, electric-blue secondary, waveform, barcode, Japanese/English broadcast header, icon row, technical borders.
- Stability rule: reserve text-safe zones before image generation; never let the hero overlap the file card or sequence strip.

Prompt template:

> Use the locked signal_dossier_board layout, 3:2 landscape. Keep the title band at the top, one dominant hero cell on the left, a file card and close-up evidence cells on the upper right, a notes/log rail below, a six-cell transmission strip at the bottom, and a final signature panel. Preserve exact cell count, slot order, margins, gutters, and text-safe regions. Use near-black, hot magenta, white, and electric blue. Generate art inside cells only; do not invent panels, move captions, or merge cells.

### 2. Signal Profile Sheet

Evidence: supplied image 2.

- Target: character reference sheet, light-novel character board, profile-card presentation.
- Canvas: 3:2 landscape.
- Structure: narrow status rail on the left; wide logo/title band; large seated or posed hero; right portrait/action cells; lower specimen strip with face, full-body, instrument/prop, eye/detail, silhouette, and emblem.
- Reading order: status rail → title → file card → hero → action → specimen strip → progress/signature bar.
- Signature features: neon sign, moon, skyline, cassette/radio prop, locked identity costume, progress bar.
- Stability rule: use the hero as the identity anchor; all specimen cells must repeat the same hair, face markings, costume, emblem, and palette.

Prompt template:

> Build a signal_profile_sheet character board in 3:2 landscape. Anchor identity in the large hero cell. Repeat the same approved character memory in portrait, back-view/action, face close-up, full-body, prop, eye/detail, silhouette, and emblem cells. Keep the left status rail and bottom specimen strip fixed. Place all labels in reserved black metadata zones. No new costume, species, accessory, or logo variant.

### 3. Volume Taxonomy Board

Evidence: supplied image 3.

- Target: light-novel series board, graphic-novel catalog, TikTok/banner/profile package.
- Canvas: 3:2 landscape or modular multi-artboard.
- Structure: narrow profile/avatar column; wide banner with title and subject; five equal volume cards; repeatable second series row.
- Reading order: identity/profile → banner → volumes I–V.
- Signature features: condensed display serif/blackletter title, volume numbering, editorial subtitle, artifact stills, dark archive palette with a controlled accent color.
- Stability rule: every volume card uses the same title, synopsis, image, and metadata coordinates.

Prompt template:

> Render a volume_taxonomy_board as an editorial archive. Keep one profile column, one wide banner, and five equal volume cards. Use a consistent title baseline, volume numbering, caption height, and image crop. Treat each card as a data-bound cell, not a freeform poster. Preserve the selected palette and typography roles across all cards.

### 4. Origin Comic Page

Evidence: supplied images 5 and 8.

- Target: LTR comic, graphic novel origin page, short-form “how it began” beat.
- Canvas: portrait 2:3.
- Structure: title band; two upper story cells; two lower transformation/reveal cells; optional final caption strip.
- Reading order: title → upper-left cause → upper-right intervention → lower-left failure/transition → lower-right identity reveal.
- Signature features: thick cream gutters, distressed ink, caption boxes, controlled limited palette, one readable SFX, one dominant reveal.
- Stability rule: the reveal cell must dominate the final beat without reducing the earlier cause/effect cells below legibility.

Prompt template:

> Render an origin_comic_page in 2:3 portrait with exactly five cells: title, cause, intervention, failure/transition, reveal. Use thick cream gutters and a dark teal/green base with one warm accent. Caption boxes stay in their reserved top or bottom zones. The reveal is the largest visual beat; preserve left-to-right, top-to-bottom reading order and do not add panels.

### 5. System Breach Irregular Page

Evidence: supplied image 6.

- Target: cyber-occult action page, manga-inspired rupture page, dramatic reveal.
- Canvas: portrait 2:3.
- Structure: narrow vertical logo/detail rail; tall character cell; small system-status and SFX cells; large lower reveal cell; callout captions.
- Reading order: status mark → breach signal → body/detail → system declaration → large reveal.
- Signature features: irregular cell sizes, teal/cyan glow, orange warning lights, cream caption plaques, oversized distressed title/SFX.
- Stability rule: irregularity must remain intentional; every cell still has an explicit reading order and anchor.

Prompt template:

> Render a system_breach_irregular_page: a controlled irregular grid with one tall character cell, one detail stack, one system-status callout, one SFX cell, and one dominant lower reveal. Preserve the declared z-order and caption anchors. Use teal/cyan night shadows, orange warning accents, and cream plaques. Irregular borders may vary, but cells may not overlap or disappear.

### 6. Open-Book Spread

Evidence: supplied image 7.

- Target: graphic-novel spread, light-novel chapter opener, cinematic character introduction.
- Canvas: 3:2 landscape representing two facing pages.
- Structure: left page title/glyph/object studies; central binding gutter; right-page full-body reveal with two narration blocks.
- Reading order: left title → left symbolic studies → binding transition → right character → narration close.
- Signature features: page curvature, central gutter, teal/cyan glyphs, dark city background, yellow editorial narration.
- Stability rule: keep critical face, title, and narration outside the binding safety zone.

Prompt template:

> Render a two-page open_book_spread with a visible but controlled central binding curve. Left page: title and symbolic studies. Right page: one full-body character reveal and two narration blocks. Keep all critical text and eyes outside the gutter. Use one shared environment across both pages; no duplicated character or broken horizon.

### 7. Webtoon Transformation Stack

Derived from supplied portrait pages 5, 6, and 8 plus vertical-scroll research.

- Target: mobile webtoon, serialized vertical reveal, scroll-first manga adaptation.
- Canvas: tall TTB scroll, split into mobile-safe chunks.
- Structure: hook panel; short setup beats; isolated object/detail beat; generous reveal gutter; tall reveal; post-reveal caption.
- Reading order: top to bottom only.
- Signature features: variable vertical gutters, short action cells, tall reveal cell, readable caption bars, deliberate scroll pause.
- Stability rule: gutter rhythm is semantic: tight for action, medium for reaction, wide before reveal. Validate each chunk independently.

Prompt template:

> Render a webtoon_transformation_stack in top-to-bottom order. Use short setup cells, one isolated detail cell, a deliberate pause before the reveal, one tall reveal cell, and a closing caption. Keep the mobile-safe text width constant. Gutters must be explicit and deterministic; do not collapse the reveal pause or place dialogue outside its cell.

## Contract mapping

Each template maps to existing choTaku contracts:

- LayoutContract.layout_family: selects the family.
- LayoutContract.gutter_rhythm: selects regular, wide, stepped, or scroll-pause spacing.
- LayoutStyle: controls palette, border, gutter, padding, and direction.
- LayoutSlot: fixes the geometry and safe margin.
- CellDefinition: names the semantic role, scene, content kind, reading order, and text regions.
- TypographyStyle: selects title, dialogue, caption, metadata, narration, or SFX behavior.
- BalloonStyle: declares speech/thought/shout/system shape, border, fill, tail mode, and target requirement.
- SfxDefinition: declares action, force direction, warp, rotation, and z-index.
- PromptManifest: records template ID/version, exact prompt, style IDs, source IDs, provider/model, and seed.

## Global stabilization rules

1. Lock the page family before writing image prompts.
2. Lock slots and cell count before generating art.
3. Give every cell a role, scene ID, reading order, focal weight, and safe margin.
4. Keep text as a separate render layer whenever possible; generated lettering is reference-only unless checked.
5. Put balloons in reading order, then point tails to explicit character anchors.
6. Reserve caption zones before composition; never “find room” for text after rendering.
7. Use one identity memory for face, silhouette, costume, emblem, prop, and palette.
8. Treat gutters as timing: regular for clarity, wide for pause, stepped for escalation, scroll-sized for mobile rhythm.
9. Block publication on text overflow, ambiguous reading order, missing balloon targets, and a non-dominant focal cell.
10. Record template, style IDs, source references, prompt, provider, model, and seed in the manifest.

## Adaptation notes

Adapt the compositional principles, not copyrighted page designs, logos, characters, or proprietary font files. The supplied AvatarArts boards establish a distinctive signal-punk/dossier grammar through recurring structural motifs; they do not imply that every future artifact should use the same palette or subject. Use the semantic family plus a target profile so choTaku can render the same story as manga, LTR comic, light-novel board, graphic-novel spread, or webtoon without losing canon or provenance.

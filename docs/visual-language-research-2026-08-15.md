# Visual language research: comics, manga, graphic novels, webtoons, and otaku media

**Research date:** 2026-08-15  
**Scope:** typography, lettering, panel/cell grammar, captions, balloons, gutters, reading direction, page rhythm, webtoon scroll behavior, visual references, and prompt stabilization.

This is an evidence-bounded design reference for choTaku. It distinguishes observed conventions from proposed AvatarArts adaptations. Sources are retained so a visual decision can be revisited rather than treated as taste without provenance.

## Core conclusion

A comic page is not an image divided into rectangles. It is a synchronized system:

~~~text
story beat
  → cell role
  → panel geometry
  → reading order
  → visual hierarchy
  → lettering/text regions
  → gutter rhythm
  → asset/provenance constraints
~~~

Each layer needs its own definition. The same illustration can read as a calm reveal, frantic action, dream sequence, dossier, or joke depending on panel scale, gutters, balloon order, lettering, contrast, and placement.

## Definitions choTaku should preserve

| Definition | Owns | Does not own |
|---|---|---|
| Layout family | print grid, manga page, webtoon scroll, splash, dossier, storyboard, cinematic board | story meaning |
| Layout contract | page/canvas dimensions, slots, safe margins, overflow policy, reading direction | provider prompts |
| Layout style | color, border, gutter defaults, padding, tone, texture, typography references | character identity |
| Cell definition | role, scene/shot binding, content kind, asset binding, reading order | final pixels |
| Text region | caption/dialogue/title/SFX/metadata geometry and text | speaker identity unless explicitly linked |
| Balloon style | speech, whisper, thought, shout, electronic, ghost, off-panel, chorus | page geometry |
| Lettering style | font family, case, weight, tracking, line length, fill/stroke, hierarchy | narrative canon |
| SFX definition | word, action, force direction, deformation, outline, overlap, palette | dialogue |
| Reader state | known facts, new reveal, open question, intended pause | rendering |
| Identity memory | approved anchors, negative anchors, references, evolution/version | layout |
| Provenance | source, license, prompt, model, seed, edit history, decision | aesthetic judgment |

## Font and lettering taxonomy

Font names are implementation details; the semantic family is the durable contract.

| Family | Use | Shape/behavior | Avoid |
|---|---|---|---|
| Hand-lettered all-caps | default dialogue | irregular but controlled, generous interior space, strong readability | distressed texture that destroys glyphs |
| Narrow grotesk / condensed sans | captions, dossier labels, metadata | compact, factual, high information density | long prose at tiny size |
| Bold display brush | titles, declarations, emotional emphasis | variable stroke, angled energy, asymmetry | using it for every line |
| Rounded manga dialogue | light banter, youth, slice-of-life | soft terminals, open counters, relaxed rhythm | pairing with grimdark horror without contrast |
| Monospace terminal | transmissions, logs, technical notes | fixed rhythm, machine voice, scanline/dossier feel | body dialogue |
| Serif literary | narration, historical text, graphic novel voiceover | measured cadence and authority | mixing unrelated serif families |
| Blackletter / occult display | ritual, faction, metal, dark fantasy | dense silhouette, ceremonial authority | small captions or accessibility-critical text |
| Pixel / bitmap | retro game, broadcast, glitch, cybernetic UI | discrete square rhythm | print-scale body copy |
| Brush-script Japanese display | title accents, signage, sound effects | vertical energy, expressive stroke | untranslated decorative text that implies meaning |
| Symbolic mark / logo lettering | project identity and recurring motif | recognizable silhouette independent of reading | replacing plain-text metadata |

### Lettering variables that deserve explicit fields

- font_family_id
- semantic_family
- case: upper, sentence, mixed, vertical
- weight
- tracking
- line_height
- max_lines
- max_characters
- fill
- stroke
- shadow
- alignment
- rotation
- warp
- balloon_style_id
- legibility_minimum
- language_script
- provenance

Text should be placed before final art generation. This follows practical lettering guidance that balloons and copy must be reserved during composition, not pasted into whatever space remains.

## Balloon and caption grammar

| Text object | Visual contract | Narrative function |
|---|---|---|
| Speech balloon | smooth container, clear tail to mouth/speaker | spoken dialogue |
| Whisper balloon | lighter/smaller treatment, reduced emphasis | secrecy, distance, vulnerability |
| Thought balloon | scalloped/cloud contour or interior marks | internal voice |
| Shout burst | jagged contour, heavier weight, expanded scale | impact, alarm, rage |
| Electronic balloon | angular/jagged or segmented contour, signal texture | radio, AI, machine, broadcast |
| Ghost/echo balloon | broken, fading, translucent, offset contour | memory, haunting, disembodied voice |
| Off-panel balloon | tail terminates at edge or source direction | unseen speaker |
| Chorus/group balloon | multiple tails or shared container | collective voice |
| Caption box | rectangular/architectural container | time, place, narrator, system status |
| Whisper caption | restrained box, low contrast, small scale | private or subliminal narration |
| SFX lettering | freeform, integrated with action and force lines | sound, motion, impact, environment |
| Title/logo | silhouette-first display treatment | identity and entry point |
| Metadata label | compact neutral text with strict alignment | dossier, file, frequency, episode, continuity |

### Balloon placement rules

1. Place dialogue regions before image prompts are finalized.
2. The first speaker appears earlier in the reading path: left-to-right for Western layouts, right-to-left for traditional manga, top-to-bottom for scroll layouts.
3. Tails should terminate near the speaker’s mouth or clearly indicate off-panel direction.
4. Avoid covering eyes, mouths, identity anchors, action-critical hands, and focal props.
5. Keep balloon interiors optically balanced; equal mathematical padding is not always equal visual padding.
6. Default to no more than three dialogue balloons in a dense cell unless the contract intentionally permits overlap.
7. Validate balloon order independently from panel order.
8. Treat text overflow as a blocking quality failure, not a cosmetic warning.

## Panel, cell, and block patterns

| Pattern | Geometry | Best for | Rhythm |
|---|---|---|---|
| Establishing wide | wide horizontal cell | location, world state, arrival | slow entry |
| Dominant hero cell | largest cell on page | identity reveal, emotional anchor | pause/emphasis |
| Reaction strip | 3–6 narrow cells | dialogue beats, micro-expressions | quick |
| Match-cut pair | two cells with repeated composition | transformation, contrast, before/after | deliberate |
| Inset detail | small cell inside/over main cell | eye, hand, relic, clue | attention spike |
| Stair-step cascade | offset cells descend diagonally | pursuit, escalation, falling, discovery | accelerating |
| Splash page | one dominant image with sparse text | climax, title, world reveal | suspended |
| Silent page | minimal/no dialogue | grief, awe, aftermath, visual metaphor | contemplative |
| Dossier grid | modular labels + image blocks | character file, world bible, archive | informational |
| Cinematic storyboard | shot cells with camera/action labels | production planning | procedural |
| Modular manga grid | uneven but bounded cells | standard page storytelling | flexible |
| Borderless bleed | art crosses page boundary | dream, memory, scale, rupture | unbounded |
| Negative-space reveal | large empty area before focal beat | suspense, loneliness, anticipation | delayed payoff |
| Vertical-scroll ladder | tall cells separated by deliberate gutters | webtoon/mobile reading | thumb-controlled |
| Split-screen | parallel columns/rows | simultaneous action, call/response | comparative |
| Diagrammatic panel | art + arrows/labels/callouts | technical, magical, investigative explanation | explanatory |

Suggested CellDefinition roles:

~~~text
establishing, hero, reaction, action, transition, detail, clue, reveal,
flashback, memory, silent, dialogue, splash, dossier, diagram,
storyboard_shot, credits, title
~~~

## Gutter rhythm

The gutter is elapsed time, not leftover whitespace.

- tight gutter: immediate continuity, rapid exchange, urgency
- normal gutter: ordinary beat transition
- wide gutter: reflection, scene change, time passage
- extreme gutter: anticipation, cliffhanger, emotional suspension
- overlapping/no gutter: collision, simultaneity, psychic rupture, montage

For webtoon-style scrolls, use relative rhythm tokens rather than one universal pixel value:

~~~yaml
gutter_rhythm:
  action: tight
  dialogue: regular
  reaction: medium
  scene_transition: wide
  reveal: extra_wide
  cliffhanger: extreme
~~~

Absolute sizes belong in target-specific adapters because print, browser, and mobile viewport behavior differ.

## Reading directions

- ltr_grid: Western comics and most English-first print layouts.
- rtl_grid: traditional manga page flow.
- ttb_scroll: webtoon/manhwa vertical scroll.
- custom: experimental or interactive layouts; requires explicit ordered cells.

Reading direction must be declared at the layout-contract level and inherited by cells only when not overridden. A page should expose a machine-readable reading_order, not force a renderer to guess from coordinates.

## Visual signature patterns for AvatarArts / choTaku

These patterns are proposed adaptations from the supplied choTaku/TrashCat, nocturneMeLody, dossier, and profile-board imagery, not claims that every image shares one exact style.

### Signal-punk dossier

- near-black field
- hot magenta as activation color
- white/gray information text
- one cold counter-color such as electric blue
- thin technical frames
- distressed edges used as texture, not as a substitute for hierarchy
- file cards, barcodes, signal traces, frequency labels
- one dominant identity image plus modular evidence cells
- recurring emblem or glyph
- bilingual or pseudo-broadcast header treatment only when meaning is controlled

### Otaku broadcast / hidden-signal board

- title/logo at the entry point
- character portrait as identity anchor
- quote or mission statement as emotional hook
- supporting action/reaction/detail cells
- recurring icon row
- transmission sequence strip
- final signature line or logo lockup
- deliberate contrast between dossier precision and punk hand-lettering

### Dark anime evidence wall

- cinematic hero crop
- close-up eye/detail insert
- setting establishing frame
- back-view or silhouette frame
- prop/weapon/object evidence
- annotation rail
- limited palette with one luminous accent
- caption hierarchy separating canon facts from mood language

## Image research: what the references teach

The visual references found during research repeatedly demonstrate:

1. Anatomy diagrams make panels, tiers, gutters, tails, captions, and SFX explicit. This supports choTaku’s typed cell/text-region model.
2. Webtoon guides use panel variation and generous vertical gaps to control thumb speed and emotional dwell time.
3. Manga reading-order examples show that balloon order must be modeled, not inferred only from panel coordinates.
4. Historical lettering guides show that balloon shape communicates voice: standard, whisper, thought, ghost, electronic, and scream are different semantics.
5. Professional lettering guidance treats text placement as part of composition and recommends reserving space before final drawing.
6. Sound-effect tutorials show that SFX lettering is an illustrated object: it follows force lines, changes scale, overlaps art, and uses outline/offset treatment.
7. The supplied AvatarArts images show a strong recurring language: dark field, hot magenta/white contrast, dossier framing, radio/broadcast metadata, modular identity studies, repeated emblemography, and a final signature panel.

## Prompt templates

### Stable page-layout prompt

~~~text
Create a [FORMAT] page using an explicit [LAYOUT_FAMILY] layout.
Canvas: [WIDTH]x[HEIGHT], [READING_DIRECTION].
Use exactly [N] cells in this order: [CELL_IDS].
Cell geometry:
- [CELL_ID]: [ROLE], x=[X], y=[Y], w=[W], h=[H], priority=[PRIORITY]

Reserve safe margins of [MARGIN] and gutters of [GUTTER_TOKEN].
Do not add, remove, merge, or reorder cells.
Keep the dominant focal cell at [FOCAL_CELL_ID].
Reserve text regions before rendering:
- [TEXT_ID]: [KIND], inside [CELL_ID], [PLACEMENT], max [LINES] lines

Style: [STYLE_ID]. Palette: [PALETTE].
Line treatment: [LINE_STYLE]. Texture: [TEXTURE].
The output must read clearly at thumbnail size and preserve all borders,
margins, cell identities, and reading order.
~~~

### Character identity stabilization prompt

~~~text
Use the approved identity memory for [CHARACTER_ID] as immutable.
Preserve: [VISUAL_ANCHORS].
Do not introduce: [NEGATIVE_ANCHORS].
Reference assets: [REFERENCE_IDS].
Scene role: [ROLE]. Emotion: [EMOTION]. Pose/action: [ACTION].
Keep face shape, eye color, hair/silhouette, costume anchors, emblem placement,
body proportions, and signature props consistent across all cells.
Change only: [ALLOWED_VARIATIONS].
Match the page style [STYLE_ID] without changing identity.
~~~

### Speech and caption placement prompt

~~~text
Letter the page after respecting the declared reading direction [DIRECTION].
Place text regions in reading order [TEXT_ORDER].
Use [BALLOON_STYLE_ID] for [SPEAKER_OR_FUNCTION].
Keep tails aimed at [TARGETS], never at empty space.
Do not cover eyes, mouths, hands, identity anchors, or the primary action.
Use [FONT_FAMILY] / [SEMANTIC_FAMILY], [CASE], [WEIGHT], [MAX_LINES] lines,
[ALIGNMENT], [FILL], [STROKE], and [PADDING].
If text does not fit, report TEXT_OVERFLOW rather than shrinking below [MIN_SIZE].
~~~

### SFX prompt

~~~text
Render the sound effect “[WORD]” as an illustrated action object.
Action: [ACTION]. Force direction: [VECTOR].
Deform letters along the force line; emphasize [IMPACT_LETTERS].
Use fill [FILL], outline [OUTLINE], offset [OFFSET], and palette [PALETTE].
Allow overlap with art only in [ALLOWED_REGION].
Keep the SFX legible at thumbnail size and do not obscure the speaker or focal prop.
~~~

### AvatarArts signal-punk board prompt

~~~text
Create a signal-punk character/story dossier board for [SUBJECT].
Use a near-black ground, hot magenta activation color, white information text,
and [COUNTER_COLOR] as the restrained secondary signal color.
Layout family: dossier_grid. Reading direction: ltr_grid.
Include: title lockup, identity portrait, full-body or hero action frame,
close-up detail, establishing city/world frame, evidence/prop cell,
transmission strip, metadata card, recurring emblem, and final signature panel.
Use thin technical frames, controlled distress, radio-frequency motifs,
barcodes or file identifiers, and deliberate negative space.
Typography hierarchy: [TITLE_STYLE], [METADATA_STYLE], [DIALOGUE_STYLE], [SFX_STYLE].
Do not let decorative glyphs replace legible canonical text.
Preserve the approved identity memory and keep all cell positions stable.
~~~

### Quality-control prompt

~~~text
Audit this page against its production contract.
Check:
- reading order
- cell count and cell IDs
- slot bounds and safe margins
- gutter rhythm
- balloon/text-region order
- text overflow and minimum legibility
- tail attribution
- character identity drift
- style/palette drift
- focal hierarchy
- SFX collision with faces, props, and borders
- provenance and rights status

Return machine-readable findings with severity BLOCKER, WARNING, or NOTE.
Do not silently repair canon, layout, or identity.
~~~

## JSON/YAML design sketch

~~~yaml
layout_contract:
  id: cho-page-001
  family: dossier_grid
  target: print
  direction: ltr_grid
  default_style_id: signal-punk
  styles:
    - id: signal-punk
      family: comic
      background: "#09090d"
      border: "#ff3d9a"
      gutter: 24
      padding: 24
      typography_id: signal-punk-type
  cells:
    - id: hero
      slot_id: slot-hero
      role: hero
      scene_id: scene-01
      style_id: signal-punk
      content_kind: image
      reading_order: 1
  text_regions:
    - id: mission-caption
      cell_id: hero
      kind: caption
      x: 0.06
      y: 0.08
      width: 0.36
      height: 0.12
      text: "Every alley has a story."
      style_id: signal-punk
~~~

## Font research and licensing boundary

The research separates font inspiration from font redistribution:

| Font ecosystem | Best use in choTaku | Licensing note |
|---|---|---|
| Blambot | dialogue, captions, SFX, display lettering | verify the exact font license; free does not automatically mean embeddable or redistributable |
| Comicraft | professional comic dialogue, manga translation, display and logo lettering | Adobe Fonts usage is distinct from self-hosting, application embedding, or shipping font files |
| Open-license families | metadata, captions, UI, multilingual support | store the license and version in the typography manifest |
| Custom/generated lettering | logos, signature marks, one-off SFX | preserve editable vector/source provenance and avoid treating a rasterized sample as a reusable font |

Useful references include [Comicraft on Adobe Fonts](https://fonts.adobe.com/foundries/comicraft), [Blambot on Adobe Fonts](https://fonts.adobe.com/fonts/blambot), [Wildwords](https://www.fontspring.com/fonts/comicraft/wildwords), and [Squarejaw Intl BB](https://www.fontbros.com/font-family/squarejaw-intl-bb). These are research references and licensing leads, not an instruction to bundle commercial font files.

For choTaku, typography manifests should record:

~~~yaml
typography:
  id: signal-punk-dialogue
  semantic_family: hand_lettered_all_caps
  font_family_id: provider-or-license-specific-id
  license_status: verified | restricted | unknown
  allowed_uses: [rendered_image, pdf, web, app]
  embedding: prohibited | permitted | unknown
  fallback_family_id: open-license-fallback
  source_uri: https://example.invalid
~~~

The safe default is to generate rendered text or SVG paths through a licensed provider, retain the font provenance, and never silently redistribute a font file whose license has not been checked.

## Source quality and caveats

| Source class | Examples | Use |
|---|---|---|
| Professional/industry craft source | Todd Klein lettering guides, Clip Studio Tips, Creative Bloq | craft rules and practical heuristics |
| Institutional/educational source | VCU Considering Comics | medium theory and semantic role of text |
| Visual reference/tutorial | anatomy diagrams, layout infographics, lettering examples | pattern discovery, not universal law |
| Commercial product guidance | webtoon and creator-tool blogs | platform-oriented heuristics; verify before hard-coding |
| Supplied AvatarArts images | choTaku/TrashCat, nocturneMeLody, dossier/profile boards | first-party style evidence and motif extraction |
| Search-result secondary source | blogs and roundups | leads only; retain caveats and do not treat claims as standards |

Numeric dimensions such as “200px gutters” or “800px webtoon width” are platform- or tutorial-specific heuristics, not universal comic laws. choTaku should store them as target-profile defaults with provenance, not bake them into the semantic core.

## Research sources

- [VCU Libraries: Text as Art](https://gallery.library.vcu.edu/exhibits/show/considering-comics/text-as-art)
- [Todd Klein: Balloon Placement](https://kleinletters.com/BalloonPlacement.html)
- [Todd Klein: Charlton’s Lettering Guide](https://kleinletters.com/Blog/how-to-charltons-lettering-guide/)
- [Clip Studio Tips: Speech Balloon Placement](https://tips.clip-studio.com/en-us/articles/4811)
- [Clip Studio Tips: Paneling Comics for Webtoon and Print](https://tips.clip-studio.com/en-us/articles/9420)
- [Creative Bloq: Creating a Manga Comic Strip](https://www.creativebloq.com/how-to/how-to-create-a-manga-comic-strip)
- [Creative Bloq: How to Draw Comic Panels](https://www.creativebloq.com/art/how-to-draw-comic-panels)
- [MangaFlow: Manga Panels and Paneling Basics](https://mangaflow.studio/blog/manga-panels-paneling-basics)
- [Oniichan: Manga Panel Layouts Guide](https://www.oniichan.app/blog/manga-panel-layouts-guide-8-layouts-every-creator-should-know)
- [Manga Structure and Composition visual reference](https://www.inhisperfectimage.com/post/manga-structure-and-composition)
- [Comicory: Comic Book Lettering](https://www.comicory.com/blog/comic-book-lettering)
- [Coloso webtoon layout reference](https://coloso.global/zh-TW/products/webtoonartist-sakon-us)

## Implemented production extension

The visual-language contract layer now includes:

1. TypographyStyle, BalloonStyle, and SfxDefinition dataclasses beside the layout contracts.
2. Text-region fields for balloon_style_id, typography_id, speaker_id, target_anchor, and z_index.
3. LayoutContract fields for gutter_rhythm, layout_family, typography styles, balloon styles, SFX definitions, and prompt manifests.
4. Deterministic validators for reading order, balloon tails, text overflow, and focal-cell dominance.
5. Executable fixture packs for ltr_grid, rtl_grid, ttb_scroll, dossier_grid, and storyboard_shot under fixtures/layouts.
6. PromptManifest records containing the exact template, version, style IDs, source IDs, provider/model placeholders, and seed.

The remaining adapter work is to make providers consume these contracts directly and to add richer geometry-aware text measurement once a renderer is selected.

# Visual layout stabilization system

This document converts the supplied ichoTaKu, Nocturne Melody, Zombot, and profile mockup images into reusable layout contracts.

The goal is not to force every generation into one composition. The goal is to make placement intentional and recoverable.

## Reference set

| Reference | Format | Primary lesson |
|---|---:|---|
| ichoTaKu broadcast sheets | 16:9 | masthead + hero + broadcast panels + transmission strip |
| ichoTaKu dossier boards | 3:2 / 1:1 | hero image balanced against identity dossier and evidence panels |
| Nocturne Melody banners | ultra-wide | title lockup, central figure, frequency statement, compact campaign variants |
| ichoTaKu profile mockup | 1:1 | identity banner, avatar lockup, feed card, metadata rail |
| Zombot page | 2:3 | title band, narration blocks, sequential comic panels, final reveal |
| square ichoTaKu boards | 1:1 | portrait identity, scene progression, asset/reference strip, signature lockup |

## Layout contracts

### Broadcast dossier — `broadcast-dossier-16x9`

Use for a character/world introduction, identity sheet, lore broadcast, or signal transmission.

Rules:

- Reserve the upper-left for the identity mark and title.
- Keep the hero subject inside a 5% inset safe area.
- Keep the dossier text inside a fixed right-column width.
- Use the bottom strip for sequence, not new story information.
- Keep the signature statement in one stable terminal slot.
- Do not let decorative glyphs cross the title, face, or dossier text.

### Signal board — `signal-board-3x2`

Use for a lore page, evidence board, album-world sheet, or character mythology.

Rules:

- Large visual anchor occupies the left or upper-left.
- Evidence panels form a deliberate counterweight on the right.
- Every panel receives a role: `identity`, `evidence`, `action`, `symbol`, `transition`, or `signature`.
- A panel cannot contain more than one high-priority focal subject.
- Use a consistent border, gutter, and caption system across all panels.

### Portrait dossier — `portrait-dossier-1x1`

Use for avatars, character cards, profile mockups, or social identity surfaces.

Rules:

- Keep the face/mascot in a predictable portrait zone.
- Put identity data in a separate card, never over the face.
- Reserve the bottom band for signature, symbols, or CTA.
- Never ask the image model to render dense exact UI copy; reserve exact text for post-layout typography.

### Vertical comic page — `comic-page-2x3`

Use for short comics, biographies, tutorials, or lore reveals.

Rules:

- Title band: 8–12%.
- Panels: 68–78%.
- Final consequence or signature: 12–18%.
- Narration boxes use one consistent corner and padding.
- Speech balloons are placed after the image stage when exact reading order matters.
- Maintain a left-to-right or top-to-bottom reading path; do not mix directions without a visual cue.

### Campaign banner — `campaign-banner-ultrawide`

Use for Nocturne Melody-style headers, music projects, channel art, and launch graphics.

Rules:

- Title lockup occupies one-third of the width.
- Subject occupies the opposing third.
- Center remains low-detail breathing room or atmospheric texture.
- Use one primary phrase and one secondary frequency/genre line.
- Keep logos and symbols away from crop edges.

## Placement stabilizer

Every generated layout should carry these fields:

- `canvas`: target width, height, and aspect ratio
- `grid`: columns, rows, gutter, outer margin
- `slots`: named regions with normalized coordinates
- `safe_zones`: regions reserved for faces, titles, text, logos, and cropping
- `reading_order`: explicit sequence
- `focal_hierarchy`: primary, secondary, tertiary
- `text_policy`: generated placeholder text versus post-layout exact text
- `continuity_anchors`: identity, costume, palette, props, motifs, location
- `asset_roles`: hero, dossier, evidence, action, symbol, signature
- `render_passes`: image pass, typography pass, finishing pass

## Prompt grammar

Use prompts in this order:

1. **Medium and target:** `editorial storyworld dossier, 16:9 landscape`
2. **Layout contract:** `fixed broadcast-dossier grid, hero left, dossier right, six-panel transmission strip along bottom`
3. **Subject identity:** `ichoTaKu / TrashCat, pink mohawk, black-and-white raccoon, black studded jacket, pink eyes`
4. **Scene content:** `rooftop alley, neon city, pink moon, guitar, hidden broadcast`
5. **Visual DNA:** `crimson-black, hot magenta, controlled blue accent, glitchpunk VHS texture, ink-heavy manga linework`
6. **Placement constraints:** `keep face in left-center hero slot; keep right dossier region dark and uncluttered; keep bottom strip readable and evenly spaced`
7. **Typography policy:** `leave clean reserved areas for exact typography; no pseudo-text; no extra logos`
8. **Negative constraints:** `no duplicate character, no merged panels, no cropped title, no text crossing the face, no random UI clutter`

## Master prompt template

```text
Create a [TARGET FORMAT] using the [LAYOUT CONTRACT] layout.

SUBJECT:
[identity, species, role, wardrobe, visual anchors]

STORY FUNCTION:
[what this page communicates and what changes]

LAYOUT:
[slot-by-slot placement, normalized zones, reading order, panel roles]

VISUAL DNA:
[palette, linework, texture, lighting, camera language, typography mood]

CONTINUITY:
[persistent identity anchors, props, motifs, location, state]

TEXT POLICY:
Leave clean reserved regions for exact post-layout text:
[TITLE SLOT], [DOSSIER SLOT], [CAPTION SLOTS], [SIGNATURE SLOT].
Do not invent or distort readable copy.

PLACEMENT LOCK:
Keep [subject] in [slot]. Keep [text/logo] in [slot].
Keep [negative space] in [slot].
Preserve gutters, borders, panel count, reading order, and safe margins.

NEGATIVE:
[unwanted layouts, duplicates, tangencies, illegible text, cropped elements, accidental focal points]
```

## Stabilization workflow

```text
reference images
→ identify layout archetype
→ assign semantic slots
→ lock identity anchors
→ generate image-only composition
→ add exact typography and UI in a layout pass
→ inspect crop and reading order
→ validate continuity
→ export manifest
```

The strongest references combine a stable identity mark, one dominant character anchor, a dossier/evidence layer, a recognizable palette, repeatable panel grammar, a signature transmission phrase, and controlled imperfection.

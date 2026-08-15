# Expanded repository scan: comics, manga, graphic books, storyboards, and visual narratives

**Search date:** 2026-08-15  
**Scope:** GitHub repositories and topics, skills.sh, Hugging Face, and adjacent creator tooling.  
**Method:** repository archaeology: stated intent → observed workflow → reusable pattern → boundary → choTaku adaptation.

## Search families

- AI comic and manga generators
- graphic-novel and novel-to-comic adaptation
- storyboarding and shot planning
- page-template and panel-layout editors
- picture-book and PDF authoring
- visual-story graphs and canvas systems
- character-consistency memory
- comic-to-video and agentic video production
- creative skills and prompt libraries

## High-value discoveries

| System | Category | What it actually contributes | Boundary |
|---|---|---|---|
| [Storyboarder](https://github.com/wonderunit/storyboarder) | storyboard editor | Fast drawing, Fountain screenplay intake, reference layers, onion skin, playback, exports, Photoshop handoff | Previsualization; no semantic canon or multimodal asset lineage |
| [Comic Template Maker](https://github.com/binarynonsense/comic-template-maker) | page layout | Custom dimensions, colors, layouts, manga/American presets, panel grids, PNG/JPG/PSD/PDF export | Layout utility; not narrative intelligence |
| [Agent Mangaka Forge](https://github.com/RemiPelloux/agent-mangaka-forge) | agent skill | Persistent `img-memory`, character versions, base/variant/evolution references, manga page and storyboard workflow | Strong visual-memory pattern; small skill package, not a complete world model |
| [Codex Novel-to-Comic Studio](https://github.com/lhfer/codex-novel-to-comic-studio) | novel adaptation | Rights gate, source parsing, narrative/visual bibles, story-first page plans, page scripts, director briefs, QC, PDF/CBZ | Closest external production-desk pattern; needs a richer semantic graph and provider-neutral core |
| [Comic Book Movie Creator](https://github.com/lalomorales22/comic-book-movie-creator) | comic-to-motion | Character model-sheet approval, collaborative storyboard, 16-page generation, selected-panel animation, narration and assembly | Strong approval sequence; tightly coupled to Gemini/Veo-style execution |
| [ViMax](https://github.com/hkuds/vimax) | agentic video | Director/screenwriter/producer/generator roles, Idea2Video, Script2Video, Novel2Video, web UI, checkpoints, provider settings | Broad orchestration reference; video-first and not comic/page-native |
| [Bibliogon](https://github.com/astrapi69/bibliogon) | book authoring | Storyboard grid, page layouts, drag-positioned image/text regions, entity filters, beat tags, comic panel templates, PDF pipeline | Excellent authoring/layout pattern; semantic story model is lighter than choTaku's |
| [Comic Studio AI](https://github.com/RobinaMirbahar/Comic-Studio-Ai) | multi-agent comic generator | Story generation, character consistency, speech bubbles, refinement agent, API/UI delivery | End-to-end generator; inspect contracts and failure handling before adapting |
| [Make Comics](https://github.com/nutlope/make-comics) | AI comic generator | Generates stories, characters, and panels; references prior pages and uploaded character images | Useful page continuity pattern; limited canon/provenance layer |
| [ComicBook-AI](https://github.com/AvaTar-ArTs/ComicBook-AI) | first-party reference | Creator UI, storage/search/publishing direction | First-party implementation history; security remediation already required |
| [comic-cult](https://github.com/AvaTar-ArTs/comic-cult) | first-party reference | Dialogue, rendering, composition, PDF delivery | First-party implementation history; needs stronger manifests and delivery safeguards |
| [comics_generator](https://github.com/AvaTar-ArTs/comics_generator) | first-party reference | Scenario-to-panel decomposition, JSON parsing, asset manifests | First-party reliability reference; requires regression and provider harnesses |
| [baoyu-comic](https://www.skills.sh/jimliu/baoyu-skills/baoyu-comic) | creative skill | Style × tone × layout × aspect selection, educational/biography/tutorial modes, storyboard and prompt outputs, PDF merge | Strong content-to-comic skill grammar; choTaku should own the canon and provenance underneath |
| [agentara/skills](https://github.com/agentara/skills) | skills library | Video character design, video plans, storyboard boards, poster/key-art systems, visual continuity prompts | Reusable role/prompt patterns; not a storyworld compiler |
| [Comic Web Markup](https://github.com/abuseofnotation/comic-web-markup) | declarative layout | Text-based comic syntax rendered to SVG, layers, dialogue, moods, custom images | Strong artifact DSL idea; does not define upstream narrative truth |
| [AIComicBuilder](https://github.com/LingyiChen-AI/AIComicBuilder) | animated comics | Script → character design → storyboard → video synthesis | Relevant motion target; inspect actual implementation before depending on it |
| [Reveria](https://github.com/Dileep2896/reveria) | interactive storybook | Director chat, parallel agents, illustrated storybook, voice narration, flipbook, comics/manga/webtoons | Strong interaction model; needs explicit canon/branch/provenance contracts |
| [StoryCanvas](https://github.com/ydsgangge-ux/StoryCanvas) | visual story canvas | Multi-timeline narrative canvas, story cards, blocks, worldbuilding | Directly relevant authoring surface; requires source and rights discipline |
| [Open Design](https://github.com/nexu-io/open-design) | creative operating system | Local-first app, composable skills/plugins/templates/design systems, HTML/PDF/PPTX/MP4 export | Strong infrastructure pattern for creator tooling; broad design scope |
| [awesome-llm-story-generation](https://github.com/Picrew/awesome-llm-story-generation) | research index | Planning, agent collaboration, multimodal story generation, coherence, evaluation, refinement references | Discovery index; each listed project needs independent verification |

## Capability comparison

| System | Canon | Character memory | Graph/timeline | Layout control | Provider-neutral | Provenance/QC | Motion |
|---|---:|---:|---:|---:|---:|---:|---:|
| Storyboarder | low | low | low | high | high | medium | medium |
| Comic Template Maker | low | low | low | high | high | low | low |
| Agent Mangaka Forge | low | high | low | medium | medium | medium | low |
| Novel-to-Comic Studio | medium | high | medium | high | medium | high | low |
| Comic Book Movie Creator | low | high | low | medium | low | medium | high |
| ViMax | medium | medium | medium | medium | medium | medium | high |
| Bibliogon | medium | medium | medium | high | high | medium | low |
| baoyu-comic | low | medium | low | medium | medium | medium | low |
| Comic Web Markup | low | low | low | high | high | high at artifact layer | low |
| Chozen Land | high | high | high | conceptual | high | conceptual | high |
| choTaku | high | high | high | emerging | high | high | emerging |

## New architectural lessons

### 1. Image memory must become semantic identity memory

Agent Mangaka Forge's `img-memory` rule is valuable: recurring characters need approved references before generation.

choTaku should extend this to:

- character version
- outfit and prop state
- expression and pose references
- visual anchors
- location and environment references
- allowed evolution
- superseded references
- source and approval records

### 2. Page planning needs reader-state contracts

Novel-to-Comic Studio adds useful fields beyond “what happens”:

- what the reader already knows
- what is newly revealed
- what question remains open
- dialogue, captions, SFX
- non-omittable causality

These belong in choTaku's scene/page contract because they protect comprehension during compression.

### 3. Layout must be declarative

Comic Template Maker, Bibliogon, and Comic Web Markup point toward a layout DSL:

- named slots
- normalized geometry
- panel roles
- gutters and safe zones
- z-index
- text containers
- reading order
- export geometry

choTaku's visual layout contracts should evolve into a typed artifact layer instead of embedding placement only inside prompts.

### 4. Rights and provenance belong before generation

Novel-to-Comic Studio's rights gate is a strong pattern. A storyworld should declare:

- private experiment
- licensed commercial
- public domain
- original first-party
- unknown / review required

The system should block publication when rights state is unresolved.

### 5. Authoring views matter as much as generation

Storyboarder, Bibliogon, StoryCanvas, and Reveria collectively suggest synchronized surfaces:

- story graph
- timeline
- storyboard grid
- entity appearance filter
- page layout editor
- artifact preview
- review/checkpoint history

choTaku should make these projections of one semantic model, not separate data silos.

### 6. Motion should be a downstream target

ViMax and Comic Book Movie Creator show the value of script → storyboard → selected assets → motion → assembly. choTaku should compile motion from scene and shot truth, not ask a video provider to invent narrative structure.

## Patterns to adapt

- Approved character-reference gate
- Versioned character variants and evolutions
- Story-first page planning
- Reader-known/new/open-question fields
- Declarative layout contracts
- Drag/reorder storyboard projection
- Rights gate before derivative generation
- Render checkpoints and resumable stages
- Separate image, typography, finishing, and export passes
- Panel/shot sequence as an inspectable artifact
- Provider adapters behind semantic contracts

## Patterns to reject or constrain

- “Perfect consistency” marketing claims without evaluation fixtures
- Prompt-only canon
- Dense exact typography delegated entirely to image models
- Untracked generated assets
- Provider-specific story schemas that make migration expensive
- Silent overwrites of pages, references, or drafts
- End-to-end agents with no approval gates
- Publishing workflows with no rights or provenance state
- A single linear story list when the underlying narrative branches

## Search record

Search families included:

- `AI comic generator`
- `manga generator`
- `storyboard generator AI`
- `graphic novel creator`
- `visual story authoring`
- `comic book layout`
- `AI manga page generation character consistency`
- `open source graphic novel authoring`
- `comic web markup SVG`
- `comic-to-video`
- `story canvas worldbuilding`
- `skills.sh comic manga storyboard`

The search surfaced GitHub topic pages, first-party repositories, skills.sh, Hugging Face references, and adjacent product pages. Search results were treated as discovery leads; repository READMEs and source trees were preferred for architectural claims.

## Recommended choTaku additions

1. Add `IdentityMemory` and approved reference assets.
2. Add `ReaderState` to scene/page contracts.
3. Add typed `LayoutContract`, `Slot`, `SafeZone`, and `ReadingOrder`.
4. Add rights status to StoryWorld and artifact manifests.
5. Add `StoryboardProjection` and `PageLayoutProjection`.
6. Add resumable render checkpoints.
7. Add evaluation fixtures for character drift, reading order, layout overflow, and provenance loss.
8. Add a declarative Comic Web / SVG exporter.

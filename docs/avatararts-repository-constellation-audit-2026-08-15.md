# AvatarArts repository constellation audit

Date: 2026-08-15

## Executive finding

The current public AvatarArts repositories form a layered creative-automation ecosystem:

    Origin Story -> evidence and repository intelligence
                 -> choTaku -> storyworld, canon, graph, scene, and artifact planning
                 -> provider experiments -> image, comic, manga, and PDF generation
                 -> Evoked -> portable assets, memory, workflows, agents, and publishing surfaces
                 -> MCP / Obsidian / web interfaces

The repositories are not yet one integrated product. They are a portfolio of experiments, foundations, adaptations, and system shells. The main architectural opportunity is to define stable records and manifests so the projects can interoperate without collapsing into a single monolith.

## Evidence boundaries

Observed facts come from GitHub repository metadata, default branches, and public README files. A repository name, language badge, update time, or screenshot is not treated as proof of implementation depth. Private repositories are recorded only by visible metadata and are not inferred from.

The screenshots provide a useful portfolio snapshot: choTaku, origin-story, comics_generator, comic-cult, AvatarArts-Comic-Creator-Matrix, ComicBook-AI, evokedOS, Evoked-Dev-Vault, Evoked-plugin, obsidian-suno-library-studio, Claudian, my-fiverr, spirit-alley, sage, and my-mcp-creator. This is evidence of active ecosystem organization, not a substitute for source inspection.

## Repository roles

| Repository | Evidence-backed role | Maturity signal | Recommended boundary |
|---|---|---|---|
| choTaku | Provider-neutral storyworld compiler with typed models, graph, provenance, validation, schemas, and artifact planning | Structured kernel with docs, tests, examples, and contracts | Semantic source of truth |
| origin-story | Repository-intelligence skill for investigation, reverse engineering, evidence, security, and synthesis | Strong documentation and reusable research method | Research and comprehension layer |
| AvatarArts-Comic-Creator-Matrix | Capability matrix and orchestration blueprint for comic, manga, webtoon, graphic novel, storyboard, animation, and publishing | Documentation and architecture layer | Product taxonomy and agent/production map |
| comics_generator | Forked Python scenario-to-six-panel generator using an LLM, Stable Diffusion, Pillow, and text overlays | Working experimental reference; provider and layout assumptions are tightly coupled | Adapter reference, not core architecture |
| comic-cult | Forked JavaScript comic pipeline combining dialogue generation, image generation, composition, feature flags, PDF delivery, and email | Working historical/reference application; README contains inherited branding and deployment assumptions | UX and delivery patterns to extract |
| ComicBook-AI | Forked React/Vite, Firebase, Firestore, DALL-E comic creator with storage, search, PDF, sharing, and Cypress tests | Useful application reference with cloud-specific coupling | Optional web publishing surface |
| ai-comic-factory | First-party comic orchestration foundation referenced by the Matrix | Repository exists and is substantial enough to investigate separately | Candidate provider/orchestration source |
| Manga-Colorization-FJ | First-party manga colorization/enhancement foundation referenced by the Matrix | Repository exists and is comparatively large | Specialized visual transformation adapter |
| evokedOS | Portable local-first platform for assets, research, memory, agents, workflows, storyworlds, and publishing | Small but clearly specified Python/HTML foundation | Runtime and portable record layer |
| Evoked-Dev-Vault | Separate Obsidian development vault with zones for assets, research, agents, worlds, workflows, memory, dispatch, and exports | Small but highly useful operational structure | Test fixture, documentation, and integration workspace |
| Evoked-plugin | Private Obsidian plugin repository visible in the portfolio | Private; implementation not evaluated | Obsidian adapter surface |
| obsidian-suno-library-studio | Private TypeScript music-library studio | Private; implementation not evaluated | Music/media catalog adapter |
| Claudian | Forked/derived Obsidian agent interface with coding agents, skills, mentions, plans, MCP, sessions, and file operations | Mature external reference with a clear interaction model | Agent workbench pattern |
| my-mcp-creator | Bounded read-only ecosystem-intelligence MCP for allowed roots, project summaries, file reads, analysis, redaction, and safety policy | Strongest productized MCP concept in the visible set | Safe inspection and intelligence service |
| my-fiverr | Public planning workspace for Fiverr Seller OS | Documentation-only visible README | Commercial packaging and offer layer |
| spirit-alley | Private HTML project | Private and minimal metadata only | Do not infer implementation; potential storyworld/artifact source |
| sage | Public repository with no readable README content found in this pass | Empty or undocumented from current evidence | Needs identity, scope, and README before integration |

## What is already strategically strong

### 1. Separation of semantic and generative concerns

choTaku explicitly places canon, psychology, lore, evidence, graph structure, scene contracts, and provenance before generation. This is the strongest differentiator in the portfolio. The comic forks demonstrate generation pipelines, but they do not replace the semantic layer.

### 2. Research is becoming a system capability

Origin Story is more than project documentation. It is a repeatable method for turning unfamiliar repositories, tools, papers, and products into evidence-bounded design decisions. It should remain upstream of architecture decisions and downstream of verification.

### 3. Evoked supplies the portable operating surface

evokedOS defines records that can move between Python, browser, REST/local APIs, MCP, Obsidian, VS Code, HTML, JSON, Markdown, and publishing. This is the right location for asset intelligence, memory, workflow state, agent runs, and export packages.

### 4. The portfolio spans the full creative lifecycle

The set covers research, canon, image generation, comic assembly, colorization, asset cataloging, agent interaction, local workspaces, publication, and commercial packaging. The gap is not capability breadth; it is durable interoperability.

## Main architectural gaps

### Shared record format

choTaku and Evoked need a shared portable record envelope:

- record_id and record_type
- title and human-readable summary
- project/world/scene relationships
- source references and confidence
- status and review state
- content hash and version
- created/updated timestamps
- provenance and parent records
- permitted interfaces and export targets

### Generation manifest

Every image, panel, page, PDF, storyboard, or video should record:

- semantic source record
- scene and layout contract
- character/reference assets
- provider, model, workflow, seed, and parameters
- prompt and negative prompt
- parent asset and revision lineage
- content hash
- validation results
- human approval state

### Adapter contracts

The comic repositories currently encode provider and delivery choices inside application flows. Extract adapters for:

- narrative decomposition
- image generation
- image revision
- lettering
- panel composition
- page/PDF/CBZ export
- colorization
- email/social publishing

### Public/private boundaries

Private projects should be represented in public documentation through capability descriptions, not leaked implementation details. Public repos should clearly label whether they are:

- production candidates
- historical forks
- experimental references
- documentation/specification repositories
- private adapters
- archived concepts

### Fork hygiene

The three visible comic applications are valuable references, but their upstream README text, branding, deployment links, inherited secrets/examples, and provider assumptions need an adaptation record before public productization. Keep upstream attribution and license boundaries explicit.

## Recommended canonical architecture

    origin-story
      research dossier, source ledger, comparative analysis
                |
                v
    choTaku
      canon, psychology, lore, graph, scenes, layout contracts
                |
                +--> InvokeAI / image providers
                +--> comic and manga renderers
                +--> colorization and enhancement
                +--> lettering and page composition
                |
                v
    Evoked records
      assets, memory, agent runs, workflows, approvals, exports
                |
                +--> MCP
                +--> Obsidian
                +--> browser workbench
                +--> portfolio / marketplace / publishing

## Priority sequence

1. Add a shared record-envelope specification to choTaku and Evoked.
2. Create importers that convert comic-generator outputs into artifact manifests.
3. Add a generation-manifest adapter for InvokeAI and other providers.
4. Connect my-mcp-creator’s bounded inspection model to read-only choTaku and Evoked tools.
5. Use Evoked-Dev-Vault as the integration test fixture.
6. Normalize the Matrix’s repository links, capabilities, and maturity classifications.
7. Add README identity pages to sage and any repository that is intentionally public but currently undocumented.
8. Keep private repositories out of public implementation claims while documenting their intended adapter role.

## Final assessment

AvatarArts already has the ingredients of a creative operating system:

- Origin Story understands systems.
- choTaku understands storyworld semantics.
- the Matrix understands production surfaces.
- provider projects understand generation and assembly.
- Evoked understands portable creative state.
- my-mcp-creator understands bounded tool access.
- Claudian and the Obsidian projects demonstrate agent-facing interaction.

The next leap is integration discipline: shared records, manifests, adapters, review gates, and evidence-linked exports. More generators are secondary until the ecosystem can remember what was created, why it was created, which source and canon it came from, and whether it is safe to publish.

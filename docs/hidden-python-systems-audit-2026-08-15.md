# Hidden Python systems audit

Date: 2026-08-15

## Finding

A filename-level recursive scan of the AvatarArts GitHub account confirms that the visible repository list significantly understates the actual system portfolio. The largest repositories contain dense Python archives, operational scripts, provider adapters, media tools, research utilities, and agent infrastructure.

This is an inventory and architectural triage, not a claim that every file is production-ready. Counts include tests, duplicates, vendored/reference material, backups, and legacy generations.

## Python inventory snapshot

| Repository | Python files found | Interpretation |
|---|---:|---|
| AVATARARTS | 2,956 | Large historical and active workspace archive spanning business, media, cataloging, SEO, automation, websites, and client systems |
| pythons | 4,138 | Broad personal automation laboratory with content intelligence, media processing, music, transcriptions, uploads, catalogs, and unified tools |
| PYTHON_MARKETPLACE_MASTER | 5,882 | Product and commercialization archive with AI agents, media, SEO, voice, prompt libraries, audio, and finished-product variants |
| ToolUniverse | 1,236 | Tool/agent ecosystem with MCP integration, registries, memory, examples, and scientific workflows |
| FastChat | 124 | Model serving, conversation, evaluation, and provider infrastructure |
| gorilla | 211 | Function-calling benchmarks, agentic evaluation, model handlers, and tool-use tests |
| notebooklm-mine | 174 | NotebookLM client, research workflows, CLI, artifacts, sources, sessions, and tests |
| agent-skills | 114 | Skill tooling, creative adapters, structured asset pipeline, ComfyUI, provider integrations, and verification |
| .Agent-skills | 94 | Parallel/derived skill collection with creative, productivity, and pipeline implementations |
| AutoTagger | 106 | Multiple generations of intelligent indexing, tagging, capture, organization, and knowledge storage |
| open-design | 74 | Design automation, image generation, pet identity, animation, and layout verification |
| lama | 98 | Image inpainting, segmentation, datasets, training, and evaluation |
| STTN | 10 | Video object removal and inpainting research implementation |

## Most important hidden capabilities

### Content-aware ecosystem intelligence

Representative files:

- https://github.com/AvaTar-ArTs/pythons/blob/main/content_organizer_agent.py
- https://github.com/AvaTar-ArTs/AVATARARTS/blob/main/00_ACTIVE/DEVELOPMENT/UTILITIES_TOOLS/cataloging/CONTENT_AWARE_CATALOG/create_content_aware_organization.py
- https://github.com/AvaTar-ArTs/pythons/blob/main/ADVANCED_CONTENT_AWARE_ANALYZER.py
- https://github.com/AvaTar-ArTs/AutoTagger/tree/main/current
- https://github.com/AvaTar-ArTs/AutoTagger/tree/main/v5-workspace/scripts

These systems scan files, inspect content, classify and tag, score strategic value, build category/tag views, and export organization reports. This is a candidate first-party Asset Intelligence layer for Evoked and choTaku.

### Structured creative asset pipeline

The structured asset pipeline in agent-skills contains adapters for OpenAI Images, Replicate, fal, ComfyUI, ElevenLabs, and Suno, plus YAML unit specifications, absolute-path enforcement, secret detection, overwrite refusal, non-empty verification, stable JSON results, dry-run mode, and report generation.

Most relevant files:

- https://github.com/AvaTar-ArTs/agent-skills/blob/main/skills/creative/structured-asset-pipeline/scripts/pipeline_dry_run.py
- https://github.com/AvaTar-ArTs/agent-skills/blob/main/skills/creative/structured-asset-pipeline/scripts/adapters/comfyui.py
- https://github.com/AvaTar-ArTs/agent-skills/tree/main/skills/creative/structured-asset-pipeline

This is closer to a reusable production substrate than the simple prompt-to-image applications. Adapt it through a manifest contract rather than copying it wholesale.

### MCP registry and loading

ToolUniverse contains remote MCP tool discovery, tool-prefixing, selected-tool loading, auto-registration, server URL management, decorators, and schemas.

- https://github.com/AvaTar-ArTs/ToolUniverse/blob/main/src/tooluniverse/mcp_integration.py
- https://github.com/AvaTar-ArTs/ToolUniverse/blob/main/src/tooluniverse/mcp_tool_registry.py
- https://github.com/AvaTar-ArTs/ToolUniverse/blob/main/src/tooluniverse/mcp_client_tool.py

Use this as a transport and registry reference. Keep semantic authority, validation, provenance, and approval gates in choTaku and Evoked.

### Multi-agent session memory

ToolUniverse memory_manager.py contains session IDs, user/session names, phases, prior results, execution history, recent agent context projection, expiration, cleanup, and thread locking. This is a direct bridge to Evoked memory records and choTaku agent-run provenance.

- https://github.com/AvaTar-ArTs/ToolUniverse/blob/main/src/tooluniverse/memory_manager.py

### Music-to-visual-story pipeline

music_tools_lyrics-storyboards.py transcribes audio, analyzes themes, emotions, objects, characters, lighting, color, and visual transitions, then prepares narrative-driven image-generation guidance.

- https://github.com/AvaTar-ArTs/pythons/blob/main/MEDIA_PROCESSING/audio/music_tools_lyrics-storyboards.py

This directly connects to the lyric-driven comic and storyboard work developed in conversation. The sampled file also has reliability debt: duplicated environment loading and malformed indentation, so it is a concept/reference until repaired and tested.

### Unified providers and automation

unified_ai_manager.py attempts a provider-neutral OpenAI, Anthropic, and Groq abstraction. universal_automation_hub.py provides scheduled tasks, dependencies, API clients, data processing, media/AI categories, concurrency, logging, and progress state.

- https://github.com/AvaTar-ArTs/pythons/blob/main/unified_ai_manager.py
- https://github.com/AvaTar-ArTs/pythons/blob/main/universal_automation_hub.py

These are ancestors of Evoked Alchemy and should be normalized into typed provider capabilities, task records, execution events, retries, and approval policies.

### Visual identity and transformation

Additional high-value foundations include:

- https://github.com/AvaTar-ArTs/lama — image inpainting, masks, datasets, and evaluation
- https://github.com/AvaTar-ArTs/STTN — video inpainting and object removal
- https://github.com/AvaTar-ArTs/AVATARARTS/blob/main/00_ACTIVE/BUSINESS/quantumforge-complete/quantum_media_processor.py — experimental DCT/block image transformation
- https://github.com/AvaTar-ArTs/open-design/tree/main/skills/hatch-pet/scripts — canonical identity references, generation manifests, hashes, repair queues, atlas validation, and animation rendering

The hatch-pet workflow is particularly relevant to visual identity stabilization because it tracks canonical base art, generated states, provenance, and validation.

## Architectural synthesis

Origin Story provides repository comprehension and evidence. AVATARARTS, pythons, and PYTHON_MARKETPLACE_MASTER provide automation and media infrastructure. Asset Intelligence organizes the ecosystem. Evoked provides portable records and memory. choTaku provides canon, storyworlds, graphs, layouts, and artifact plans. The structured asset pipeline provides verified provider execution. MCP, Obsidian, web, and publishing become controlled surfaces.

## Immediate extraction priorities

1. Extract the structured-asset-pipeline contract into a shared specification.
2. Build a repository and Python capability index for the entire AvatarArts account.
3. Consolidate content-aware organization and AutoTagger generations into one tested Asset Intelligence package.
4. Port multi-agent session memory into durable Evoked records.
5. Turn music-to-visual analysis into a typed choTaku multimodal scene input.
6. Normalize the provider abstraction with model and provider provenance.
7. Produce a deduplication and lineage report for repeated scripts across the large archives.
8. Repair or quarantine scripts with hard-coded paths, implicit credentials, malformed imports, missing typing imports, or destructive filesystem behavior.
9. Add capability metadata to high-value scripts: purpose, inputs, outputs, dependencies, safety class, maturity, and destination system.

## Final assessment

The account contains a hidden creative-automation infrastructure layer far beyond the visible comic repositories. The most valuable discoveries are reusable subsystems: content-aware asset intelligence, structured multimodal generation, provider adapters, MCP registries, multi-agent memory, visual identity tracking, music-to-storyboard transformation, and commercialization tooling.

These are the next research-to-implementation bridge between Origin Story, choTaku, Evoked, and the broader AvatarArts production ecosystem.
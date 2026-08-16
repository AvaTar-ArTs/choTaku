# First-party InvokeAI audit

Date: 2026-08-15

## Finding

AvaTar-ArTs/InvokeAI is a public first-party fork of invoke-ai/InvokeAI. It is Apache-2.0 licensed and retains the upstream project’s full creative-engine scope. The repository should be treated as a visual-generation substrate, not as the semantic source of truth for AvatarArts canon.

This audit is based on repository metadata, the fork README, package configuration, image API routes, and representative Flux backend code. It does not assume that the fork contains unpublished AvatarArts modifications unless a diff proves them.

## What it contributes

InvokeAI supplies the lower visual layer:

- local web application and React interface
- Unified Canvas for generation, inpainting, outpainting, and brush-based work
- workflow and node execution
- boards, galleries, image metadata, prompt recall, and model management
- support for multiple diffusion and image backends
- upscaling, embeddings, segmentation, ControlNet, IP Adapter, LoRA, and regional prompting
- a substantial Python service, API, storage, and test surface

These capabilities directly support choTaku’s visual artifact pipeline and the layout-stabilization work documented in the visual layout research.

## What it does not own

InvokeAI should not become the authority for:

- character identity, goals, fears, wounds, or relationships
- canon, continuity, provenance, or rights decisions
- scene contracts, story beats, or typed narrative graphs
- publication manifests, page order, captions, dialogue, or reader-facing accessibility
- the decision that an image is canonically accepted

Those belong to choTaku, origin-story, or the eventual AvatarArts Forge orchestration layer.

## Proposed boundary

    storyworld -> scene contract -> visual layout contract
              -> InvokeAI adapter -> workflow/canvas generation
              -> asset + metadata manifest -> validation -> canon candidate

The adapter must be one-way with respect to canon: choTaku may request an image and record the result, but InvokeAI output must not mutate canon without an explicit validation and approval step.

## Adapter input

An InvokeAI request should include:

- scene_id and artifact_id
- layout_id, aspect ratio, dimensions, safe areas, and panel placement constraints
- approved character and location references
- positive and negative prompts
- model, workflow, LoRA, ControlNet, IP Adapter, and VAE selections
- seed policy and identity anchors
- generation mode: text-to-image, image-to-image, inpaint, outpaint, upscale, or revision

## Adapter output

The returned manifest should preserve:

- generated asset path and content hash
- provider and model identifiers
- workflow identifier and workflow hash
- seed and sampler settings
- attached LoRAs, ControlNets, IP Adapters, and reference hashes
- source asset and parent-asset relationships
- prompt and negative-prompt snapshots
- layout-contract result and validation status
- human approval or rejection status

## Architectural recommendation

Keep InvokeAI as an optional provider behind a stable choTaku interface. Do not fork or rewrite the upstream engine to embed narrative logic. First build a thin adapter that can submit a deterministic request, collect metadata, and return an immutable artifact record. Add workflow templates for character sheet, panel image, page composite, cover, and revision passes only after the contract is stable.

## Risks and controls

The fork carries upstream dependency, GPU, model-license, and maintenance risk. Pin provider versions, record model licenses, isolate credentials, use explicit workspace roots, and preserve every generation manifest. Treat model outputs as candidates until continuity, identity, layout, and rights checks pass.

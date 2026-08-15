# Research → implementation map

This document records how the accumulated research becomes choTaku design, without treating any external project as a dependency or template.

## Primary conceptual inputs

| Research area | Reusable insight | choTaku boundary |
|---|---|---|
| Origin Story | inspect intent, implementation, sources, gaps, and provenance | research and comprehension remain explicit inputs |
| Chozen Land | context, meaning, canon, graph, narrative, artifact progression | semantic backbone and future graph interchange |
| Visual Story-Writing | entity, spatial, timeline, and action views with bidirectional editing | future authoring projections over the same storyworld |
| Worldbuilding systems | structured lore, relationships, rules, and state | typed canon records and evidence |
| Agentic planning | preserve decisions, rejected paths, commitments, and progress | agent manifests and future decision ledger |
| Comic/manga generators | scene decomposition, continuity anchors, page/panel production | provider-neutral scene contracts |
| Media pipelines | separate generation, composition, enhancement, and publishing | adapters downstream of the compiler |
| Asset intelligence | hashes, metadata, manifests, lineage, and reproducibility | provenance fields and future asset registry |

## What choTaku owns

- The meaning of the story
- Canon and disputed canon
- Character psychology and causal motivation
- Event, evidence, and progression state
- Scene contracts and continuity requirements
- Target-specific artifact plans
- Provenance and quality-gate declarations

## What choTaku delegates

- Language, image, audio, and video model execution
- ControlNet/ComfyUI-style rendering graphs
- Layout and lettering applications
- Storage, search, and catalog databases
- Publishing destinations
- UI surfaces and MCP transport

## Gap-bridging strategy

Steven's demonstrated capability is the bridge between these layers: creative automation, Python systems, AI workflow architecture, multimodal asset pipelines, research synthesis, agent/MCP design, visual storytelling, and creator-tool infrastructure. choTaku converts that breadth into stable contracts so each capability can become a replaceable adapter instead of a disconnected experiment.

## Quality gates

Every future adapter should answer:

1. Which storyworld and version produced this output?
2. Which scene contract did it satisfy?
3. Which sources and decisions shaped it?
4. Which provider, model, prompt, seed, and transformation steps were used?
5. Which continuity checks passed or failed?
6. Can the artifact be regenerated or audited?

## Roadmap

- **0.1 kernel:** models, compiler, validation, schema, manifests, CI
- **0.2 graph:** typed edges, timelines, relationships, state transitions
- **0.3 adapters:** image, text, audio, video, layout, lettering, publishing
- **0.4 authoring:** synchronized entity/spatial/timeline/action views
- **0.5 MCP:** inspect, compile, validate, render, manifest, compare
- **0.6 studio:** web UI, asset catalog, review, release management

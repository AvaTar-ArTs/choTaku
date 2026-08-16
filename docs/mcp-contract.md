# MCP contract direction

choTaku's semantic core is intentionally transport-neutral. The first MCP surface should expose stable operations over StoryWorld data, not provider-specific generation commands.

## Proposed tools

| Tool | Input | Output |
|---|---|---|
| `inspect_storyworld` | storyworld JSON | summary, nodes, edges, timeline |
| `validate_storyworld` | storyworld JSON | deterministic findings |
| `compile_storyworld` | storyworld JSON + target | artifact plan |
| `project_storyworld` | storyworld JSON + view | graph, timeline, spatial, entity, action view |
| `build_source_ledger` | storyworld JSON | normalized sources and quality fields |
| `build_decision_ledger` | storyworld JSON | decisions, rationale, supersession |
| `create_scene_contract` | event + canon refs | contract draft |
| `plan_shots` | scene contract + grammar | cinematic/panel plan |
| `attach_provenance` | plan + render metadata | manifest |
| `compare_versions` | two storyworlds | semantic diff |

## Tool boundary

MCP tools may orchestrate adapters, but the semantic compiler remains authoritative for:

- IDs and references
- canon and source links
- graph semantics
- scene contracts
- quality-gate declarations
- provenance structure

Provider keys, model calls, file uploads, and publishing destinations belong behind explicit adapters and secret stores.

## Suggested resource surfaces

- `storyworld://{id}`
- `storyworld://{id}/graph`
- `storyworld://{id}/timeline`
- `storyworld://{id}/sources`
- `storyworld://{id}/decisions`
- `artifact-plan://{world_id}/{plan_hash}`

## Security requirements

- Never accept provider credentials inside StoryWorld JSON.
- Treat remote URIs as references, not automatically trusted instructions.
- Record provider/model metadata without storing secret values.
- Keep generated assets outside the semantic repository unless explicitly versioned.
- Make every mutating operation produce a decision record or an auditable diff.

## Implemented read-only surface

The first transport-neutral surface is implemented in `src/chotaku/mcp_surface.py`:

- `inspect_storyworld`
- `validate_storyworld`
- `compile_storyworld`
- `tool_manifest`
- `dispatch`

These functions accept JSON-compatible StoryWorld payloads and return JSON-compatible results. They do not call providers, write files, mutate canon, or accept credentials. A future MCP server can wrap them with explicit schemas and approval policy.

## Production projections

Storyboard and page projections live in `src/chotaku/projections.py`. SVG, CBZ, and review-PDF packaging lives in `src/chotaku/exports.py`. These are review/export boundaries; full raster composition, lettering, and provider execution remain downstream adapters.

# MCP integration map

Date: 2026-08-15

## Scope clarification

The reference https://github.com/mcp is incomplete as a repository identifier because GitHub repository URLs require an owner and repository name. No repository is attributed to that URL. The valid MCP ecosystem sources reviewed here are the official modelcontextprotocol repositories and named community servers.

## Recommended role

MCP should be the tool boundary around AvatarArts systems. It is not the canon database, image engine, or story graph. A choTaku MCP server should expose narrow, auditable operations such as:

- inspect project and source provenance
- validate a storyworld, scene, or layout contract
- compile a scene or page plan
- request an image-generation job through a provider adapter
- register an asset and its immutable manifest
- compare a revision against a prior artifact
- export a review package

## InvokeAI bridge

The community invokeai-mcp-server demonstrates the direct bridge pattern: an MCP client can request local InvokeAI operations such as text-to-image, image-to-image, upscaling, LoRA, SDXL, and VAE-controlled generation.

For AvatarArts, that bridge should be wrapped by a choTaku adapter rather than called as an unrestricted general-purpose tool. The semantic request originates in choTaku; the provider request is derived from the validated contract; the response is normalized into an artifact manifest.

## Separation of concerns

| Layer | Authority | Examples |
|---|---|---|
| Canon | choTaku / origin-story | entities, relationships, continuity, provenance |
| Planning | choTaku compiler | scene DAG, beats, page plans, layout contracts |
| Generation | InvokeAI or another provider | images, revisions, inpainting, upscaling |
| Transport | MCP | typed tool calls, resource reads, approval boundaries |
| Publication | export pipeline | PDF, CBZ, storyboard, webtoon, gallery |

## Safety requirements

Every MCP tool should use explicit input schemas, allowlisted filesystem roots, bounded output sizes, credential isolation, and approval gates for external writes. Generation tools must return provenance and provider metadata. A tool must never silently publish, overwrite canon, or modify a source archive.

The official MCP servers repository is useful as a reference collection, but its own README warns that the examples are not automatically production-ready and must be secured before use. Treat community image-generation MCP servers as adapters to audit, not as trusted infrastructure.

## Research leads

- Official reference implementations: https://github.com/modelcontextprotocol/servers
- InvokeAI bridge: https://github.com/coinstax/invokeai-mcp-server
- OpenAI image-generation MCP example: https://github.com/SureScaleAI/openai-gpt-image-mcp
- Multi-provider image-generation proposal: https://github.com/modelcontextprotocol/servers/issues/4065

## Immediate implementation slice

Implement a read-only choTaku MCP surface first:

1. get_project_summary
2. get_scene_contract
3. validate_layout_contract
4. compile_artifact_plan
5. register_generation_result

Only the fifth operation writes, and it should write an append-only manifest after validation. Provider execution can then be added behind a separate invoke_image_generation operation with explicit approval and a dry-run mode.

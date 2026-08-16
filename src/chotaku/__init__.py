"""choTaku: a semantic storyworld compiler."""

from .compiler import compile_storyworld
from .graph import graph_summary, timeline_view
from .models import StoryWorld
from .provenance import decision_ledger, manifest, source_ledger
from .exports import export_cbz, export_review_pdf, export_svg_page
from .mcp_surface import inspect_storyworld, validate_storyworld_payload
from .projections import page_projection, storyboard_projection
from .production import (
    BalloonStyle,
    CellDefinition,
    IdentityMemory,
    LayoutContract,
    LayoutSlot,
    LayoutStyle,
    PromptManifest,
    ReaderState,
    RenderCheckpoint,
    RightsRecord,
    SfxDefinition,
    TextRegionDefinition,
    TypographyStyle,
)
from .validation import Finding, validate_storyworld

__all__ = [
    "Finding",
    "StoryWorld",
    "BalloonStyle",
    "CellDefinition",
    "IdentityMemory",
    "LayoutContract",
    "LayoutSlot",
    "LayoutStyle",
    "PromptManifest",
    "ReaderState",
    "RenderCheckpoint",
    "RightsRecord",
    "SfxDefinition",
    "TextRegionDefinition",
    "TypographyStyle",
    "compile_storyworld",
    "decision_ledger",
    "graph_summary",
    "manifest",
    "source_ledger",
    "timeline_view",
    "validate_storyworld",
    "export_cbz",
    "export_review_pdf",
    "export_svg_page",
    "inspect_storyworld",
    "validate_storyworld_payload",
    "page_projection",
    "storyboard_projection",
]
__version__ = "0.2.0"

import json
from pathlib import Path
from zipfile import ZipFile

from chotaku.exports import export_cbz, export_review_pdf, export_svg_page
from chotaku.mcp_surface import inspect_storyworld, validate_storyworld_payload
from chotaku.models import LayoutContract, LayoutSlot
from chotaku.projections import page_projection, storyboard_projection


def load_payload():
    return json.loads((Path(__file__).parents[1] / "examples" / "crimson-curse-master.json").read_text())


def test_storyboard_projection_creates_rows():
    projection = storyboard_projection({"target": "comic", "world": {"id": "w"}, "scenes": [{"id": "s", "purpose": "turn", "emotional_turn": "dread", "visual_motif": "sigil"}]})
    assert projection["count"] == 1
    assert projection["rows"][0]["scene_id"] == "s"


def test_page_projection_binds_slots():
    plan = {"target": "comic", "scenes": [{"id": "s", "shots": [{"id": "shot-1", "action": "look"}]}]}
    contract = LayoutContract("page", slots=[LayoutSlot("p1", "hero", 0, 0, 100, 100)])
    page = page_projection(plan, contract, asset_ids={"shot-1": "asset-1"})
    assert page["bindings"][0]["asset_id"] == "asset-1"


def test_exports_svg_pdf_and_cbz(tmp_path):
    contract = LayoutContract("page", width=100, height=100, slots=[LayoutSlot("p1", "hero", 0, 0, 100, 100)])
    svg = export_svg_page(contract, tmp_path / "001.svg")
    pdf = export_review_pdf(contract, tmp_path / "review.pdf")
    cbz = export_cbz([svg], tmp_path / "book.cbz")
    assert svg.exists() and svg.read_text().startswith("<svg")
    assert pdf.read_bytes().startswith(b"%PDF")
    with ZipFile(cbz) as archive:
        assert archive.namelist() == ["001-001.svg"]


def test_mcp_surface_is_read_only_and_validates():
    result = inspect_storyworld(load_payload())
    assert result["counts"]["characters"] == 1
    validation = validate_storyworld_payload(load_payload())
    assert validation["valid"]

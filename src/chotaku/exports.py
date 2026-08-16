"""Dependency-light review and comic package exporters."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path

from .production import LayoutContract, layout_to_svg


def export_svg_page(contract: LayoutContract, output: str | Path, *, title: str = "choTaku page") -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(layout_to_svg(contract, title=title), encoding="utf-8")
    return path


def export_cbz(pages: list[str | Path], output: str | Path) -> Path:
    """Package rendered page files into a deterministic CBZ archive."""
    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted((Path(page) for page in pages), key=lambda item: item.name)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for index, page in enumerate(ordered, start=1):
            archive.write(page, f"{index:03d}-{page.name}")
    return destination


def export_review_pdf(contract: LayoutContract, output: str | Path, *, title: str = "choTaku review") -> Path:
    """Write a minimal text-based PDF review artifact.

    This is intentionally a review proof, not a raster compositor. Provider
    adapters can replace it with a full image/PDF renderer later.
    """
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [title, f"layout: {contract.id}", f"size: {contract.width}x{contract.height}"]
    lines.extend(f"{index}. {slot.label or slot.role} [{slot.x},{slot.y},{slot.width},{slot.height}]" for index, slot in enumerate(contract.slots, 1))
    stream_text = "BT /F1 12 Tf 50 760 Td " + " ".join(f"({re.sub(r'[^ -~]', '', line)}) Tj 0 -18 Td" for line in lines) + " ET"
    objects = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        f"<< /Length {len(stream_text.encode())} >>\nstream\n{stream_text}\nendstream",
    ]
    chunks = ["%PDF-1.4\n"]
    offsets = [0]
    for number, obj in enumerate(objects, 1):
        offsets.append(sum(len(chunk.encode()) for chunk in chunks))
        chunks.append(f"{number} 0 obj\n{obj}\nendobj\n")
    xref = sum(len(chunk.encode()) for chunk in chunks)
    chunks.append(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n")
    chunks.extend(f"{offset:010d} 00000 n \n" for offset in offsets[1:])
    chunks.append(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n")
    path.write_bytes("".join(chunks).encode())
    return path

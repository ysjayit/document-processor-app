"""Reusable PDF operations shared by the CLI scripts and the web UI."""
from io import BytesIO

from pypdf import PdfReader, PdfWriter


def merge_pdfs(files):
    """Merge PDFs in the given order. `files` are paths or file-like objects."""
    writer = PdfWriter()
    for f in files:
        writer.append(f)
    out = BytesIO()
    writer.write(out)
    writer.close()
    out.seek(0)
    return out


def change_title(file, new_title):
    """Return a copy of the PDF with a new /Title, keeping other metadata."""
    reader = PdfReader(file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    metadata = reader.metadata or {}
    writer.add_metadata({
        "/Title": new_title,
        "/Author": metadata.get("/Author", ""),
        "/Subject": metadata.get("/Subject", ""),
        "/Creator": metadata.get("/Creator", ""),
        "/Producer": metadata.get("/Producer", ""),
    })

    out = BytesIO()
    writer.write(out)
    out.seek(0)
    return out

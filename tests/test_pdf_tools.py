import io
import os
import sys

import pytest
from pypdf import PdfReader, PdfWriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from pdf_tools import change_title, merge_pdfs  # noqa: E402
from web import app  # noqa: E402


def blank_pdf(width):
    """A one-page PDF whose page width identifies it."""
    w = PdfWriter()
    w.add_blank_page(width=width, height=100)
    buf = io.BytesIO()
    w.write(buf)
    buf.seek(0)
    return buf


def widths(pdf_bytes):
    return [float(p.mediabox.width) for p in PdfReader(pdf_bytes).pages]


def test_merge_respects_order():
    out = merge_pdfs([blank_pdf(300), blank_pdf(100), blank_pdf(200)])
    assert widths(out) == [300, 100, 200]


def test_merge_sample_assets_page_count():
    paths = [os.path.join(ROOT, "assets", f"0{i}-sample-document.pdf") for i in (1, 2, 3)]
    expected = sum(len(PdfReader(p).pages) for p in paths)
    assert len(PdfReader(merge_pdfs(paths)).pages) == expected


def test_change_title():
    out = change_title(blank_pdf(100), "Hello")
    assert PdfReader(out).metadata.title == "Hello"


@pytest.fixture
def client():
    return app.test_client()


def test_web_merge_order_and_validation(client):
    ok = client.post("/merge", data={
        "files": [(blank_pdf(300), "a.pdf"), (blank_pdf(100), "b.pdf")]
    }, content_type="multipart/form-data")
    assert ok.status_code == 200
    assert widths(io.BytesIO(ok.data)) == [300, 100]

    one = client.post("/merge", data={"files": [(blank_pdf(100), "a.pdf")]},
                      content_type="multipart/form-data")
    assert one.status_code == 400

    bad = client.post("/merge", data={
        "files": [(io.BytesIO(b"x"), "a.txt"), (io.BytesIO(b"y"), "b.txt")]
    }, content_type="multipart/form-data")
    assert bad.status_code == 400

    corrupt = client.post("/merge", data={
        "files": [(io.BytesIO(b"nope"), "a.pdf"), (io.BytesIO(b"nope"), "b.pdf")]
    }, content_type="multipart/form-data")
    assert corrupt.status_code == 400


def test_web_title(client):
    ok = client.post("/title", data={"file": (blank_pdf(100), "a.pdf"), "title": "T"},
                     content_type="multipart/form-data")
    assert ok.status_code == 200
    assert PdfReader(io.BytesIO(ok.data)).metadata.title == "T"

    empty = client.post("/title", data={"file": (blank_pdf(100), "a.pdf"), "title": " "},
                        content_type="multipart/form-data")
    assert empty.status_code == 400

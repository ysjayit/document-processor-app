import threading
import webbrowser

from flask import Flask, jsonify, render_template, request, send_file
from pypdf.errors import PyPdfError

from pdf_tools import change_title, merge_pdfs

HOST, PORT = "127.0.0.1", 5000

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024  # 25 MB


def _is_pdf(storage):
    return bool(storage.filename) and storage.filename.lower().endswith(".pdf")


def _error(message, status=400):
    return jsonify(error=message), status


@app.errorhandler(413)
def too_large(_):
    return _error("Upload too large (25 MB max).", 413)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/merge")
def merge():
    # Files arrive in the order the UI appended them (the user's chosen order).
    files = request.files.getlist("files")
    if len(files) < 2:
        return _error("Select at least 2 PDF files to merge.")
    if not all(_is_pdf(f) for f in files):
        return _error("Only .pdf files are allowed.")
    try:
        result = merge_pdfs([f.stream for f in files])
    except (PyPdfError, ValueError, OSError):
        return _error("One of the files is not a valid PDF.")
    return send_file(result, mimetype="application/pdf",
                     as_attachment=True, download_name="merged.pdf")


@app.post("/title")
def title():
    file = request.files.get("file")
    new_title = request.form.get("title", "").strip()
    if file is None or not _is_pdf(file):
        return _error("Select a .pdf file.")
    if not new_title:
        return _error("Enter a title.")
    try:
        result = change_title(file.stream, new_title)
    except (PyPdfError, ValueError, OSError):
        return _error("The file is not a valid PDF.")
    return send_file(result, mimetype="application/pdf",
                     as_attachment=True, download_name=file.filename)


if __name__ == "__main__":
    threading.Timer(1.0, lambda: webbrowser.open(f"http://{HOST}:{PORT}")).start()
    app.run(host=HOST, port=PORT, debug=False)

# Document Processor

**Document Processor** is a simple Python application designed to handle basic document processing tasks. Currently, it supports merging PDF files, with plans to incorporate additional features in the future.

## Features

- **PDF Merging**: Combine multiple PDF files into a single PDF document, with an easy way to reorder them (web UI).
- **Change PDF Title**: Update a PDF's title while keeping its other metadata.

## Quick Start (Web UI)

You only need Python 3 installed. One step sets everything up and opens the app in your browser at `http://127.0.0.1:5000`:

- Linux / Mac:
```shell
./run.sh
```
- Windows: double-click `run.bat` (or run it from a terminal).

In the **Merge PDFs** section, add your files, then drag them (⠿) or use the ↑ / ↓ buttons to set the order. Click **Merge & download**. Use **Change PDF title** to update a PDF's title.

Files are processed in memory and are never stored on the server. The app listens on localhost only.

## Requirements

- Python 3.9 or higher
- `pypdf` for PDF manipulation and `Flask` for the web UI (both installed by `requirements.txt`)

## Installation

1. **Clone the Repository**:
```shell
git clone https://github.com/ysjayit/document-processor-app.git
cd document-processor-app
```
2. **Create and Activate a Virtual Environment (optional but recommended)**:
If virtualenv is not installed yet, you can install it via pip:
```shell
pip install virtualenv
```
Create the environment (creates a folder in your current directory)
```shell
virtualenv [ENVIRONMENT NAME] -> Ex: virtualenv venv
```
Activate the virtual environment:
- In Linux or Mac, activate the new python environment
```shell
source [ENVIRONMENT NAME]/bin/activate
```
- In Windows
```shell
.\[ENVIRONMENT NAME]\Scripts\activate
```
3. **Install Dependencies**:
```shell
pip install -r requirements.txt
```

## Usage (command line)
`pdf_tools.py` holds the shared logic. The scripts below are optional CLI wrappers; edit the constants at the top of each file.

To change a PDF's title, set `input_pdf`, `output_pdf` and `new_title` in `change_pdf_title.py`, then run `python change_pdf_title.py`.

To merge:
1. Insert the pdf files in to assets directory in project
2. **Update the `documents` List**:
   - Open the `app.py` file.
   - Locate the `documents` list in the script.
   - Update this list with the filenames of the PDF documents you want to merge. Ensure the filenames match exactly and include the file extension (e.g., `file1.pdf`, `file2.pdf`).
3. To merge PDF files, run the `app.py` script as follows:
```shell
python app.py
```
4. The script will merge the specified PDF files and save the merged document in the `assets/outputs` directory

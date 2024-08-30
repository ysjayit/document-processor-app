# Document Processor

**Document Processor** is a simple Python application designed to handle basic document processing tasks. Currently, it supports merging PDF files, with plans to incorporate additional features in the future.

## Features

- **PDF Merging**: Combine multiple PDF files into a single PDF document.

## Requirements

- Python 3.6 or higher
- `PyPDF2` library for PDF manipulation

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

## Usage
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

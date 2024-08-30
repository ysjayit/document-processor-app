from pypdf import PdfWriter
from datetime import datetime
import os

documents = [
    '01-sample-document.pdf',
    '02-sample-document.pdf',
    '03-sample-document.pdf',
]

assets_dir = 'assets/'
output_dir = 'assets/outputs/'

merger = PdfWriter()

def merge_pdfs(documents, assets_dir, output_dir):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Append each PDF to the merger object
    for pdf in documents:
        pdf_path = os.path.join(assets_dir, pdf)
        if os.path.isfile(pdf_path):
            merger.append(pdf_path)
            print(f"Added: {pdf_path}")
        else:
            print(f"Warning: {pdf_path} does not exist and will be skipped.")

    # Generate the output filename with a timestamp
    now = datetime.now()
    timestamp_str = now.strftime('%Y%m%d_%H%M%S')
    output_filename = f"merged-file-{timestamp_str}.pdf"
    output_path = os.path.join(output_dir, output_filename)

    # Write the merged PDF to the output directory
    merger.write(output_path)
    merger.close()
    print(f"PDFs merged successfully into: {output_path}")

# Run the PDF merging function
merge_pdfs(documents, assets_dir, output_dir)

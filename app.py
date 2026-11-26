import os
from datetime import datetime

from pdf_tools import merge_pdfs

documents = [
    '01-sample-document.pdf',
    '02-sample-document.pdf',
    '03-sample-document.pdf',
]

assets_dir = 'assets/'
output_dir = 'assets/outputs/'


def run(documents, assets_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    paths = []
    for pdf in documents:
        pdf_path = os.path.join(assets_dir, pdf)
        if os.path.isfile(pdf_path):
            paths.append(pdf_path)
            print(f"Added: {pdf_path}")
        else:
            print(f"Warning: {pdf_path} does not exist and will be skipped.")

    timestamp_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = os.path.join(output_dir, f"merged-file-{timestamp_str}.pdf")

    with open(output_path, "wb") as f:
        f.write(merge_pdfs(paths).read())
    print(f"PDFs merged successfully into: {output_path}")


if __name__ == "__main__":
    run(documents, assets_dir, output_dir)

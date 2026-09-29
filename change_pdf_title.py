from pypdf import PdfReader, PdfWriter

input_pdf = "input.pdf"
output_pdf = "output.pdf"

new_title = "ADD THE TITLE HERE"

reader = PdfReader(input_pdf)
writer = PdfWriter()

# Copy all pages
for page in reader.pages:
    writer.add_page(page)

# Preserve existing metadata, then change the title
metadata = reader.metadata or {}

writer.add_metadata({
    "/Title": new_title,
    "/Author": metadata.get("/Author", ""),
    "/Subject": metadata.get("/Subject", ""),
    "/Creator": metadata.get("/Creator", ""),
    "/Producer": metadata.get("/Producer", ""),
})

with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"Done! Created: {output_pdf}")

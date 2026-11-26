from pdf_tools import change_title

input_pdf = "input.pdf"
output_pdf = "output.pdf"

new_title = "ADD THE TITLE HERE"

if __name__ == "__main__":
    with open(output_pdf, "wb") as f:
        f.write(change_title(input_pdf, new_title).read())
    print(f"Done! Created: {output_pdf}")

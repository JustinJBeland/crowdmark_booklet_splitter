from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_pdf: str, pages_per_split: int, output_dir: str = "."):
    # Open the input PDF
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through in chunks
    for idx in range(0, total_pages, pages_per_split):
        writer = PdfWriter()
        # add this chunk of pages
        for j in range(idx, min(idx + pages_per_split, total_pages)):
            writer.add_page(reader.pages[j])

        # compute 1‑based part number and zero‑pad to 4 digits
        part_num = idx // pages_per_split + 1
        filename = f"{part_num:04d}.pdf"
        out_path = os.path.join(output_dir, filename)

        # write it out
        with open(out_path, "wb") as out_f:
            writer.write(out_f)

        print(f"Created: {out_path}")

    print(f"Total split PDFs created: { (total_pages + pages_per_split - 1) // pages_per_split }")

# Example usage:
if __name__ == "__main__":
    input_pdf       = "final.pdf"
    pages_per_split = 18
    output_dir      = "booklets"
    split_pdf(input_pdf, pages_per_split, output_dir)
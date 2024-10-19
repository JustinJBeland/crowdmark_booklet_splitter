from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_prefix, pages_per_split):
    # Open the input PDF
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    split_count = 0

    # Loop through the PDF in chunks of pages_per_split
    for i in range(0, total_pages, pages_per_split):
        # Create a PDF writer for the new split file
        writer = PdfWriter()

        # Add the pages for this split
        for j in range(i, min(i + pages_per_split, total_pages)):
            writer.add_page(reader.pages[j])
        
        # Generate output filename for the split PDF
        output_filename = f"{output_prefix}_part_{split_count + 1}.pdf"
        
        # Write the split PDF to the file
        with open(output_filename, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"Created: {output_filename}")
        split_count += 1

    print(f"Total split PDFs created: {split_count}")

# Example usage:
# Split a 1428-page PDF into 119 booklets, each with about 12 pages.
input_pdf = "mie250_main_booklets.pdf"  # Replace with your actual PDF file path
output_prefix = "exam_booklet"
pages_per_split = 12  # You want about 12 pages per booklet

# Call the function to split the PDF
split_pdf(input_pdf, output_prefix, pages_per_split)

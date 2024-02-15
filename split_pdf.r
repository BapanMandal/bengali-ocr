# Install and load the pdftools package
if (!requireNamespace("pdftools", quietly = TRUE)) {
  install.packages("pdftools")
}

library(pdftools)

# Function to split PDF into fixed ranges
split_pdf_by_ranges <- function(input_pdf, output_dir, page_length = 50) {
  pdf_info <- pdf_info(input_pdf)
  total_pages <- pdf_info[["pages"]]

  # Create the output directory if it doesn't exist
  dir.create(output_dir, showWarnings = FALSE)

  # Split the PDF into fixed ranges
  for (start_page in seq(1, total_pages, by = page_length)) {
    end_page <- min(start_page + page_length - 1, total_pages)

    output_file <- file.path(
      output_dir,
      sprintf("output_%d-%d.pdf", start_page, end_page)
    )

    pdf_subset(
      input_pdf,
      pages = start_page:end_page,
      output = output_file
    )

    cat("Created: ", output_file, "\n")
  }
}

input_pdf_file <- "compiler_book.pdf"
output_directory <- "output_pdfs"

split_pdf_by_ranges(input_pdf_file, output_directory)

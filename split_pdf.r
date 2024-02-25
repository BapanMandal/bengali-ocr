# import the required libraries
library(pdftools)



# Get command line arguments
args <- commandArgs(trailingOnly = TRUE)



# Function to split PDF into fixed ranges
split_pdf_by_ranges <- function(
  input_pdf_path,
  output_dir,
  pdf_subset_max_len = 50
) {
  # Get the total number of pages in the PDF
  pdf_info <- pdf_info(input_pdf_path)
  total_pages <- pdf_info[["pages"]]

  # Create the output directory if it doesn't exist
  dir.create(output_dir, showWarnings = FALSE)

  # Split the PDF into fixed ranges
  for (start_page in seq(1, total_pages, by = pdf_subset_max_len)) {
    end_page <- min(start_page + pdf_subset_max_len - 1, total_pages)

    output_file <- file.path(
      output_dir,
      sprintf("output_%d-%d.pdf", start_page, end_page)
    )

    pdf_subset(
      input_pdf_path,
      pages = start_page:end_page,
      output = output_file
    )

    cat("\tCreated: ", output_file, "\n")
  }

}



input_pdf_file <- args
output_directory <- "split_pdfs"

cat("\nSplitting the PDF into fixed ranges...\n")
split_pdf_by_ranges(input_pdf_file, output_directory)
cat("Done!\n\n")
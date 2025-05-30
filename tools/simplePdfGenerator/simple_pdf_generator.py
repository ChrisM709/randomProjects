import argparse
from fpdf import FPDF


def textToPdf(lines, outputPdf):
    """
    Generate a PDF file from a list of text lines.

    Parameters:
    - lines (list of str): The text lines to include in the PDF.
    - outputPdf (str): The filename for the generated PDF.
    """
    # initialize the pdf object
    pdf = FPDF()
    # enable automatic page breaks with a 15pt bottom margin to avoid text overflow
    pdf.set_auto_page_break(auto=True, margin=15)
    # add the first blank page
    pdf.add_page()
    # set the font to Arial, regular style, size 12pt
    pdf.set_font("Arial", size=12)

    # loop through each line and write it to the pdf
    for line in lines:
        pdf.cell(0, 8, txt=line, ln=1)

    # save the pdf to the specified file
    pdf.output(outputPdf)
    print(f"✅ Wrote {len(lines)} lines to {outputPdf}")


def main():
    """
    Entry point for the script:
    - Parse command-line arguments for output filename.
    - Prompt the user to paste or type text until a sentinel line 'EOF' (End-Of-File) is entered.
    - Generate a PDF from the provided text lines.
    """
    # set up argument parser to allow specifying output PDF name
    argParser = argparse.ArgumentParser(
        description="Convert pasted or typed text into a PDF."
    )
    argParser.add_argument(
        "-o", "--output",
        default="output.pdf",
        help="Name of the PDF file to create (default: output.pdf)"
    )
    args = argParser.parse_args()
    outputPdf = args.output  # store the output filename in camelCase variable

    # inform the user how to end input: EOF stands for End-Of-File
    print("Paste or type your text. To finish, type 'EOF' (End-Of-File) on a new line and press Enter:")
    lines = []
    # read lines until the sentinel 'EOF' is entered
    while True:
        try:
            line = input()
        except EOFError:
            # handle unexpected EOF (e.g., if stdin closes); exit loop
            break
        # if the user types 'EOF' exactly, we stop reading further input
        if line.strip() == 'EOF':
            break
        lines.append(line)

    # if no lines are provided, exit with a warning
    if not lines:
        print("⚠️ No text received. Exiting.")
        return

    # convert the collected lines into a pdf
    textToPdf(lines, outputPdf)


# if this script is run (instead of imported), execute the main function
if __name__ == "__main__":
    main()

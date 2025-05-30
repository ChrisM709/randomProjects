# Simple PDF Generator

Convert pasted or typed text into a PDF file via the command line.

![PyPI](https://img.shields.io/pypi/v/your-package)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.6%2B-green)


## Features

* reads multi-line text from standard input
* terminates input on a sentinel `EOF` line
* outputs a formatted PDF with automatic page breaks
* configure output filename via `-o`/`--output`
* lightweight dependency on [FPDF](https://pypi.org/project/fpdf/)

## Prerequisites

* Python 3.6+ installed
* `pip` for package management

## Installation

1. clone or download this repository
2. install dependencies:

   ```bash
   pip install fpdf
   ```

## Usage

```bash
python simple_pdf_generator.py [-o OUTPUT]
```

* `-o/--output`  name of the PDF file to create (default: `output.pdf`)

### Interactive Input

1. run the script:

   ```bash
   python simple_pdf_generator.py -o mydoc.pdf
   ```
2. when prompted:

   ```text
   Paste or type your text. To finish, type 'EOF' (End-Of-File) on a new line and press Enter:
   ```
3. paste or type your content line by line
4. on a new line, type:

   ```text
   EOF
   ```
5. the script will generate `mydoc.pdf` and print a confirmation

## Examples

```bash
$ python simple_pdf_generator.py -o notes.pdf
Paste or type your text. To finish, type 'EOF' (End-Of-File) on a new line and press Enter:
> This is page one.
> It has two lines.
> EOF
✅ Wrote 2 lines to notes.pdf
```

## File Structure

```
├── README.md
└── simple_pdf_generator.py
```

## License

MIT © your name

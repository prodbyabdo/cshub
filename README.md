# Math Document Tool

A modular, extensible tool for extracting structured content (Laws, Theorems, Examples, Exercises) from PDF documents and automatically solving math problems using SymPy.

## Features

- **Generic Extraction**: Extract content from any PDF using configurable regex patterns.
- **Automated Solving**: Automatically solves standard Calculus problems (Derivatives, Integrals) found in the text.
- **Modular Design**: Easy to extend for other subjects (Physics, Chemistry, etc.) by finding new patterns.
- **Clean Output**: Generates structured Markdown files with "Solution" and "Law" categories.

## Installation

Requires Python 3.8+.

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install pdfplumber sympy
    ```

## Usage

### Basic Extraction

Run the CLI tool on a PDF file:

```bash
python process_math_pdf.py "path/to/document.pdf"
```

This will create a Markdown file in `output_math_tool/`.

### Extraction with Solver

To automatically attempt to solve exercises found in the text:

```bash
python process_math_pdf.py "path/to/document.pdf" --solve
```

### Specifying Output Directory

```bash
python process_math_pdf.py "input.pdf" --output "my_notes"
```

## Configuration

Settings are managed in `math_doc_tool/config.py`.

## Extending for New Subjects

To add support for a new subject (e.g., Physics):

1.  Create a new pattern file (e.g., `math_doc_tool/extractors/physics_patterns.py`).
2.  Define `DEFAULT_PATTERNS` with keys for `laws` (e.g., Newton's Laws) and `solutions` (Examples).
3.  Inject these patterns into the `PatternExtractor` in `process_math_pdf.py`.

## Project Structure

- `math_doc_tool/`: Main package.
    - `core.py`: Data models.
    - `solver.py`: SymPy integration logic.
    - `extractors/`: Extraction strategies.
- `process_math_pdf.py`: CLI Entry point.

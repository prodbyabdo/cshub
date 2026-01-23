import os
from pathlib import Path
from math_doc_tool.extractors.pattern_extractor import PatternExtractor
from math_doc_tool.extractors.text_extractor import TextExtractor
from math_doc_tool.solver import MathSolver
from math_doc_tool.core import ExtractedItem

# Configuration
SOURCE_ROOT = Path("uni data")
OUTPUT_ROOT = Path("output_pdfplumber/markdown_cache")
SUBJECTS = {
    #"Discrete Math New": "Discrete Math",
    #"Econ": "Economics",
    #"Information Systems": "Information Systems",
    #"Managment": "Management",
    #"Comp Applications": "Comp Applications",
    "INTRODUCTION TO CS&IT": "IntroCS"
}

def process_file(pdf_path, subject, output_dir):
    print(f"Processing {pdf_path.name} ({subject})...")
    
    # Select Extractor
    if subject == "Discrete Math":
        extractor = PatternExtractor()
    else:
        # Non-math subjects: Extract raw text for later summarization
        extractor = TextExtractor()
    
    try:
        items = extractor.extract(pdf_path)
    except Exception as e:
        print(f"  Error extracting {pdf_path}: {e}")
        return

    # Skip solving for non-math subjects to save time/errors
    if subject != "Discrete Math":
        pass # No solver
    else:
        # Maybe generic math solver for Discrete Math?
        pass

    # Save Markdown
    output_dir.mkdir(parents=True, exist_ok=True)
    out_name = pdf_path.stem + ".md"
    out_file = output_dir / out_name
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Extracted Content: {pdf_path.name}\n\n")
        if not items:
            f.write("> No specific 'Laws' or 'Solutions' patterns found. This might be a slide deck.\n\n")
        
        for item in items:
            f.write(f"### {item.item_type} (Page {item.page_number})\n")
            f.write(f"**Category**: {item.category}\n\n")
            f.write(f"> {item.content.replace(chr(10), chr(10)+'> ')}\n\n")
            f.write("---\n\n")
    
    print(f"  Saved to {out_file}")

def main():
    for folder_name, subject in SUBJECTS.items():
        folder_path = SOURCE_ROOT / folder_name
        if not folder_path.exists():
            print(f"Skipping {folder_name} (not found)")
            continue

        print(f"\n--- Scanning {folder_name} ---")
        # specific output dir for this subject
        subject_out_dir = OUTPUT_ROOT / folder_name
        
        for pdf_file in folder_path.glob("*.pdf"):
            process_file(pdf_file, subject, subject_out_dir)

if __name__ == "__main__":
    main()

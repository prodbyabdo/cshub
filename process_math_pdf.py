import argparse
import sys
from pathlib import Path
from math_doc_tool.config import Config
from math_doc_tool.extractors.pattern_extractor import PatternExtractor
from math_doc_tool.solver import MathSolver

def main():
    parser = argparse.ArgumentParser(description="Math PDF Processor")
    parser.add_argument("input", help="Input PDF file or directory")
    parser.add_argument("--output", "-o", help="Output directory", default="output_math_tool")
    parser.add_argument("--subject", "-s", help="Subject (Calculus, LinearAlgebra, Generic)", default="Calculus")
    
    parser.add_argument("--solve", action="store_true", help="Attempt to solve extracted exercises")
    
    args = parser.parse_args()
    
    # Setup
    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(exist_ok=True, parents=True)
    
    print(f"--- Math PDF Processor (Subject: {args.subject}) ---")
    
    # Select Extractor
    extractor = PatternExtractor()
    solver = MathSolver() if args.solve else None
    
    # Gather Files
    files = []
    if input_path.is_file():
        files.append(input_path)
    elif input_path.is_dir():
        files.extend(list(input_path.glob("*.pdf")))
        
    if not files:
        print("No PDF files found.")
        return

    # Process
    for pdf_file in files:
        items = extractor.extract(pdf_file)
        print(f"  Extracted {len(items)} items from {pdf_file.name}")
        
        # Solving Phase
        if solver:
            print("  Running solver on exercises...")
            for item in items:
                # We assume "Solution" categories might be exercises to verify, 
                # or "Law" might contain examples. Patterns usually map "Example/Exercise" -> "Solution" category.
                if item.category == "Solution" or "Example" in item.item_type or "Exercise" in item.item_type:
                    solution = solver.solve(item)
                    if solution:
                        item.computed_answer = solution

        # Simple Markdown Dump
        out_name = pdf_file.stem + ".md"
        out_file = output_path / out_name
        
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"# Extracted Content: {pdf_file.name}\n\n")
            for item in items:
                f.write(f"### {item.item_type} (Page {item.page_number})\n")
                f.write(f"**Category**: {item.category}\n\n")
                f.write(f"> {item.content.replace(chr(10), chr(10)+'> ')}\n\n")
                
                if item.computed_answer:
                    f.write(f"> [!TIP] **AI Solver**\n> {item.computed_answer}\n\n")

                if item.solution_content:
                    f.write(f"**Original Solution**:\n> {item.solution_content.replace(chr(10), chr(10)+'> ')}\n\n")
                f.write("---\n\n")
        
        print(f"  Saved to {out_file}")

if __name__ == "__main__":
    main()

"""
Extraction Script for Calculus Lecture Notes
Extracts Laws/Theorems and Solutions/Examples from separate PDF files.
"""

import pdfplumber
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List
import re
import warnings
import sys

# Suppress pdfplumber font warnings
warnings.filterwarnings('ignore', message='.*FontBBox.*')


def _safe_print(text: str) -> str:
    """Sanitize text for console output."""
    try:
        text.encode(sys.stdout.encoding or 'utf-8')
        return text
    except (UnicodeEncodeError, UnicodeDecodeError, AttributeError):
        return text.encode('ascii', 'replace').decode('ascii')


@dataclass
class ExtractedItem:
    page_number: int
    item_type: str  # "Law", "Theorem", "Definition", "Solution", "Example", "Problem"
    category: str   # "Law" or "Solution"
    content: str    # Full content or Statement
    solution_content: Optional[str] = None # content after "Sol"
    is_near_page_boundary: bool = False


class PDFProcessor:
    def __init__(self, pdf_path: str | Path):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        self.items: List[ExtractedItem] = []

    # Regex patterns
    LAW_PATTERNS = [
        r'\b(Rule|Theorem|Definition|Corollary|Lemma|Proposition|Formula|Property)\s*[\d.]*[:\s]',
    ]
    SOLUTION_PATTERNS = [
        r'\b(Example|Solution|Problem|Exercise)\s*[\d.]*[:\s]',
    ]

    def _determine_category(self, text: str) -> tuple[str, str]:
        """Determine type and category (Law vs Solution) from text."""
        # Check Laws
        for pattern in self.LAW_PATTERNS:
            match = re.search(r'\b(Rule|Theorem|Definition|Corollary|Lemma|Proposition|Formula|Property)\b', 
                             text, re.IGNORECASE)
            if match:
                return match.group(1).title(), "Law"
        
        # Check Solutions
        for pattern in self.SOLUTION_PATTERNS:
            match = re.search(r'\b(Example|Solution|Problem|Exercise)\b',
                             text, re.IGNORECASE)
            if match:
                return match.group(1).title(), "Solution"
                
        return "Unknown", "Unknown"

    def extract(self) -> List[ExtractedItem]:
        self.items = []
        print(f"Processing {self.pdf_path.name}...")
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue
                
                # Split by double newlines to find blocks
                paragraphs = re.split(r'\n\s*\n', text)
                
                current_item = None
                
                for para in paragraphs:
                    para = para.strip()
                    if not para:
                        continue
                        
                    # Check start of new item
                    item_type, category = self._determine_category(para)
                    
                    if category != "Unknown":
                        # If we were processing an item, save it
                        if current_item:
                             self.items.append(current_item)
                        
                        # Start new item
                        current_item = ExtractedItem(
                            page_number=page_num,
                            item_type=item_type,
                            category=category,
                            content=para
                        )
                    elif current_item:
                        # Continue existing item
                        current_item.content += "\n\n" + para
                        
                # Append last item of page
                if current_item:
                    self.items.append(current_item)

        # Post-processing: Split Solution Content
        for item in self.items:
            if item.category == "Solution":
                # Look for "Sol" or "Solution" marker
                # pattern: newline + Sol + newline/space or just Sol at start of line
                split_match = re.search(r'\n\s*(Sol|Solution)\s*[:.]?\s*\n', item.content, re.IGNORECASE)
                if split_match:
                    start_sol = split_match.start()
                    end_sol = split_match.end()
                    item.solution_content = item.content[end_sol:].strip()
                    item.content = item.content[:start_sol].strip() # This becomes Statement

        return self.items

    def to_markdown(self) -> str:
        if not self.items:
            return f"# Extracted Content\n\n_No content found in {self.pdf_path.name}_\n"
            
        lines = [
            f"# Content Extracted from {self.pdf_path.name}",
            "",
            "---",
            ""
        ]
        
        for i, item in enumerate(self.items, start=1):
            lines.append(f"### {item.item_type} (Page {item.page_number})")
            lines.append(f"**Category:** {item.category}")
            lines.append("")
            
            lines.append("**Statement:**")
            # Quote block for statement
            content_lines = item.content.split('\n')
            for cl in content_lines:
                lines.append(f"> {cl}")
            lines.append("")
            
            if item.solution_content:
                lines.append("**Solution:**")
                # Quote block for solution
                sol_lines = item.solution_content.split('\n')
                for sl in sol_lines:
                    lines.append(f"> {sl}")
                lines.append("")
            
            lines.append("---")
            lines.append("")
            
        return '\n'.join(lines)


def main():
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "output_pdfplumber"
    output_dir.mkdir(exist_ok=True)

    # 3 Specific files
    target_files = [
        "Calculus 1 lecnote6_202512281307_52093.pdf",
        "Calculus 1 lecnote7_202512281308_09617.pdf",
        "Calculus 1 lecnote8_202512281308_49361.pdf"
    ]

    for fname in target_files:
        pdf_path = data_dir / fname
        if not pdf_path.exists():
            print(f"Skipping missing file: {fname}")
            continue
            
        processor = PDFProcessor(pdf_path)
        processor.extract()
        
        # Save MD
        out_name = fname.replace(".pdf", ".md").replace(" ", "_")
        out_path = output_dir / out_name
        out_path.write_text(processor.to_markdown(), encoding='utf-8')
        print(f"Saved: {out_path.name}")

if __name__ == "__main__":
    main()

"""
Precision Extraction of Calculus Rules via Geometric Detection

Extracts mathematical rules/theorems from PDF documents using:
1. Lines that form boxes (rectangle detection from line segments)
2. Text patterns (Rule, Theorem, Definition keywords)
3. Native rect objects when available

Uses pdfplumber's coordinate-based geometry detection (not OCR).
"""

import pdfplumber
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import re
import warnings
import sys

# Suppress pdfplumber font warnings
warnings.filterwarnings('ignore', message='.*FontBBox.*')


def _safe_print(text: str) -> str:
    """Sanitize text for console output (handles special Unicode chars)."""
    try:
        # Try encoding to console encoding
        text.encode(sys.stdout.encoding or 'utf-8')
        return text
    except (UnicodeEncodeError, UnicodeDecodeError):
        # Replace problematic characters
        return text.encode('ascii', 'replace').decode('ascii')


@dataclass
class ExtractedRule:
    """Represents an extracted rule/theorem from a PDF."""
    page_number: int
    rule_index: int
    rule_type: str  # "box", "keyword", "table"
    content: str
    bbox: Optional[tuple[float, float, float, float]] = None
    is_near_page_boundary: bool = False


class RuleExtractor:
    """Extracts rules from PDF using multiple detection strategies."""
    
    # Thresholds for box detection
    MIN_BOX_AREA = 3000  # Minimum area in pts²
    MIN_BOX_WIDTH = 100  # Minimum width in pts
    MIN_BOX_HEIGHT = 30  # Minimum height in pts
    LINE_TOLERANCE = 5   # Tolerance for line alignment (pts)
    MARGIN_TOLERANCE = 5
    BOUNDARY_MARGIN = 50
    
    # Keyword patterns for text-based extraction
    RULE_KEYWORDS = [
        r'\b(Rule|Theorem|Definition|Corollary|Lemma|Proposition|Formula|Property)\s*[\d.]*[:\s]',
    ]
    
    def __init__(self, pdf_path: str | Path):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
        self.rules: list[ExtractedRule] = []
    
    def _find_boxes_from_lines(self, lines: list[dict], page_width: float, page_height: float) -> list[tuple]:
        """
        Detect rectangles formed by 4 lines.
        Returns list of bboxes: (x0, y0, x1, y1)
        """
        if not lines:
            return []
        
        # Separate horizontal and vertical lines
        h_lines = []  # horizontal: height ~= 0
        v_lines = []  # vertical: width ~= 0
        
        for line in lines:
            width = abs(line['x1'] - line['x0'])
            height = abs(line['y1'] - line['y0'])
            
            if height < self.LINE_TOLERANCE and width > self.MIN_BOX_WIDTH:
                h_lines.append(line)
            elif width < self.LINE_TOLERANCE and height > self.MIN_BOX_HEIGHT:
                v_lines.append(line)
        
        boxes = []
        
        # Try to find rectangles: 2 horizontal + 2 vertical lines
        for h1 in h_lines:
            for h2 in h_lines:
                if h1 == h2:
                    continue
                
                # Check if horizontals are aligned (same x range)
                if abs(h1['x0'] - h2['x0']) > self.LINE_TOLERANCE:
                    continue
                if abs(h1['x1'] - h2['x1']) > self.LINE_TOLERANCE:
                    continue
                
                # Get y positions
                y_top = min(h1['y0'], h2['y0'])
                y_bottom = max(h1['y1'], h2['y1'])
                
                if abs(y_bottom - y_top) < self.MIN_BOX_HEIGHT:
                    continue
                
                # Check for vertical lines connecting them
                x_left = min(h1['x0'], h2['x0'])
                x_right = max(h1['x1'], h2['x1'])
                
                has_left = any(
                    abs(v['x0'] - x_left) < self.LINE_TOLERANCE and
                    v['y0'] <= y_top + self.LINE_TOLERANCE and
                    v['y1'] >= y_bottom - self.LINE_TOLERANCE
                    for v in v_lines
                )
                
                has_right = any(
                    abs(v['x0'] - x_right) < self.LINE_TOLERANCE and
                    v['y0'] <= y_top + self.LINE_TOLERANCE and
                    v['y1'] >= y_bottom - self.LINE_TOLERANCE
                    for v in v_lines
                )
                
                if has_left and has_right:
                    bbox = (x_left, y_top, x_right, y_bottom)
                    area = (x_right - x_left) * (y_bottom - y_top)
                    if area >= self.MIN_BOX_AREA:
                        # Avoid duplicates
                        is_dup = any(
                            abs(b[0] - bbox[0]) < self.LINE_TOLERANCE and
                            abs(b[1] - bbox[1]) < self.LINE_TOLERANCE
                            for b in boxes
                        )
                        if not is_dup:
                            boxes.append(bbox)
        
        return boxes
    
    def _find_rules_by_keyword(self, text: str, page_num: int) -> list[ExtractedRule]:
        """Extract rules based on keyword patterns in text."""
        rules = []
        
        if not text:
            return rules
        
        # Combined pattern for all keywords
        pattern = '|'.join(self.RULE_KEYWORDS)
        
        # Split text into paragraphs/sections
        paragraphs = re.split(r'\n\s*\n', text)
        
        rule_idx = 0
        for para in paragraphs:
            if re.search(pattern, para, re.IGNORECASE):
                # Found a rule/theorem/definition
                rule_idx += 1
                
                # Clean up the content
                content = para.strip()
                
                # Determine the rule type
                match = re.search(r'\b(Rule|Theorem|Definition|Corollary|Lemma|Proposition|Formula|Property)\b', 
                                 para, re.IGNORECASE)
                rule_type = match.group(1).title() if match else "Rule"
                
                rules.append(ExtractedRule(
                    page_number=page_num,
                    rule_index=rule_idx,
                    rule_type=rule_type,
                    content=content
                ))
        
        return rules
    
    def _extract_text_from_bbox(self, page, bbox: tuple) -> Optional[str]:
        """Extract text within a bounding box."""
        try:
            # Ensure bbox is within page bounds
            x0, y0, x1, y1 = bbox
            x0 = max(0, x0)
            y0 = max(0, y0)
            x1 = min(page.width, x1)
            y1 = min(page.height, y1)
            
            cropped = page.within_bbox((x0, y0, x1, y1))
            text = cropped.extract_text()
            return text.strip() if text else None
        except Exception as e:
            return None
    
    def _is_near_boundary(self, bbox: tuple, page_height: float) -> bool:
        """Check if box is near page top/bottom."""
        y0, y1 = bbox[1], bbox[3]
        near_top = y0 < self.BOUNDARY_MARGIN
        near_bottom = y1 > page_height - self.BOUNDARY_MARGIN
        return near_top or near_bottom
    
    def extract(self, verbose: bool = True) -> list[ExtractedRule]:
        """Extract all rules from the PDF using multiple strategies."""
        self.rules = []
        box_rules = []
        keyword_rules = []
        
        with pdfplumber.open(self.pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"Processing {self.pdf_path.name} ({total_pages} pages)...")
            
            for page_num, page in enumerate(pdf.pages, start=1):
                page_width = page.width
                page_height = page.height
                
                # Strategy 1: Find boxes from lines
                lines = page.lines or []
                boxes = self._find_boxes_from_lines(lines, page_width, page_height)
                
                if verbose and boxes:
                    print(f"  Page {page_num}: Found {len(boxes)} boxes from lines")
                
                for idx, bbox in enumerate(boxes, start=1):
                    text = self._extract_text_from_bbox(page, bbox)
                    if text and len(text) > 20:  # Minimum content length
                        rule = ExtractedRule(
                            page_number=page_num,
                            rule_index=idx,
                            rule_type="Box",
                            content=text,
                            bbox=bbox,
                            is_near_page_boundary=self._is_near_boundary(bbox, page_height)
                        )
                        box_rules.append(rule)
                        
                        if verbose:
                            preview = text[:50].replace('\n', ' ') + ('...' if len(text) > 50 else '')
                            print(f"    Box {idx}: \"{_safe_print(preview)}\"")
                
                # Strategy 2: Find rules by keywords in page text
                page_text = page.extract_text() or ""
                kw_rules = self._find_rules_by_keyword(page_text, page_num)
                
                if verbose and kw_rules:
                    print(f"  Page {page_num}: Found {len(kw_rules)} keyword-based rules")
                    for r in kw_rules:
                        preview = r.content[:50].replace('\n', ' ') + ('...' if len(r.content) > 50 else '')
                        print(f"    {r.rule_type}: \"{_safe_print(preview)}\"")
                
                keyword_rules.extend(kw_rules)
        
        # Combine BOTH box-based and keyword-based results
        self.rules = []
        
        # Add box-based rules first (geometry-detected)
        if box_rules:
            self.rules.extend(box_rules)
            print(f"\nBOX-based extraction: {len(box_rules)} rules found.")
        
        # Add keyword-based rules  
        if keyword_rules:
            self.rules.extend(keyword_rules)
            print(f"KEYWORD-based extraction: {len(keyword_rules)} rules found.")
        
        # Sort by page number
        self.rules.sort(key=lambda r: (r.page_number, r.rule_index))
        
        print(f"Total extracted: {len(self.rules)} rules/theorems.")
        return self.rules
    
    def to_markdown(self) -> str:
        """Convert extracted rules to Markdown format."""
        if not self.rules:
            return "# Calculus Rules Extracted\n\n_No rules found in the PDF._\n"
        
        lines = [
            "# Calculus Rules Extracted",
            "",
            f"_Extracted from: {self.pdf_path.name}_",
            "",
            "---",
            ""
        ]
        
        current_page = None
        
        for i, rule in enumerate(self.rules, start=1):
            # Add page header if new page
            if rule.page_number != current_page:
                current_page = rule.page_number
                lines.append(f"## Page {current_page}")
                lines.append("")
            
            # Add rule header
            lines.append(f"### {rule.rule_type} {i}")
            lines.append("")
            
            # Add boundary warning if applicable
            if rule.is_near_page_boundary:
                lines.append("> [!NOTE]")
                lines.append("> _This content may continue on the next page._")
                lines.append("")
            
            # Add the actual content in a blockquote for visual separation
            content_lines = rule.content.split('\n')
            for cl in content_lines:
                lines.append(f"> {cl}")
            lines.append("")
            lines.append("---")
            lines.append("")
        
        return '\n'.join(lines)
    
    def save_markdown(self, output_path: str | Path) -> Path:
        """Save extracted rules to a Markdown file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        markdown = self.to_markdown()
        output_path.write_text(markdown, encoding='utf-8')
        
        print(f"Saved to: {output_path}")
        return output_path


def main():
    """Main entry point."""
    # Paths configuration
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    output_dir = base_dir / "output"
    
    # PDF files
    test_pdf = data_dir / "CALC QUESTIONS ONLY.pdf"
    main_pdf = data_dir / "CALC MERGED.pdf"
    output_file = output_dir / "Calculus_Rules_Extracted.md"
    
    # Run on test file first
    print("=" * 60)
    print("TESTING with: CALC QUESTIONS ONLY.pdf")
    print("=" * 60)
    
    if test_pdf.exists():
        extractor = RuleExtractor(test_pdf)
        extractor.extract(verbose=True)
        
        if extractor.rules:
            test_output = output_dir / "Test_Extraction.md"
            extractor.save_markdown(test_output)
    else:
        print(f"Test PDF not found: {test_pdf}")
    
    print()
    print("=" * 60)
    print("MAIN EXTRACTION: CALC MERGED.pdf")
    print("=" * 60)
    
    if main_pdf.exists():
        extractor = RuleExtractor(main_pdf)
        extractor.extract(verbose=True)
        extractor.save_markdown(output_file)
    else:
        print(f"Main PDF not found: {main_pdf}")


if __name__ == "__main__":
    main()

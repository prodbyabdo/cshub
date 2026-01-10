import re
import pdfplumber
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from ..core import ExtractedItem
from .base import BaseExtractor

class PatternExtractor(BaseExtractor):
    """
    Extracts content using regex patterns.
    Patterns can be customized for different subjects.
    """
    
    # Default patterns (Calculus/Math centered)
    DEFAULT_PATTERNS = {
        "laws": [
            r'\b(Rule|Theorem|Definition|Corollary|Lemma|Proposition|Formula|Property|Identity)\s*[\d.]*[:\s]',
        ],
        "solutions": [
            r'\b(Example|Solution|Problem|Exercise)\s*[\d.]*[:\s]',
        ]
    }

    def __init__(self, patterns: Optional[Dict[str, List[str]]] = None):
        self.patterns = patterns or self.DEFAULT_PATTERNS
        self.law_keywords = self._extract_keywords(self.patterns.get("laws", []))
        self.sol_keywords = self._extract_keywords(self.patterns.get("solutions", []))

    def _extract_keywords(self, pattern_list: List[str]) -> List[str]:
        """Simple helper to extract keyword words from regex for classification."""
        # This is a bit heuristic, assumes patterns start with \b(Word|Word)\b like structure
        keywords = []
        for p in pattern_list:
            # simple extraction of words inside parens
            match = re.search(r'\(([\w|]+)\)', p)
            if match:
                keywords.extend(match.group(1).split('|'))
        return keywords

    def _determine_category(self, text: str) -> Tuple[str, str]:
        """
        Determine type and category from text.
        Returns: (ItemType, Category)
        Example: ("Theorem", "Law") or ("Example", "Solution")
        """
        # Check Laws
        for pattern in self.patterns.get("laws", []):
            # We match strictly on the specific pattern structure provided
            # But for robustness, we search for the keywords first
            match = re.search(r'\b(' + '|'.join(self.law_keywords) + r')\b', text, re.IGNORECASE)
            if match:
                return match.group(1).title(), "Law"
        
        # Check Solutions
        for pattern in self.patterns.get("solutions", []):
            match = re.search(r'\b(' + '|'.join(self.sol_keywords) + r')\b', text, re.IGNORECASE)
            if match:
                return match.group(1).title(), "Solution"
                
        return "Unknown", "Unknown"

    def extract(self, file_path: Path) -> List[ExtractedItem]:
        items = []
        if not file_path.exists():
            print(f"File not found: {file_path}")
            return items

        print(f"Extracting from {file_path.name} using PatternExtractor...")
        
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue
                
                # Split roughly by double newlines or visual gaps
                paragraphs = re.split(r'\n\s*\n', text)
                
                current_item = None
                
                for para in paragraphs:
                    para = self._clean_text(para)
                    if not para:
                        continue
                        
                    item_type, category = self._determine_category(para)
                    
                    if category != "Unknown":
                        # Save previous item
                        if current_item:
                            items.append(current_item)
                        
                        # Start new item
                        current_item = ExtractedItem(
                            item_type=item_type,
                            category=category,
                            content=para,
                            page_number=page_num,
                            source_file=file_path.name
                        )
                    elif current_item:
                        # Append to existing
                        current_item.content += "\n\n" + para
                
                # Append last item of page
                if current_item:
                    items.append(current_item)
        
        # Post-process: Split Solution Content
        # Uses explicit "Sol" or "Solution" markers inside the text block
        for item in items:
            if item.category == "Solution":
                split_match = re.search(r'\n\s*(Sol|Solution)\s*[:.]?\s*\n', item.content, re.IGNORECASE)
                if split_match:
                    item.solution_content = item.content[split_match.end():].strip()
                    item.content = item.content[:split_match.start()].strip()

        return items

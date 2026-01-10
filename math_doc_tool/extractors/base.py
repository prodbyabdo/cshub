from typing import List
from pathlib import Path
from ..core import ContentExtractor, ExtractedItem

class BaseExtractor(ContentExtractor):
    """
    Base implementation for extractors.
    Can hold common utility methods for text processing or regex helpers.
    """
    
    def extract(self, file_path: Path) -> List[ExtractedItem]:
        raise NotImplementedError("Subclasses must implement extract()")
    
    def _clean_text(self, text: str) -> str:
        """Common text cleanup utilities."""
        if not text:
            return ""
        return text.strip()

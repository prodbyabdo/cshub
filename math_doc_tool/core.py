from dataclasses import dataclass, field
from typing import Optional, List, Any
from abc import ABC, abstractmethod
from pathlib import Path

@dataclass
class ExtractedItem:
    """Represents a single extracted unit of content."""
    item_type: str  # e.g. "Theorem", "Example", "Exercise"
    category: str   # "Law" or "Solution"
    content: str    # The main text content
    
    # metadata
    page_number: Optional[int] = None
    source_file: Optional[str] = None
    
    # For exercises/examples
    solution_content: Optional[str] = None
    
    # For computed results
    computed_answer: Optional[str] = None

class ContentExtractor(ABC):
    """Abstract base class for extraction strategies."""
    
    @abstractmethod
    def extract(self, file_path: Path) -> List[ExtractedItem]:
        pass

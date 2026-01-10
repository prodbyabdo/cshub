import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Config:
    # Default to current working directory if not specified
    base_dir: Path = field(default_factory=lambda: Path(os.getcwd()))
    
    # Input/Output directories
    input_dir: Path = field(default_factory=lambda: Path("data"))
    output_dir: Path = field(default_factory=lambda: Path("output_pdfplumber"))
    
    # Processing settings
    solve_exercises: bool = False
    supported_subjects: List[str] = field(default_factory=lambda: ["Calculus", "Linear Algebra"])
    
    # Extraction settings
    extraction_strategy: str = "pattern"  # pattern, geometric, etc.

    def __post_init__(self):
        # Resolve paths relative to base_dir if they are not absolute
        if not self.input_dir.is_absolute():
            self.input_dir = self.base_dir / self.input_dir
        
        if not self.output_dir.is_absolute():
            self.output_dir = self.base_dir / self.output_dir

        # Ensure directories exist
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def load(cls, base_path: Optional[Path] = None):
        """Load configuration. check env vars or default."""
        # For now, just simplistic default loading. 
        # In future we can load from .env or config.yaml
        if base_path:
            return cls(base_dir=base_path)
        return cls()

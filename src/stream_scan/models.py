# models.py
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ScanResult:
    is_valid: bool
    flags: List[str]        # e.g., ["Potential PII", "Toxic Language"]
    scores: Dict[str, float] # e.g., {"toxicity": 0.92, "readability": 12.5}
    details: str            # A detailed message for the user

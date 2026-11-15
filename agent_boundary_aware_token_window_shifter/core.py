"""Core implementation of boundary-aware window shifter."""
from typing import Optional

class BoundaryAwareWindowShifter:
    @staticmethod
    def slice_window(text: str, max_chars: int) -> str:
        if len(text) <= max_chars:
            return text

        candidate = text[:max_chars]
        # Seek sentence or paragraph boundaries first
        for d in ["\n\n", "\n", ". "]:
            last_idx = candidate.rfind(d)
            if last_idx != -1:
                cut_idx = last_idx + len(d)
                return text[:cut_idx].strip()

        # Fallback to word boundary
        last_space = candidate.rfind(" ")
        if last_space != -1 and last_space > max_chars // 3:
            return text[:last_space].strip()

        return candidate.strip()

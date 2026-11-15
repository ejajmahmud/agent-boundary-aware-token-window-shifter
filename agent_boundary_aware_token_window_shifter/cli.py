"""CLI for Boundary-Aware Window Shifter."""
import argparse
from .core import BoundaryAwareWindowShifter

def main():
    parser = argparse.ArgumentParser(description="Boundary-Aware Window Shifter CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate boundary-aware slicing")
    args = parser.parse_args()

    sample = "First sentence completed. Second sentence in progress but getting long here. Third sentence."
    sliced = BoundaryAwareWindowShifter.slice_window(sample, max_chars=45)
    print(f"Original: '{sample}'")
    print(f"Clean Slice (45 chars limit): '{sliced}'")

if __name__ == "__main__":
    main()

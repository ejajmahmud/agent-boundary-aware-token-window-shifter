"""Automated test suite for Boundary-Aware Window Shifter."""
import unittest
from agent_boundary_aware_token_window_shifter.core import BoundaryAwareWindowShifter

class TestBoundaryAwareWindowShifter(unittest.TestCase):
    def test_sentence_boundary_preservation(self):
        text = "Hello world. This is a very long test sentence that must be cut. End."
        sliced = BoundaryAwareWindowShifter.slice_window(text, max_chars=30)
        self.assertEqual(sliced, "Hello world.")

    def test_short_text_unmodified(self):
        text = "Short text."
        self.assertEqual(BoundaryAwareWindowShifter.slice_window(text, 50), text)

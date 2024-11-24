# tests/test_analyzer.py

import unittest
from text_analyzer import count_characters, count_spaces, count_uppercase, count_lowercase, count_punctuation

class TestTextAnalyzer(unittest.TestCase):
    def test_count_characters(self):
        self.assertEqual(count_characters("Hello"), 5)

    def test_count_spaces(self):
        self.assertEqual(count_spaces("Hello World"), 1)

    def test_count_uppercase(self):
        self.assertEqual(count_uppercase("Hello World"), 2)

    def test_count_lowercase(self):
        self.assertEqual(count_lowercase("Hello World"), 8)

    def test_count_punctuation(self):
        self.assertEqual(count_punctuation("Hello, World!"), 2)

if __name__ == "__main__":
    unittest.main()
 

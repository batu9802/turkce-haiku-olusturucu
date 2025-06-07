import unittest
import io
import sys
import re
from pyton import (
    count_syllables,
    choose_word,
    generate_haiku_line,
    generate_haiku,
    MASTER_WORD_LIST,
    HAIKU_SYLLABLES,
    TURKISH_VOWELS # Import if needed for any test setup, though direct use is unlikely
)

class TestHaikuGenerator(unittest.TestCase):

    def test_count_syllables_basic(self):
        self.assertEqual(count_syllables("merhaba"), 3)
        self.assertEqual(count_syllables("aeıioöuü"), 8)
        self.assertEqual(count_syllables("AEIİOÖUÜ"), 8)
        self.assertEqual(count_syllables("köy"), 1) # öy is one vowel sound
        self.assertEqual(count_syllables("su"), 1)
        self.assertEqual(count_syllables(""), 0)
        self.assertEqual(count_syllables("büyüleyici"), 5) # from existing word list

    def test_choose_word_finds_word(self):
        sample_pool = [{'text': 'kısa', 'syllables': 2}, {'text': 'uzunbiraz', 'syllables': 4}]
        chosen = choose_word(sample_pool, 2)
        self.assertIsNotNone(chosen)
        if chosen: # Should always be true if NotNone
            self.assertLessEqual(chosen['syllables'], 2)
            self.assertEqual(chosen['text'], 'kısa') # Only one option

        chosen_too_long = choose_word(sample_pool, 1)
        self.assertIsNone(chosen_too_long)

    def test_choose_word_empty_pool(self):
        chosen = choose_word([], 5)
        self.assertIsNone(chosen)

    def test_generate_haiku_line_basic(self):
        # Ensure MASTER_WORD_LIST has some variety for a more robust test,
        # or create a specific pool for this test.
        # Using MASTER_WORD_LIST, but acknowledging randomness.
        if not MASTER_WORD_LIST: # Should not happen with current pyton.py
            self.skipTest("MASTER_WORD_LIST is empty, cannot test generate_haiku_line effectively.")

        # Make sure there's at least one word with 1 syllable for the > 0 assertion later
        has_one_syllable_word = any(word['syllables'] == 1 for word in MASTER_WORD_LIST)

        line_words, syllables = generate_haiku_line(MASTER_WORD_LIST, 5)

        self.assertIsInstance(line_words, list)
        self.assertIsInstance(syllables, int)
        self.assertGreaterEqual(syllables, 0)

        if line_words: # If any word was chosen
             # Syllables should be > 0 if a word is picked and there are 1-syllable words
            if has_one_syllable_word or syllables > 0 : # if syllables > 0, a word was picked
                 self.assertGreater(syllables, 0)

        self.assertLessEqual(syllables, 5) # It should not exceed the target

    def test_generate_haiku_line_no_words_fit(self):
        sample_pool = [{'text': 'çokuzunbirşey', 'syllables': 5}] # A word that is 5 syllables
        line_words, syllables = generate_haiku_line(sample_pool, 1) # Target 1 syllable

        # choose_word will return None for the first word if 'çokuzunbirşey' (5) > 1
        # Then, remaining_syllables = 1. choose_word again with max_syllables=1, returns None.
        self.assertEqual(len(line_words), 0)
        self.assertEqual(syllables, 0)

    def test_generate_haiku_output_structure(self):
        # Capture stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        generate_haiku() # Call the function that prints

        sys.stdout = sys.__stdout__  # Reset redirect.

        output = captured_output.getvalue()

        # Check for the header
        self.assertIn("Haiku Oluşturucu", output)

        lines = output.strip().split('\n')
        # Expected: Header line, then 3 haiku lines
        # Adjust if generate_haiku adds more lines or if the header is multi-line
        header_lines = 0
        if "----" in lines[0]: header_lines +=1
        if "Haiku Oluşturucu" in lines[header_lines]: header_lines +=1
        if "----" in lines[header_lines]: header_lines +=1

        haiku_lines = lines[header_lines:]
        self.assertEqual(len(haiku_lines), 3, "Should be 3 lines in the haiku.")

        syllable_pattern = re.compile(r".+ \((\d+) syllables\)$")
        # Also check for empty lines like " (0 syllables)"
        empty_line_pattern = re.compile(r" \((\d+) syllables\)$")

        for line in haiku_lines:
            match = syllable_pattern.match(line) or empty_line_pattern.match(line)
            self.assertIsNotNone(match, f"Line '{line}' does not match expected format.")
            if match:
                syllable_count = int(match.group(1))
                self.assertGreaterEqual(syllable_count, 0)

if __name__ == '__main__':
    unittest.main()

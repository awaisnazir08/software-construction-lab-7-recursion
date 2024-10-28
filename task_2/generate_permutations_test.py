import unittest
from itertools import permutations as itertools_permutations
from generate_permutations import (
    generate_permutations_recursive, 
    generate_unique_permutations, 
    generate_permutations_non_recursive
)

class TestStringPermutations(unittest.TestCase):

    def test_single_character(self):
        """Test with a single-character string."""
        result = generate_permutations_recursive("a")
        self.assertEqual(result, ["a"])

    def test_two_characters(self):
        """Test with a two-character string."""
        result = generate_permutations_recursive("ab")
        expected = ["ab", "ba"]
        self.assertCountEqual(result, expected)

    def test_duplicate_characters(self):
        """Test with duplicate characters and ensure unique permutations."""
        result = generate_unique_permutations("aab")
        expected = ["aab", "aba", "baa"]
        self.assertCountEqual(result, expected)

    def test_empty_string(self):
        """Test with an empty string."""
        result = generate_permutations_recursive("")
        self.assertEqual(result, "")  # Empty string should yield a single empty result

    def test_recursive_vs_non_recursive(self):
        """Compare recursive and non-recursive results for correctness."""
        input_string = "abc"
        recursive_result = generate_permutations_recursive(input_string)
        non_recursive_result = generate_permutations_non_recursive(input_string)
        self.assertCountEqual(recursive_result, non_recursive_result)

    def test_permutations_with_non_recursive(self):
        """Test non-recursive implementation for correct permutations."""
        result = generate_permutations_non_recursive("ab")
        expected = ["ab", "ba"]
        self.assertCountEqual(result, expected)

    def test_duplicate_permutations_exclusion(self):
        """Ensure unique permutations when duplicates are present."""
        result = generate_unique_permutations("aaa")
        self.assertEqual(result, ["aaa"])  # Only one unique permutation for "aaa"

    def test_long_string_performance(self):
        """Test performance for a longer string."""
        input_string = "abcd"
        with self.assertRaises(RecursionError):
            generate_permutations_recursive("a" * 1000)  # Large input to test recursion depth handling

if __name__ == "__main__":
    unittest.main()

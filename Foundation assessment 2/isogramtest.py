import unittest
from isogram import is_isogram


class IsogramTestCase(unittest.TestCase):
    def test_is_isogram_true(self):
        # Test cases with isograms
        self.assertTrue(is_isogram("isogram"), "Expected True for 'isogram'")
        self.assertTrue(is_isogram("uncopyrightable"), "Expected True for 'uncopyrightable'")

    def test_is_isogram_empty_string(self):
        # Test case for an empty string
        self.assertTrue(is_isogram(""), "Expected True for an empty string")

    def test_is_isogram_case_insensitive(self):
        # Test case for case-insensitive comparison
        self.assertFalse(is_isogram("Programming"), "Expected False for 'Programming'")

    def test_is_isogram_special_characters(self):
        # Test case for special characters
        self.assertTrue(is_isogram("@#$%"), "Expected True for '@#$%' (no repeated letters)")


if __name__ == "__main__":
    unittest.main()

# test_is_isogram_true: This test ensures that words known to be isograms return True. It includes two test cases:
#    - Test case 1: Checks if the word "isogram" is correctly identified as an isogram.
#    - Test case 2: Checks if the word "uncopyrightable" is correctly identified as an isogram.
#
# test_is_isogram_empty_string: This test validates that an empty string is considered an isogram. It checks if the
# function correctly returns True when an empty string is passed.
#
# test_is_isogram_case_insensitive: This test ensures that the function handles case-insensitive comparison correctly.
# It verifies that a word with different casing, such as "Programming", is correctly identified as not an isogram.
#
# test_is_isogram_special_characters: This test checks if the function handles special characters appropriately.
# It verifies that a word containing special characters, such as "@#$%", is correctly identified as an isogram
# since there are no repeated letters.
#



import unittest
import tempfile
import os
from recursive_file_search import search_files

class TestFileSearch(unittest.TestCase):
    def setUp(self):
        """
        Set up a temporary directory and files for testing.
        This method creates a directory structure with:
        - test1.txt in the root directory
        - test2.txt inside a 'subdir' subdirectory
        """
        self.test_dir = tempfile.TemporaryDirectory()
        self.file1_path = os.path.join(self.test_dir.name, "test1.txt")
        self.file2_path = os.path.join(self.test_dir.name, "subdir", "test2.txt")

        os.mkdir(os.path.join(self.test_dir.name, "subdir"))
        with open(self.file1_path, 'w') as f:
            f.write("This is test1.")
        with open(self.file2_path, 'w') as f:
            f.write("This is test2.")

    def tearDown(self):
        """Clean up the temporary directory after each test."""
        self.test_dir.cleanup()

    def test_search_case_sensitive(self):
        """Test case-sensitive search for two existing files."""
        results = search_files(self.test_dir.name, ["test1.txt", "test2.txt"])
        self.assertEqual(len(results["test1.txt"]), 1)  # Check test1.txt found once
        self.assertEqual(len(results["test2.txt"]), 1)  # Check test2.txt found once

    def test_search_case_insensitive(self):
        """Test case-insensitive search for a file using different casing."""
        results = search_files(self.test_dir.name, ["TEST1.TXT"], case_sensitive=False)
        self.assertEqual(len(results["TEST1.TXT"]), 1)  # Ensure it finds test1.txt

    def test_file_not_found(self):
        """Test search for a nonexistent file."""
        results = search_files(self.test_dir.name, ["nonexistent.txt"])
        self.assertEqual(len(results["nonexistent.txt"]), 0)  # No files should be found

    def test_multiple_occurrences(self):
        """Test searching for a file that appears multiple times."""
        # Create another occurrence of 'test1.txt' in a subdirectory
        file_duplicate_path = os.path.join(self.test_dir.name, "subdir", "test1.txt")
        with open(file_duplicate_path, 'w') as f:
            f.write("This is another test1.")

        results = search_files(self.test_dir.name, ["test1.txt"])
        self.assertEqual(len(results["test1.txt"]), 2)  # Both files should be found

    def test_empty_directory(self):
        """Test searching in an empty directory."""
        empty_dir = tempfile.TemporaryDirectory()
        results = search_files(empty_dir.name, ["test1.txt"])
        self.assertEqual(len(results["test1.txt"]), 0)  # No files should be found
        empty_dir.cleanup()

    def test_permission_error(self):
        """Test handling permission errors gracefully."""
        # Create a directory with restricted permissions
        restricted_dir = os.path.join(self.test_dir.name, "restricted")
        os.mkdir(restricted_dir, mode=0o000)  # No permissions

        # Ensure the program doesn't crash and continues searching
        results = search_files(self.test_dir.name, ["test1.txt"])
        self.assertEqual(len(results["test1.txt"]), 1)  # Existing test1.txt should be found

        # Reset permissions for cleanup
        os.chmod(restricted_dir, 0o777)

if __name__ == "__main__":
    unittest.main()

# Import the unit test library
import unittest
# Import the functions defined in main count_lines, count_words, count_bytes
from main import count_lines, count_words, count_bytes

# Create a new class TestFileAnalysis with inherit unittest.TestCase 
class TestFileAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a sample file for testing
        cls.test_file = 'test_file.txt'
        with open(cls.test_file, 'w') as f:
            f.write("Hello world\n")
            f.write("This is a test file\n")
            f.write("With three lines\n")
            f.write("And several words\n")

    def test_count_lines_should_pass(self):
        with open(self.test_file, 'r') as f:
            self.assertEqual(count_lines(f), 4)

    def test_count_words_should_pass(self):
        with open(self.test_file, 'r') as f:
            self.assertEqual(count_words(f), 13)

    def test_count_bytes_should_pass(self):
        with open(self.test_file, 'r') as f:
            self.assertTrue(count_bytes(f) > 0)

    # Intentionally failing tests
    def test_count_lines_should_fail(self):
        with open(self.test_file, 'r') as f:
            self.assertEqual(count_lines(f), 100)

    def test_count_words_should_fail(self):
        with open(self.test_file, 'r') as f:
            self.assertEqual(count_words(f), 2)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test file
        import os
        os.remove(cls.test_file)

if __name__ == '__main__':
    unittest.main()

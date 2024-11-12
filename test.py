import unittest
from main import add_numbers, subtract_numbers

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        """Test addition function."""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        """Test subtraction function."""
        self.assertEqual(subtract_numbers(10, 4), 6)
        self.assertEqual(subtract_numbers(5, 7), -2)
        self.assertEqual(subtract_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

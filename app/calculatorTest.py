import unittest
import sys
from io import StringIO
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.old_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_addition(self):
        # Simulate user input
        sys.stdin = StringIO("1\n5\n3\n")
        result = calculator()
        self.assertEqual(result, 8)

    def test_subtraction(self):
        sys.stdin = StringIO("2\n10\n4\n")
        result = calculator()
        self.assertEqual(result, 6)

    def test_multiplication(self):
        sys.stdin = StringIO("3\n6\n7\n")
        result = calculator()
        self.assertEqual(result, 42)

    def test_division(self):
        sys.stdin = StringIO("4\n15\n3\n")
        result = calculator()
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        sys.stdin = StringIO("4\n10\n0\n")
        result = calculator()
        self.assertIsNone(result)
        self.assertIn("Cannot divide by zero", self.held_output.getvalue())

    def test_invalid_choice(self):
        sys.stdin = StringIO("5\n")
        with self.assertRaises(ValueError):
            calculator()
        self.assertIn("Invalid choice", self.held_output.getvalue())

    def test_invalid_number_input(self):
        sys.stdin = StringIO("1\nabc\n5\n")
        with self.assertRaises(ValueError):
            calculator()
        self.assertIn("Invalid input", self.held_output.getvalue())

if __name__ == '__main__':
    unittest.main()

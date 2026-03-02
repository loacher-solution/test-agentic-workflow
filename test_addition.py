"""
Tests for the 1+1=x solver.
"""
import unittest
from addition import solve_addition


class TestAddition(unittest.TestCase):
    def test_one_plus_one_equals_two(self):
        """1 + 1 = x should resolve x to 2 (the correct sum)."""
        result = solve_addition(1, 1)
        self.assertEqual(result, 2)

    def test_result_is_integer(self):
        """The result of 1+1 should be an integer."""
        result = solve_addition(1, 1)
        self.assertIsInstance(result, int)


if __name__ == "__main__":
    unittest.main()

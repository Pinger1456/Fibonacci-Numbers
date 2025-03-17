"""Test cases for the fibonacci module."""

import unittest
from fibonacci import calculate_fibonacci


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci sequence calculations."""

    def test_fibonacci_1(self):
        """Test the first Fibonacci number."""
        self.assertEqual(calculate_fibonacci(1), 0)

    def test_fibonacci_2(self):
        """Test the second Fibonacci number."""
        self.assertEqual(calculate_fibonacci(2), 1)

    def test_fibonacci_10(self):
        """Test the 10th Fibonacci number."""
        self.assertEqual(calculate_fibonacci(10), 34)


if __name__ == "__main__":
    unittest.main()

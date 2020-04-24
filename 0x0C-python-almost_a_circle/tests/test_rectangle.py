#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""
Test Module for Rectangle class
"""


class TestBase(unittest.TestCase):
    """
    TestBase for Base
    """
    def test_zero(self):
        """
        Tests for rectangle
        """
        if __name__ == "main":
            R = Rectangle(10, 2)
            self.assertEqual(R.id, 1)
            R = Rectangle(2, 10)
            self.assertEqual(R.id, 2)
            R = Rectangle(10, 2, 0, 0, 12)
            self.assertEqual(R.id, 12)
            R = Rectangle(-2, 1)
            self.assertEqual(R.id, 3)

    def test_two(self):
        """
        Second round of tests
        """
        with self.assertRaises(TypeError):
            R1 = Rectangle(10, "2")

        with self.assertRaises(ValueError):
            R1 = Rectangle(0, 3)

        with self.assertRaises(ValueError):
            R1 = Rectangle(-5, 6)

        with self.assertRaises(ValueError):
            R1 = Rectangle(2, -5)

        with self.assertRaises(TypeError):
            R1 = Rectangle("2", 3)

        with self.assertRaises(ValueError):
            R1 = Rectangle(5, 10, 0, -9)

        with self.assertRaises(ValueError):
            R1 = Rectangle(5, 10, -3, 5)

        with self.assertRaises(TypeError):
            R1 = Rectangle(5, 10, "hello", 2)

        with self.assertRaises(TypeError):
            R2 = Rectangle(5, 10, 2, "helloe")

        R1 = Rectangle(5, 10, 0, 2, 3)
        self.assertEqual(R1.id, 3)

        with self.assertRaises(TypeError):
            R1 = Rectangle()


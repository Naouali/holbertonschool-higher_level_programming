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

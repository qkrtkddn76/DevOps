import unittest
from unittest import result
import calc


class test_calc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(10, calc.sum(3, 7))

    def test_minus(self):
        self.assertEqual(5, calc.minus(10, 5))

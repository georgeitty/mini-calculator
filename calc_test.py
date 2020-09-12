import unittest
from calc import *

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(add(2, 2), 4)
        self.assertAlmostEqual(add(6, 3), 9)
        self.assertAlmostEqual(add(3, 3), 6)

    def test_sub(self):
        self.assertAlmostEqual(sub(2, 2), 0)
        self.assertAlmostEqual(sub(6, 3), 3)
        self.assertAlmostEqual(sub(3, 3), 0)

    def test_mult(self):
        self.assertAlmostEqual(mult(2, 2), 4)
        self.assertAlmostEqual(mult(6, 3), 18)
        self.assertAlmostEqual(mult(3, 3), 9)

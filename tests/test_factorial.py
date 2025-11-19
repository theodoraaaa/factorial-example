import unittest
from mymath.factorial import factorial


class TestFactorialFunctions(unittest.TestCase):

    def test_5(self):
        self.assertEqual(factorial(5), 120)

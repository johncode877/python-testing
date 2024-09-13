import unittest
from src.calculator import *
# from src.calculator import sum, substract

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
      assert sum(2,3) == 5

    def test_substract(self):
      assert substract(18,5) == 13

    def test_multiply(self):
      assert multiply(2,5) == 10
 
    def test_division_divisor_non_zero(self):
      assert division(12,3) == 4

    def test_division_divisor_zero(self):
       with self.assertRaises(ValueError): 
         division(3,0)


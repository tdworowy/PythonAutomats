import time
import unittest

from Calculator.Elements.TestBase import CalculatorBase
from Utils.decorators import catch_assertion


class CalculatorTests(CalculatorBase):
    @catch_assertion
    def test_open_scientific_calculator(self):
        self.calculator.openCalculator()
        time.sleep(1)
        self.assertTrue(self.calculator.scientificCalculatorCheck())

    @catch_assertion
    def test_scientific_calculator_sum_1(self):
        self.calculator.openCalculator()
        time.sleep(1)
        self.calculator.sum(2, 2)
        self.assertEqual(self.calculator.getCalcResult(), "4.")

    @catch_assertion
    def test_scientific_calculator_sum_2(self):
        self.calculator.openCalculator()
        time.sleep(1)
        self.calculator.sum(-2, 2)
        self.assertEqual(self.calculator.getCalcResult(), "0.")

    @catch_assertion
    def test_scientific_calculator_sum_3(self):
        self.calculator.openCalculator()
        time.sleep(1)
        self.calculator.bigSum(1000, 1000)
        self.assertEqual(self.calculator.getCalcResult(), "2000.")


if __name__ == '__main__':
    test_program = unittest.main()

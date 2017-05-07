import time
import unittest

from Calculator.Elements.TestBase import CalculatorBase
from Utils.decorators import catchAssertion


class CalculatorTests(CalculatorBase):

    @catchAssertion
    def testOpenScientificCalculator(self):
        self.calculator.openCalculator()
        time.sleep(1)
        self.assertTrue(self.calculator.scientificCalculatorCheck())

    @catchAssertion
    def testScientificCalculatorSum1(self):
         self.calculator.openCalculator()
         time.sleep(1)
         self.calculator.sum(2, 2)
         self.assertEqual(self.calculator.getCalcResult(),"4.")

    @catchAssertion
    def testScientificCalculatorSum2(self):
         self.calculator.openCalculator()
         time.sleep(1)
         self.calculator.sum(-2, 2)
         self.assertEqual(self.calculator.getCalcResult(), "0.")

    @catchAssertion
    def testScientificCalculatorSum3(self):
         self.calculator.openCalculator()
         time.sleep(1)
         self.calculator.bigSum(1000, 1000)
         self.assertEqual(self.calculator.getCalcResult(), "2000.")


if __name__ == '__main__':
    test_program = unittest.main()

import time
import unittest

from Calculator.Elements.TestBase import CalculatorBase
from Utils.utils import logResult


class CalculatorTests(CalculatorBase):


    def testOpenScientificCalculator(self):
        try:
            self.calculator.openCalculator()
            time.sleep(1)
            self.assertTrue(self.calculator.scientificCalculatorCheck())
            logResult("testOpenScientificCalculator", "Pass")
        except AssertionError:
            logResult("testOpenScientificCalculator", "Fail")
            self.fail("fail")

    def testScientificCalculatorSum1(self):
        try:
            self.calculator.openCalculator()
            time.sleep(1)
            self.assertTrue((self.calculator.sum(2, 2, 4)))
            logResult("testScientificCalculatorSum1", "Pass")
        except AssertionError:
            logResult("testScientificCalculatorSum1", "Fail")
            self.fail("fail")

    def testScientificCalculatorSum2(self):
        try:
            self.calculator.openCalculator()
            time.sleep(1)
            self.assertTrue((self.calculator.sum(-2, 2, 0)))
            logResult("testScientificCalculatorSum2", "Pass")
        except AssertionError:
            logResult("testScientificCalculatorSum2", "Fail")
            self.fail("fail")

    def testScientificCalculatorSum3(self):
        try:
            self.calculator.openCalculator()
            time.sleep(1)
            self.assertTrue((self.calculator.bigSum(1000, 1000, 2000)))
            logResult("testScientificCalculatorSum3", "Pass")
        except AssertionError:
            logResult("testScientificCalculatorSum3", "Fail")
            self.fail("fail")


if __name__ == '__main__':
    test_program = unittest.main()

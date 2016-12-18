import time

from Calculator.Elements.TestBase import CalculatorBase


class CalculatorTests(CalculatorBase):


    def testOpenScientificCalculator(self):
        self.calculator.openCalculator().click()
        time.sleep(1)
        self.assertTrue(self.calculator.scientificCalculator().is_displayed())

    def testScientificCalculatorSum1(self):
        self.calculator.openCalculator().click()
        time.sleep(1)
        self.assertTrue((self.calculator.sum(2, 2, 4)))

    def testScientificCalculatorSum2(self):
        self.calculator.openCalculator().click()
        time.sleep(1)
        self.assertTrue((self.calculator.sum(-2, 2, 0)))

    def testScientificCalculatorSum3(self):
        self.calculator.openCalculator().click()
        time.sleep(1)
        self.assertTrue((self.calculator.bigSum(1000, 1000, 2000)))


import unittest

import time

from Elements.CalculatorElements import CalculatorElements
from selenium import webdriver


class CalculatorTests(unittest.TestCase):
    driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get('http://www.calculator.net/')
        self.calculator = CalculatorElements(self.driver)

    def tearDown(self):
        self.driver.quit()


    def testOpenScientificCalculator(self):
        self.calculator.openCalculator().click()
        time.sleep(5)
        assert self.calculator.scientificCalculator().is_displayed()


    def testScientificCalculatorSum1(self):
        self.calculator.openCalculator().click()
        time.sleep(5)
        self.calculator.numberButton(2).click()
        self.calculator.plusButton().click()
        self.calculator.numberButton(2).click()
        self.calculator.equalButton().click()
        self.assertEqual (self.calculator.result().text, '4.')
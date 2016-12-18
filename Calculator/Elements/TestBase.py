import unittest

from selenium import webdriver

from Calculator.Elements.Calculator import CalculatorElements

class CalculatorBase(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.calculator.net/')
        self.calculator = CalculatorElements(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
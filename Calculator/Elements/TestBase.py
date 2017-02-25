import unittest

from selenium import webdriver

from Calculator.Elements.Calculator import CalculatorElements
from chromedriverFolder.driverPath import getDriverPath


class CalculatorBase(unittest.TestCase):


    def setUp(self):
        chromeDriverPath = getDriverPath()+ '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        self.driver.get('http://www.calculator.net/')
        self.calculator = CalculatorElements(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
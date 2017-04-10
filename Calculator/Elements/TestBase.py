import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

from Calculator.Elements.Calculator import CalculatorElements
from chromedriverFolder.driverPath import getDriverPath

server = 'http://www.calculator.net/'

class CalculatorBase(unittest.TestCase):

    remote = False

    def setUp(self):
        if(self.remote):
            # self.driver = WebDriver("http://localhost:4444/wd/hub", "chrome", "ANY")
            self.driver = WebDriver("http://localhost:4444", DesiredCapabilities.CHROME)
        else:
            chromeDriverPath = getDriverPath()+ '\\chromedriver.exe'
            self.driver = webdriver.Chrome(chromeDriverPath)
        self.driver.get(server)
        self.calculator = CalculatorElements(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)



    def tearDown(self):
        self.driver.quit()


    # def remoteDriver(self):
    #   return  webdriver.Remote(
    #         command_executor=server,
    #         desired_capabilities={
    #             "browserName": "chrome",
    #             "version": "56",
    #             "video": "false",
    #             "platform": "Windows 10",
    #             "marionette": "false",
    #         })



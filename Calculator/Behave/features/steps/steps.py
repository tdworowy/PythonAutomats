import time

from behave import *
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from Calculator.Elements.Calculator import CalculatorElements
from Utils.utils import log
from chromedriverFolder.driverPath import getDriverPath

server = 'http://www.calculator.net/'
chrome = {
        "browserName": "chrome",
        "version": "58",
        "platform": "ANY"
    }

@given('set up')
def setUp(context):
            remote = False
            if (remote):
                # self.driver = WebDriver("http://localhost:4444/wd/hub", "chrome", "ANY")
              # context.driver = WebDriver("http://192.168.99.100:5000", DesiredCapabilities.CHROME)
              #   context.driver = WebDriver(command_executor="http://192.168.99.100:5000/wd/hub", desired_capabilities=DesiredCapabilities.CHROME,proxy=None)
              #   options = webdriver.ChromeOptions
                context.driver = WebDriver(command_executor="http://192.168.99.100:5000/wd/hub",desired_capabilities=chrome)
                # context.driver = webdriver.Remote(
                #     command_executor='http://192.168.99.100:5000/wd/hub',
                #     desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
                # don't work becouse grid bug
            else:
                chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
                context.driver = webdriver.Chrome(chromeDriverPath)
            context.driver.get(server)
            context.calculator = CalculatorElements(context.driver)
           # context.driver.maximize_window()
            context.driver.implicitly_wait(10)
#
# def setDriver(context):
#     context.driver = driver



def getURL(context):
    return context.driver.current_url



# def tearDown(context):
#     context.driver.quit()
def tearDown(context):
    context.driver.quit()

@given('open scientific calculator')
def openscientificCalculator(context):
        context.calculator.openCalculator()
        context.open =context.calculator.scientificCalculatorCheck()
        time.sleep(1)

@when('sum 2 + 2')
def sum1(context):
    context.sum = context.calculator.sum(2, 2)
    context.result = "4."

@when('sum -2 + 2')
def sum2(context):
    context.sum = context.calculator.sum(-2, 2)
    context.result = "0."


@when('sum 1000 + 1000')
def sum3(context):
    context.calculator.bigSum(1000,1000)
    context.result = "2000."


@when('sum {sum}')
def sumP(context,sum):
    ele = sum.split(',')
    x =int(ele[0])
    y =int(ele[1])
    context.calculator.bigSum(x, y)

@then('check calculator')
def checkifCalculatorIsDisplayed(context):
    assert context.open is True

@then('check result')
def checkResult(context):
    actual = context.calculator.getCalcResult()
    log("Check result: " + context.result,context.logFile)
    log("Actual result: " + actual,context.logFile)
    assert context.result == context.calculator.getCalcResult()

@then('check {result}')
def checkResult2(context,result):
    actual = context.calculator.getCalcResult()
    log("Check result: " + result,context.logFile)
    log("Actual result: " + actual,context.logFile)
    assert result == context.calculator.getCalcResult()




import time

from behave import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.remote.webdriver import WebDriver

from Calculator.Elements.Calculator import CalculatorElements
from chromedriverFolder.driverPath import getDriverPath

server = 'http://www.calculator.net/'
@given('set up')
def SetUp(context):
            remote = False
            if (remote):
                # self.driver = WebDriver("http://localhost:4444/wd/hub", "chrome", "ANY")
                context.driver = WebDriver("http://localhost:4444", DesiredCapabilities.CHROME)
            else:
                chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
                context.driver = webdriver.Chrome(chromeDriverPath)
            context.driver.get(server)
            context.calculator = CalculatorElements(context.driver)
            context.driver.maximize_window()
            context.driver.implicitly_wait(10)

def tearDown(context):
        context.driver.quit()

@given('open scientific calculator')
def openscientificCalculator(context):
        context.calculator.openCalculator()
        context.open =context.calculator.scientificCalculatorCheck()
        time.sleep(1)

@when('sum 2 + 2')
def sum1(context):
    context.sum = context.calculator.sum(2, 2, 4)

@when('sum -2 + 2')
def sum2(context):
    context.sum = context.calculator.sum(-2, 2, 0)

@when('sum 1000 + 1000')
def sum3(context):
    context.sum = context.calculator.bigSum(1000,1000, 2000)


@when('sum {sum}')
def sumP(context,sum):
    ele = sum.split(',')
    x =int(ele[0])
    y =int(ele[1])

    context.resoult= x + y
    context.calculator.bigSum(x, y, context.resoult)


@then('check calculator')
def checkifCalculatorIsDisplayed(context):
    assert context.open is True

@then('check result')
def checkResult(context):
    assert context.sum is True

@then('check {result}')
def checkResult2(context,result):
    assert context.resoult is result




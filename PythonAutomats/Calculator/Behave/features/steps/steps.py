import time

from Calculator.Elements.Calculator import CalculatorElements
from Chrome_Driver_Folder.driver_path import get_driver_path
from Utils.utils import MyLogging
from behave import *
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

SERVER = 'http://www.calculator.net/'
CHROME = {
    "browserName": "chrome",
    "version": "58",
    "platform": "ANY"
}


@given('set up')
def set_up(context):
    context.my_loggin = MyLogging()
    remote = False
    if remote:
        # self.driver = WebDriver("http://localhost:4444/wd/hub", "chrome", "ANY")
        # context.driver = WebDriver("http://192.168.99.100:5000", DesiredCapabilities.CHROME)
        #   context.driver = WebDriver(command_executor="http://192.168.99.100:5000/wd/hub", desired_capabilities=DesiredCapabilities.CHROME,proxy=None)
        #   options = webdriver.ChromeOptions
        context.driver = WebDriver(command_executor="http://192.168.99.100:5000/wd/hub", desired_capabilities=CHROME)
        # context.driver = webdriver.Remote(
        #     command_executor='http://192.168.99.100:5000/wd/hub',
        #     desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
        # don't work becouse grid bug
    else:
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        context.driver = webdriver.Chrome(chrome_driver_path)
    context.driver.get(SERVER)
    context.calculator = CalculatorElements(context.driver)
    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)


#
# def setDriver(context):
#     context.driver = driver


def get_url(context):
    return context.driver.current_url


# def tearDown(context):
#     context.driver.quit()
def tear_down(context):
    context.driver.quit()


@given('open scientific calculator')
def open_scientific_calculator(context):
    context.calculator.open_calculator()
    context.open = context.calculator.scientific_calculator_check()
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
    context.calculator.big_sum(1000, 1000)
    context.result = "2000."


@when('sum {sum}')
def parametrized_sum(context, sum):
    ele = sum.split(',')
    x = int(ele[0])
    y = int(ele[1])
    context.calculator.big_sum(x, y)


@then('check calculator')
def check_if_calculator_is_displayed(context):
    assert context.open is True


@then('check result')
def check_result(context):
    actual = context.calculator.get_calc_result()
    context.my_loggin.log(context.logFile).info("Check result: " + context.result)
    context.my_loggin.log(context.logFile).info("Actual result: " + actual)
    assert context.result == context.calculator.get_calc_result()


@then('check {result}')
def parametrized_check_result(context, result):
    actual = context.calculator.get_calc_result()
    context.my_loggin.log(context.logFile).info("Check result: " + result)
    context.my_loggin.log(context.logFile).info("Actual result: " + actual)
    assert result == context.calculator.get_calc_result()

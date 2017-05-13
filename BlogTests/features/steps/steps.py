from behave import *

from BlogTests.screens.screenPath import getScreenPath


def takeScreenshot(context,file):
    context.driver.save_screenshot(getScreenPath()+"//"+file.replace(' ','_')+'.png')

def getURL(context):
    return context.driver.current_url

def tearDown(context):
    tearDown(context)

@given('login page is opened')
def checkLoginPage(context):
        context.loginPage.checkIFLoginPageIsOpen()

@when('login admin')
def loginAdmin(context):
    context.loginPage.logIn("admin","AdminPass123")

@then('admin page is opened')
def checkAdminPage(context):
    context.adminPage.chakIFPageOpened()









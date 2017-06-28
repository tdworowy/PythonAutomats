from behave import *

from BlogTests.Pages.basePage import setUp

loginPage = "http://localhost:8081/admin/login/"
blogPage = "http://localhost:8081/blog/"


adminLogin = "admin"
adminPass = "AdminPass123"


def getURL(context):
    return context.driver.current_url


@given("open login page")
def openLoginPage(context):
    setUp(context,loginPage)

@given("open blog page")
def openLoginPage(context):
    setUp(context,loginPage)


@then('login page is opened')
def checkLoginPage(context):
        context.loginPage.checkIFLoginPageIsOpen()

@when('login admin')
def loginAdmin(context):
    context.loginPage.logIn(adminLogin,adminPass)

@then('admin page is opened')
def checkAdminPage(context):
    context.adminPage.chakIFPageOpened()









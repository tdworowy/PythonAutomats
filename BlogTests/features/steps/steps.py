from behave import *

from BlogTests.Pages.basePage import setUp
from BlogTests.dataModels.PostModel import POST

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
    setUp(context,blogPage)


@then('login page is opened')
def checkLoginPage(context):
        context.loginPage.checkIFLoginPageIsOpen()

@when('login admin')
def loginAdmin(context):
    context.loginPage.login(adminLogin, adminPass)

@then('admin page is opened')
def checkAdminPage(context):
    context.adminPage.chakIFPageOpened()


@when('add Post {title} {body}')
def addPost(context,title,body):
    import time
    ms = time.time() * 1000.0

    context.post = POST(title+"_"+str(ms),body,"TestTag","1",True) # 1 means admin
    context.adminPage.addPost(context.post)

@when('open Last post')
def openLastPost(context):
    context.postPage = context.blogPage.openLatestPost()

@then('check post')
def checkPost(context):
    context.postPage.checkPost(context.post)









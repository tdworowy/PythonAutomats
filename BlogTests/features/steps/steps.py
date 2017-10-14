from BlogTests.Pages.basePage import set_up
from BlogTests.dataModels.PostModel import POST
from behave import *

loginPage = "http://localhost:8081/admin/login/"
blogPage = "http://localhost:8081/blog/"

adminLogin = "admin"
adminPass = "AdminPass123"


def get_url(context):
    return context.driver.current_url


@given("open login page")
def open_login_page(context):
    set_up(context, loginPage)


@given("open blog page")
def open_blog_page(context):
    set_up(context, blogPage)


@then('login page is opened')
def check_login_page(context):
    context.loginPage.check_if_login_page_is_open()


@when('login admin')
def login_admin(context):
    context.loginPage.login(adminLogin, adminPass)


@then('admin page is opened')
def check_admin_page(context):
    context.adminPage.check_if_page_opened()


@when('add Post {title} {body}')
def add_post(context, title, body):
    import time
    ms = time.time() * 1000.0

    context.post = POST(title + "_" + str(ms), body, "TestTag", "1", True)  # 1 means admin
    context.adminPage.add_post(context.post)


@when('open Last post')
def open_last_post(context):
    context.postPage = context.blogPage.open_latest_post()


@then('check post')
def check_post(context):
    context.postPage.check_post(context.post)

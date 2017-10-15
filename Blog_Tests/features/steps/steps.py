from behave import *

from Blog_Tests.Pages.base_page import set_up
from Blog_Tests.dataModels.postmodel import POST

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
    context.login_page.check_if_login_page_is_open()


@when('login admin')
def login_admin(context):
    context.login_page.login(adminLogin, adminPass)


@then('admin page is opened')
def check_admin_page(context):
    context.admin_page.check_if_page_opened()


@when('add Post {title} {body}')
def add_post(context, title, body):
    import time
    ms = time.time() * 1000.0

    context.post = POST(title + "_" + str(ms), body, "TestTag", "1", True)  # 1 means admin
    context.admin_page.add_post(context.post)


@when('open Last post')
def open_last_post(context):
    context.post_page = context.blog_page.open_latest_post()


@then('check post')
def check_post(context):
    context.post_page.check_post(context.post)

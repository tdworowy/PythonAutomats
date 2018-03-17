from Blog_Tests.Pages.base_page import set_up
from Blog_Tests.dataModels.postmodel import POST
from behave import *

PORT = 8083
LOGIN_PAGE_URL = "http://localhost:%s/admin/login/" % str(PORT)
BLOG_PAGE_URL = "http://localhost:%s/blog/" % str(PORT)

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "AdminPass123"


def get_url(context):
    return context.driver.current_url


@given("open login page")
def open_login_page(context):
    set_up(context, LOGIN_PAGE_URL)


@given("open blog page")
def open_blog_page(context):
    set_up(context, BLOG_PAGE_URL)


@then('login page is opened')
def check_login_page(context):
    context.login_page.check_if_login_page_is_open()


@when('login admin')
def login_admin(context):
    context.login_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)


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

from Blog_Tests.Pages.base_page import set_up, open_page
from Blog_Tests.dataModels.postmodel import POST
from behave import *

PORT = 8083
LOGIN_PAGE_URL = "http://localhost:%s/admin/login/" % str(PORT)
BLOG_PAGE_URL = "http://localhost:%s/blog/" % str(PORT)

ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "AdminPass123"


def get_url(context):
    return context.driver.current_url


@given("open blog page")
def open_blog_page(context):
    open_page(context, BLOG_PAGE_URL)


@given('user is logged as Admin')
def login_admin(context):
    set_up(context, LOGIN_PAGE_URL)
    context.login_page.check_if_login_page_is_open()
    context.login_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)
    context.admin_page.check_if_page_opened()


@Given('user is on Login Page')
def check_login_page(context):
    set_up(context, LOGIN_PAGE_URL)
    context.login_page.check_if_login_page_is_open()


@when('user login in as admin')
def login_as_admin(context):
    context.login_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)


@when('user adds Post {title} {body}')
def add_post(context, title, body):
    import time
    ms = time.time() * 1000.0

    context.post = POST(title + "_" + str(ms), body, "TestTag", "1", True)  # 1 means admin
    context.admin_page.add_post(context.post)


@Then('admin page is opened')
def admin_page_is_opened(context):
    context.admin_page.check_if_page_opened()


@then('post is displayed on main page')
def check_post(context):
    open_blog_page(context)
    context.post_page = context.blog_page.open_latest_post()
    context.post_page.check_post(context.post)

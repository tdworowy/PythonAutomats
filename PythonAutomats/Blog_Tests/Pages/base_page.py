from Blog_Tests.Pages.admin_page import AdminPage
from Blog_Tests.Pages.blog_page import BlogPage
from Blog_Tests.Pages.login_page import LoginPage
from Chrome_Driver_Folder.driver_path import get_driver_path
from selenium import webdriver


def set_up(context, server):
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    context.driver = webdriver.Chrome(chrome_driver_path)
    context.driver.get(server)
    context.driver.implicitly_wait(1)
    context.login_page = LoginPage(context.driver)
    context.admin_page = AdminPage(context.driver)
    context.blog_page = BlogPage(context.driver)


def open_page(context, server):
    context.driver.get(server)
    context.driver.implicitly_wait(1)


def tear_down(context):
    context.driver.quit()

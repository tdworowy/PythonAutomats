from BlogTests.Pages.adminPage import AdminPage
from BlogTests.Pages.blogPage import BlogPage
from BlogTests.Pages.loginPage import LoginPage
from ChromedriverFolder.driverPath import get_driver_path
from selenium import webdriver


def set_up(context, server):
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    context.driver = webdriver.Chrome(chrome_driver_path)
    context.driver.get(server)
    context.driver.implicitly_wait(1)
    context.login_page = LoginPage(context.driver)
    context.admin_page = AdminPage(context.driver)
    context.blog_page = BlogPage(context.driver)


def tear_down(context):
    context.driver.quit()

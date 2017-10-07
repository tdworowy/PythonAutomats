from selenium import webdriver

from BlogTests.Pages.adminPage import AdminPage
from BlogTests.Pages.blogPage import BlogPage
from BlogTests.Pages.loginPage import LoginPage
from ChromedriverFolder.driverPath import get_driver_path


def setUp(context,server):
    chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
    context.driver = webdriver.Chrome(chromeDriverPath)
    context.driver.get(server)
    context.driver.implicitly_wait(1)
    context.loginPage = LoginPage(context.driver)
    context.adminPage = AdminPage(context.driver)
    context.blogPage = BlogPage(context.driver)


def tearDown(context):
    context.driver.quit()
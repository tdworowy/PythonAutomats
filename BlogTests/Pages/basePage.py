from BlogTests.Pages.adminPage import AdminPage
from BlogTests.Pages.blogPage import BlogPage
from BlogTests.Pages.loginPage import LoginPage
from ChromedriverFolder.driverPath import getDriverPath
from selenium import webdriver


def setUp(context,server):
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    context.driver = webdriver.Chrome(chromeDriverPath)
    context.driver.get(server)
    context.driver.implicitly_wait(1)
    context.loginPage = LoginPage(context.driver)
    context.adminPage = AdminPage(context.driver)
    context.blogPage = BlogPage(context.driver)


def tearDown(context):
    context.driver.quit()
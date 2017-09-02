from BlogTests.Pages.adminPage import AdminPage
from BlogTests.Pages.loginPage import LoginPage
from ChromedriverFolder.driverPath import getDriverPath
from selenium import webdriver

SERVER = "http://localhost:8081/admin/login/"
def setUp(context,server=SERVER):
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    context.driver = webdriver.Chrome(chromeDriverPath)
    context.driver.get(server)
    context.driver.implicitly_wait(1)
    context.loginPage = LoginPage(context.driver)
    context.adminPage = AdminPage(context.driver)


def tearDown(context):
    context.driver.quit()
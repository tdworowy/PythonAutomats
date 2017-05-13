from selenium.webdriver.common.by import By


class LoginPage:

    def initializeElements(self):
        self.loginImput = (By.NAME, 'username')
        self.passwodrImput = (By.NAME, "password")
        self.LogInButton = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self,driverArg):
        self.initializeElements()
        self.driver = driverArg

    def setLogin(self,login):
        loginImput= self.driver.find_element(*self.loginImput)
        loginImput.click()
        loginImput.send_keys(login)

    def setPassword(self, password):
        passwordImput = self.driver.find_element(*self.passwodrImput)
        passwordImput.click()
        passwordImput.send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(*self.LogInButton).click()


    def logIn(self,login,password):
        self.setLogin(login)
        self.setPassword(password)
        self.clickLoginButton()

    def checkIFLoginPageIsOpen(self):
        assert self.driver.find_element(*self.loginImput).is_displayed()
        assert self.driver.find_element(*self.passwodrImput).is_displayed()
        assert self.driver.find_element(*self.LogInButton).is_displayed()

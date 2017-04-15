import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class skypeBot():
    def initializeElements(self):
        self.loginFB = (By.ID, 'loginWithFacebook')
        self.loginEmail = (By.ID, 'email')
        self.loginPassword = (By.ID, 'pass')
        self.loginButton = (By.ID, 'pass')
        self.inputField = (By.CSS_SELECTOR, "div.input input.inputField.fontSize-h4")

        self.loginSkype = (By.ID, 'username')
        self.loginSkypeButton = (By.ID, 'signIn')
        self.loginSkypePassword = (By.NAME, 'passwd')

        self.group = (By.CLASS_NAME, 'list-selectable')



    def __init__(self,webdriver):
        self.driver= webdriver
        self.initializeElements()



    def sendMessageToSelected(self, message):
        actions = ActionChains(self.driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)

    def sendEnter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()


    def openSkype(self):
        self.driver.get('https://web.skype.com/pl/')

    def waitForInputField(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_any_elements_located(self.inputField))
        time.sleep(1)

    def loginFacebook(self, autentycation):
        self.openSkype()

        loginFB = self.driver.find_element(*self.loginFB)
        loginFB.click()

        loginField = self.driver.find_element(*self.loginEmail)
        loginField.click()
        loginField.send_keys(autentycation[0])

        passField = self.driver.find_element(*self.loginPassword)
        passField.click()
        passField.send_keys(autentycation[1])

        loginButton = self.driver.find_element(*self.loginButton)
        loginButton.click()
        self.waitForInputField()

    def login(self, autentycation):
        self.openSkype()
        loginField = self.driver.find_element(*self.loginSkype)
        loginField.click()
        loginField.send_keys(autentycation[0])

        loginButton = self.driver.find_element(*self.loginSkypeButton)
        loginButton.click()

        passField = self.driver.find_element(*self.loginSkypePassword)
        passField.click()
        passField.send_keys(autentycation[1])

        self.sendEnter()
        self.waitForInputField()

    def select(self, name):
        searchSkype = self.driver.find_element(*self.inputField)
        searchSkype.click()
        time.sleep(1)

        searchSkype.send_keys(name)
        time.sleep(1)
        group = self.driver.find_element(*self.group)
        group.click()
        time.sleep(2)

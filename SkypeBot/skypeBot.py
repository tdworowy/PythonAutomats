import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class skypeBot():
    def __init__(self,webdriver):
        self.driver= webdriver



    def sendMessageToSelected(self, message):
        actions = ActionChains(self.driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)


    def loginFacebook(self, autentycation):
        self.driver.get('https://web.skype.com/pl/')
        self.driver.implicitly_wait(3)
        loginFB = self.driver.find_element_by_id("loginWithFacebook")
        loginFB.click()

        loginField = self.driver.find_element_by_id("email")
        loginField.click()
        loginField.send_keys(autentycation[0])

        passField = self.driver.find_element_by_id("pass")
        passField.click()
        passField.send_keys(autentycation[1])

        loginButton = self.driver.find_element_by_id("loginbutton")
        loginButton.click()
        WebDriverWait(self.driver, 40).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "div.input input.inputField.fontSize-h4")))
        time.sleep(1)

    def select(self, name):
        searchSkype = self.driver.find_element_by_css_selector("div.input input.inputField.fontSize-h4")
        searchSkype.click()
        time.sleep(1)

        searchSkype = self.driver.find_element_by_css_selector("div.input.active input.inputField.fontSize-h4")
        searchSkype.send_keys(name)
        time.sleep(1)
        group = self.driver.find_element_by_class_name("list-selectable")
        group.click()
        time.sleep(2)

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SkypeBot():
    def initialize_elements(self):
        self.loginFB = (By.ID, 'loginWithFacebook')
        self.loginEmail = (By.ID, 'email')
        self.loginPassword = (By.ID, 'pass')
        self.loginButton = (By.ID, 'pass')
        self.inputField = (By.CSS_SELECTOR, "div.input input.inputField.fontSize-h4")

        self.loginSkype = (By.ID, 'username')
        self.loginSkypeButton = (By.ID, 'signIn')
        self.loginSkypePassword = (By.NAME, 'passwd')

        self.group = (By.CLASS_NAME, 'list-selectable')

        self.addPersonButton = (By.CSS_SELECTOR, "button[class=\"btn secondary circle stroke\"]")
        self.addButton = (By.CSS_SELECTOR, "button[aria-label=\"Add\"]")

        self.content = (By.CSS_SELECTOR, "div[class=\"content\"] p")

    def set_search_item(self, user):
        self.searchItem = (By.CSS_SELECTOR, "li[title=\"" + user + "\"")

    def __init__(self, webdriver):
        self.driver = webdriver
        self.initialize_elements()

    def send_message_to_selected(self, message):
        actions = ActionChains(self.driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)

    def send_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def open_skype(self):
        self.driver.get('https://web.Skype.com/pl/')

    def wait_for_input_field(self):
        WebDriverWait(self.driver, 40).until(EC.visibility_of_any_elements_located(self.inputField))
        time.sleep(1)

    def login_facebook(self, authentication):
        self.open_skype()

        loginFB = self.driver.find_element(*self.loginFB)
        loginFB.click()

        loginField = self.driver.find_element(*self.loginEmail)
        loginField.click()
        loginField.send_keys(authentication[0])

        passField = self.driver.find_element(*self.loginPassword)
        passField.click()
        passField.send_keys(authentication[1])

        loginButton = self.driver.find_element(*self.loginButton)
        loginButton.click()
        self.wait_for_input_field()

    def login(self, authentication):
        self.open_skype()
        loginField = self.driver.find_element(*self.loginSkype)
        loginField.click()
        loginField.send_keys(authentication[0])

        loginButton = self.driver.find_element(*self.loginSkypeButton)
        loginButton.click()

        passField = self.driver.find_element(*self.loginSkypePassword)
        passField.click()
        passField.send_keys(authentication[1])

        self.send_enter()
        self.wait_for_input_field()

    def select(self, name):
        searchSkype = self.driver.find_element(*self.inputField)
        searchSkype.click()
        time.sleep(1)

        searchSkype.send_keys(name)
        time.sleep(1)
        group = self.driver.find_element(*self.group)
        group.click()
        time.sleep(2)

    def add_person_button_click(self):
        self.driver.implicitly_wait(5);
        self.driver.find_element(*self.addPersonButton).click()

    def add_button_click(self):
        self.driver.find_element(*self.addButton).click()

    def search_item_click(self, user):
        try:
            self.set_search_item(user)
            self.driver.find_element(*self.searchItem).click()
            self.add_button_click()
        except Exception as ex:
            print(str(ex))
            print(user, " is alredy added")

    def check_content(self, toCheck):  # don't work as should
        try:
            print(self.driver.find_element(*self.content).text)
            if self.driver.find_element(*self.content).text == toCheck:
                return True
            else:
                return False
        except Exception:
            return False

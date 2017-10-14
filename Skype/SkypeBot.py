import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SkypeBot():
    def initialize_elements(self):
        self.login_FB = (By.ID, 'loginWithFacebook')
        self.login_email = (By.ID, 'email')
        self.login_password = (By.ID, 'pass')
        self.login_button = (By.ID, 'pass')
        self.input_field = (By.CSS_SELECTOR, "div.input input.inputField.fontSize-h4")

        self.login_skype = (By.ID, 'username')
        self.login_skype_button = (By.ID, 'signIn')
        self.login_skype_password = (By.NAME, 'passwd')

        self.group = (By.CLASS_NAME, 'list-selectable')

        self.add_person_button = (By.CSS_SELECTOR, "button[class=\"btn secondary circle stroke\"]")
        self.add_button = (By.CSS_SELECTOR, "button[aria-label=\"Add\"]")

        self.content = (By.CSS_SELECTOR, "div[class=\"content\"] p")

    def set_search_item(self, user):
        self.search_item = (By.CSS_SELECTOR, "li[title=\"" + user + "\"")

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
        WebDriverWait(self.driver, 40).until(EC.visibility_of_any_elements_located(self.input_field))
        time.sleep(1)

    def login_facebook(self, authentication):
        self.open_skype()

        login_FB = self.driver.find_element(*self.login_FB)
        login_FB.click()

        login_field = self.driver.find_element(*self.login_email)
        login_field.click()
        login_field.send_keys(authentication[0])

        pass_field = self.driver.find_element(*self.login_password)
        pass_field.click()
        pass_field.send_keys(authentication[1])

        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
        self.wait_for_input_field()

    def login(self, authentication):
        self.open_skype()
        login_field = self.driver.find_element(*self.login_skype)
        login_field.click()
        login_field.send_keys(authentication[0])

        login_button = self.driver.find_element(*self.login_skype_button)
        login_button.click()

        pass_field = self.driver.find_element(*self.login_skype_password)
        pass_field.click()
        pass_field.send_keys(authentication[1])

        self.send_enter()
        self.wait_for_input_field()

    def select(self, name):
        search_skype = self.driver.find_element(*self.input_field)
        search_skype.click()
        time.sleep(1)

        search_skype.send_keys(name)
        time.sleep(1)
        group = self.driver.find_element(*self.group)
        group.click()
        time.sleep(2)

    def add_person_button_click(self):
        self.driver.implicitly_wait(5);
        self.driver.find_element(*self.add_person_button).click()

    def add_button_click(self):
        self.driver.find_element(*self.add_button).click()

    def search_item_click(self, user):
        try:
            self.set_search_item(user)
            self.driver.find_element(*self.search_item).click()
            self.add_button_click()
        except Exception as ex:
            print(str(ex))
            print(user, " is alredy added")

    def check_content(self, to_check):  # don't work as should
        try:
            print(self.driver.find_element(*self.content).text)
            if self.driver.find_element(*self.content).text == to_check:
                return True
            else:
                return False
        except Exception:
            return False

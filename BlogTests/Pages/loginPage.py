from selenium.webdriver.common.by import By


class LoginPage:
    def initialize_elements(self):
        self.login_input = (By.NAME, 'username')
        self.password_input = (By.NAME, "password")
        self.logIn_button = (By.CSS_SELECTOR, "input[type='submit']")

    def __init__(self, driver_arg):
        self.initialize_elements()
        self.driver = driver_arg

    def set_login(self, login):
        login_input = self.driver.find_element(*self.login_input)
        login_input.click()
        login_input.send_keys(login)

    def set_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.click()
        password_input.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.logIn_button).click()

    def login(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.click_login_button()

    def check_if_login_page_is_open(self):
        assert self.driver.find_element(*self.login_input).is_displayed()
        assert self.driver.find_element(*self.password_input).is_displayed()
        assert self.driver.find_element(*self.logIn_button).is_displayed()

from selenium.webdriver.common.by import By


class CalculatorElements:
    def initialize_elements(self):
        self.scientific_calculator_link = (By.LINK_TEXT, "Scientific Calculator")
        self.scientific_calculator = (By.ID, "sciout")
        self.calculator_result = (By.ID, "sciOutPut")
        self.plus_button = (By.CSS_SELECTOR, "span[onclick=\"r('+')\"]")
        self.change_button = (By.CSS_SELECTOR, "span[onclick=\"r('+/-')\"]")
        self.equal_button = (By.CSS_SELECTOR, "span[onclick=\"r('=')\"]")
        self.number_buttons = [
            (By.CSS_SELECTOR, 'span[onclick="r(%s)"]' % number)
            for number in range(0, 10)
        ]

    def __init__(self, driverArg):
        self.driver = driverArg
        self.initialize_elements()

    def open_calculator(self):
        self.driver.find_element(*self.scientific_calculator_link).click()

    def scientific_calculator_check(self):
        return self.driver.find_element(*self.scientific_calculator).is_displayed()

    def get_calc_result(self):
        return self.driver.find_element(*self.calculator_result).text

    def number_button_click(self, number):
        self.driver.find_element(*self.number_buttons[number]).click()

    def plus_button_click(self):
        self.driver.find_element(*self.plus_button).click()

    def change_button_click(self):
        self.driver.find_element(*self.change_button).click()

    def equal_button_click(self):
        self.driver.find_element(*self.equal_button).click()

    def sum(self, num1, num2):
        self.number_button_click(abs(num1))
        if num1 < 0:
            self.change_button_click()

        self.plus_button_click()

        self.number_button_click(abs(num2))
        if num2 < 0:
            self.change_button_click()
        self.equal_button_click()

    def big_sum(self, num1, num2):
        num1_list = list(str(num1))
        num2_list = list(str(num2))
        self.click_numbers(num1_list)
        self.plus_button_click()
        self.click_numbers(num2_list)

        self.equal_button_click()

    def click_numbers(self, num_list):
        for n in num_list:
            self.number_button_click(int(n))

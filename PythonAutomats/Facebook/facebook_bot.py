import os
import time

from Chrome_Driver_Folder.driver_path import get_driver_path
from Utils.enum_ import Enum
from selenium import webdriver

visibilityEnum = Enum(["friends", "public", "me"])


# TODO
class FacebookBot:
    def __init__(self, webdriver):
        self.driver = webdriver
        self.driver.get("https://pl-pl.facebook.com/")

    def login_facebook(self, authentication):
        self.driver.implicitly_wait(3)

        login_field = self.driver.find_element_by_id("email")
        login_field.click()
        login_field.send_keys(authentication[0])

        pass_field = self.driver.find_element_by_id("pass")
        pass_field.click()
        pass_field.send_keys(authentication[1])

        login_button = self.driver.find_element_by_id("loginbutton")
        login_button.click()
        time.sleep(1)

    def set_visibility(self, vis):

        visibility_ = self.driver.find_element_by_class("_55pe")
        visibility_.click()

        more_options = self.driver.find_element_by_class("_54nh _4chm")
        more_options.click()
        if vis is visibilityEnum.friends:
            friends = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Friends')]"
            )
            friends.click()
        if vis is visibilityEnum.public:
            public = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Public')]"
            )
            public.click()
        if vis is visibilityEnum.me:
            onlyMe = self.driver.find_elements_by_xpath(
                "//*[contains(text(), 'Only me')]"
            )
            onlyMe.click()

    def post(self, content, vis):
        post_filed = self.driver.find_element_by_css_selector(
            "div[role='presentation']"
        )
        post_filed.click()
        post_filed.send_keys(content)

        self.set_visibility(vis)

        post_button = self.driver.find_element_by_css_selector(
            "button[data-testid='react-composer-post-button'"
        )
        post_button.click()


if __name__ == "__main__":
    chrome_driver_path = get_driver_path() + "\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.maximize_window()
    driver.implicitly_wait(2)

    fb = FacebookBot(driver)

    f = open(os.path.dirname(os.path.abspath(__file__)) + "\\aut.txt")
    fb.login_facebook((f.readline().strip(), f.readline().strip()))
    fb.post("Test", visibilityEnum.me)

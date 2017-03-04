import time
from enum import Enum


class facebookBot():
    def __init__(self,webdriver):
        self.driver= webdriver

    def loginFacebook(self, autentycation):
        self.driver.get('https://pl-pl.facebook.com/')
        self.driver.implicitly_wait(3)

        loginField = self.driver.find_element_by_id("email")
        loginField.click()
        loginField.send_keys(autentycation[0])

        passField = self.driver.find_element_by_id("pass")
        passField.click()
        passField.send_keys(autentycation[1])

        loginButton = self.driver.find_element_by_id("loginbutton")
        loginButton.click()
        time.sleep(1)

    def visibility(self):
        return Enum("friends",'public','me')

    def post(self, content, vis):
        postFiled = self.driver.find_element_by_css_selector("rov[data-testid='react-composer-root'] div[role='presentation']")
        postFiled.click()
        postFiled.send_keys(content)

        visibility = self.driver.find_element_by_class("_55pe")
        visibility.click()

        moreOptions = self.driver.find_element_by_class("_54nh _4chm")
        moreOptions.click()
        if vis is self.visibility().friends :
           friends = self.driver.find_element_by_class("_54nh _4chm _48u0")
           friends.click()
        if vis is self.visibility().public:
            friends = self.driver.find_element_by_class("_54nh _4chm _48u0") #TODO
            friends.click()
        if vis is self.visibility().me:
            friends = self.driver.find_element_by_class("_54nh _4chm _48u0")
            friends.click()
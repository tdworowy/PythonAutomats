import os
import time

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Utils.enum_ import Enum

visibilityEnum= Enum(["friends",'public','me'])

#TODO
class facebookBot():
    def __init__(self,webdriver):
        self.driver= webdriver
        self.driver.get('https://pl-pl.facebook.com/')

    def loginFacebook(self, autentycation):
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


    def setVisibility(self,vis):

        visibility_ = self.driver.find_element_by_class("_55pe")
        visibility_.click()

        moreOptions = self.driver.find_element_by_class("_54nh _4chm")
        moreOptions.click()
        if vis is visibilityEnum.friends:
            friends = self.driver.find_elements_by_xpath("//*[contains(text(), 'Friends')]")
            friends.click()
        if vis is visibilityEnum.public:
            public = self.driver.find_elements_by_xpath("//*[contains(text(), 'Public')]")
            public.click()
        if vis is visibilityEnum.me:
            onlyMe = self.driver.find_elements_by_xpath("//*[contains(text(), 'Only me')]")
            onlyMe.click()

    def post(self, content, vis):
        postFiled = self.driver.find_element_by_css_selector("div[role='presentation']")
        postFiled.click()
        postFiled.send_keys(content)

        self.setVisibility(vis)

        postButton = self.driver.find_element_by_css_selector("button[data-testid='react-composer-post-button'")
        postButton.click()



if __name__ == '__main__':

    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    driver.maximize_window()
    driver.implicitly_wait(2)

    fb = facebookBot(driver)

    f = open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt')
    fb.loginFacebook((f.readline().strip(), f.readline().strip()))
    fb.post("Test",visibilityEnum.me)
import unittest

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class songOfTheDay():

    def __init__(self):
        self.setUp()

    def sendMessageToSelected(self,message):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.TAG_NAME, 'swx-textarea')))
        element = element.find_element_by_tag_name("textarea")
        element.click()
        element.clear()
        element.send_keys(message)
        element.send_keys(Keys.ENTER)



    def  login(self,autentycation ):
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
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'summary')))
        WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located((By.CLASS_NAME, 'shellSplashContent')))

    def select(self,name):
        searchSkype = self.driver.find_element_by_css_selector("div.input input.inputField.fontSize-h4")
        searchSkype.click()
        time.sleep(1)

        searchSkype = self.driver.find_element_by_css_selector("div.input.active input.inputField.fontSize-h4")
        searchSkype.send_keys(name)
        self.driver.implicitly_wait(5)
        group = self.driver.find_element_by_class_name("list-selectable")
        group.click()
        self.driver.implicitly_wait(5)
        time.sleep(2)



    def findSong(self, song):
        self.driver.get('https://www.youtube.com')
        input = self.driver.find_element_by_id("masthead-search-term")
        searchButton = self.driver.find_element_by_css_selector("button[type='submit']")
        input.click()
        input.send_keys(song)
        searchButton.click()

        self.driver.implicitly_wait(5)
        firstResoult = self.driver.find_element_by_css_selector("h3")
        firstResoult.click()
        self.driver.implicitly_wait(3)
        return self.driver.current_url





    def sentSong(self,autentycation,songURL):
        self.login(autentycation)

        self.select("A smiechom i szopom nie było konca")

        self.sendMessageToSelected("Piosenka dina [Auto]")
        self.sendMessageToSelected("songURL")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testsongOfTheDay(self):
         self.sentSong(["dworowytomasz@gmail.com","Jefferson Airplane1966!"],self.findSong("paranoid")) # TODO load data from file




def main():
  try:

      song = songOfTheDay()

      autentycation = ["dworowytomasz@gmail.com","Jefferson Airplane1966!"]

      url= song.findSong("paranoid")
      song.sentSong(autentycation , url)
      song.tearDown()

  except Exception  as err:
    print(err)
  finally:
    quit()


if __name__ == '__main__':
    main()
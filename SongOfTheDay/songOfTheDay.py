import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



class songOfTheDay(unittest.TestCase):

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
        self.driver.implicitly_wait(60)

        searchSkype = self.driver.find_element_by_css_selector("div.input input.inputField.fontSize-h4")
        searchSkype.click()
        searchSkype = self.driver.find_element_by_css_selector("div.input.active input.inputField.fontSize-h4")
        searchSkype.send_keys("A smiechom i szopom nie było konca")
        self.driver.implicitly_wait(5)
        group = self.driver.find_element_by_class_name("list-selectable")
        group.click()
        self.driver.implicitly_wait(5)
        messageImput = self.driver.find_element_by_css_selector("div#chatInputContainer.container textarea#chatInputAreaWithQuotes")# fail
        messageImput.click()
        messageImput.send_keys("Piosenka Dnia [AUTO]")
        messageImput.send_keys(Keys.ENTER)
        messageImput.send_keys(songURL)
        messageImput.send_keys(Keys.ENTER)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testsongOfTheDay(self):
         self.sentSong(["dworowytomasz@gmail.com","Jefferson Airplane1966!"],self.findSong("paranoid")) # TODO load data from file


if __name__ == '__main__':
    unittest.main()

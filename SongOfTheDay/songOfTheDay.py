import getpass
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from datetime import date
import calendar



class songOfTheDay():
    def __init__(self):
        self.setUp()

    def mesageByTime(self):
        now = datetime.datetime.now()
        today7 = now.replace(hour=7, minute=0, second=0, microsecond=0)
        today16 = now.replace(hour=16, minute=0, second=0, microsecond=0)
        today20 = now.replace(hour=16, minute=0, second=0, microsecond=0)
        dateToday = date.today()

        if calendar.day_name[dateToday.weekday()] is "Saturday" : "Piosenka na sobote[auto]"
        elif calendar.day_name[dateToday.weekday()] is "Sunday": "Piosenka na niedziele[auto]"
        elif today7 <= now <= today16 : return  "Piosenka dnia[auto]"
        elif today16 <  now <= today20: return "Piosenka na wieczór[auto]"
        elif  now > today20: return "Piosenka na noc[auto]"


    def sendMessageToSelected(self, message):


        actions = ActionChains(self.driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(1)


    def login(self, autentycation):
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

    def findSong(self, song):
        self.driver.get('https://www.youtube.com')
        input = self.driver.find_element_by_id("masthead-search-term")
        searchButton = self.driver.find_element_by_css_selector("button[type='submit']")
        input.click()
        input.send_keys(song)
        searchButton.click()
        time.sleep(2)
        firstResoult = self.driver.find_element_by_css_selector("h3 a")
        firstResoult.click()
        time.sleep(1)

        return self.driver.current_url

    def sentSong(self, autentycation, songURL):
        self.login(autentycation)

        self.select("Echo")
        self.select("A smiechom i szopom nie było konca")
        self.sendMessageToSelected(self.mesageByTime())
        self.sendMessageToSelected(songURL)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()



def main(login, password):
    try:

        song = songOfTheDay()
        f = open('file.txt', 'r')
        songsList = f.read()
        songsList=songsList.split("\n")
        autentycation = [login, password]

        ran= random.randrange(len(songsList))
        print(songsList[ran])
        url = song.findSong(songsList[ran].strip())
        song.sentSong(autentycation, url)
        song.tearDown()

    except Exception  as err:
        print(err)

    finally:
        quit()


if __name__ == '__main__':
    # var1 = input("Login: ")
    #var2 = input("Pass: ")
    f= open("aut.txt")

    main(f.readline().strip(), f.readline().strip())

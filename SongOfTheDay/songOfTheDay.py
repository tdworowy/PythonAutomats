import calendar
import datetime
import os
import random
import sys
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from SkypeBot.skypeBot import skypeBot
from SongOfTheDay.Songs import updateSongs
from Utils.decorators import logExeption
from Utils.utils import log
from chromedriverFolder.driverPath import getDriverPath


class songOfTheDay():
    def __init__(self):
        self.setUp()

    def mesageByTime(self):
        now = datetime.datetime.now()
        dateToday = date.today()
        log("Today is: "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today()))
        return "Song for "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today() + " [AUTO] ")



    def findSong(self, song):
        self.driver.get('https://www.youtube.com')
        actions = ActionChains(self.driver)

        input = self.driver.find_element_by_id("masthead-search-term")
        input.click()
        input.send_keys(song)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)
        firstResoult = self.driver.find_element_by_css_selector("h3 a")

        firstResoult.click()
        time.sleep(1)

        return self.driver.current_url

    def sentSong(self, autentycation, songURLs):
        self.skypeBot.login(autentycation)

        self.skypeBot.select("Echo")
        self.skypeBot.select("A smiechom i szopom nie było konca")
        log(self.mesageByTime())
        for songURL in songURLs:
            log(songURL)
            self.skypeBot.sendMessageToSelected(self.mesageByTime())
            self.skypeBot.sendMessageToSelected(songURL)

    def setUp(self):
        updateSongs()
        chromeDriverPath =getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.skypeBot = skypeBot(self.driver)


    def tearDown(self):
        self.driver.quit()


@logExeption
def main(login, password):
        song = songOfTheDay()
        f = open(os.path.dirname(os.path.abspath(__file__))+'\\file.txt', 'r')
        log("Get random song")
        songsList = f.read()
        songsList=songsList.split("\n")
        autentycation = [login, password]

        ran= random.randrange(len(songsList))
        log(songsList[ran])
        url = song.findSong(songsList[ran].strip())
        song.sentSong(autentycation, [url])
        song.tearDown()

@logExeption
def rickAndRollSpam(login, password,count):
        song = songOfTheDay()

        autentycation = [login, password]
        urlList = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ" for x in range(count)]
        song.sentSong(autentycation, urlList)
        song.tearDown()



if __name__ == '__main__':

   if len(sys.argv) <2:
     f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
     user = f.readline().strip()
     passw = f.readline().strip()
   else:
       user = sys.argv[1]
       passw = sys.argv[2]
   main(user, passw)


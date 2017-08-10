import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Skype.SkypeBot import SkypeBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log, mesageByTime, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDay():
    def __init__(self):
        self.setUp()



    def sentSong(self, autentycation, songURLs):
        self.skypeBot.login(autentycation)

        self.skypeBot.select("Echo")
        self.skypeBot.select("Szopy Reaktywacja!")
        log(mesageByTime())
        for songURL in songURLs:
            log(songURL)
            self.skypeBot.sendMessageToSelected(mesageByTime())
            self.skypeBot.sendMessageToSelected(songURL)
            saveHistory(songURL,"Skype.txt")

    def setUp(self):
        updateSongs()
        chromeDriverPath =getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.skypeBot = SkypeBot(self.driver)


    def tearDown(self):
        self.driver.quit()


@logExeption
def main(login, password):
        song = songOfTheDay()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")
        authentication = [login, password]

        ran = random.randrange(len(songsList))
        songTitle = songsList[ran]
        log(songTitle)
        saveHistory(songTitle, "Skype.txt")
        url = getYoutubeURL(song.driver,songTitle.strip())
        song.sentSong(authentication, [url])
        song.tearDown()

@logExeption
def rickAndRollSpam(login, password,count):
        song = songOfTheDay()

        authentication = [login, password]
        urlList = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ" for x in range(count)]
        song.sentSong(authentication, urlList)
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


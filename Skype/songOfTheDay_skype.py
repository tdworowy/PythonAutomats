import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Skype.SkypeApi_ import SkypeApi
from Skype.SkypeBot import SkypeBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log, mesageByTime, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDay():
    def __init__(self,authentication):
        self.setUp(authentication)



    def sentSongAPI(self, songURL,gropus):

        log(mesageByTime())
        log(songURL)
        self.sa.setChats(gropus)
        self.sa.snedMessage(mesageByTime())
        self.sa.snedMessage(songURL)

        for group in gropus:
            saveHistory(group, "Skype.txt")
            saveHistory(songURL,"Skype.txt")


    def sentSongUI(self, songURL,gropus):

        log(mesageByTime())
        log(songURL)
        self.sb.login(self.autentycation)

        for group in gropus:
            self.sb.select(group)
            self.sb.sendMessageToSelected(songURL)
            saveHistory(group, "Skype.txt")
            saveHistory(songURL,"Skype.txt")

    def setUp(self,autentycation):
        updateSongs()
        chromeDriverPath =getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.autentycation = autentycation
        self.sa = SkypeApi(self.autentycation[0], self.autentycation[1])
        self.sb = SkypeBot(self.driver)


    def tearDown(self):
         self.driver.quit()


@logExeption
def main(login, password):
        authentication = [login, password]
        song = songOfTheDay(authentication)
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")

        ran = random.randrange(len(songsList))
        songTitle = songsList[ran]
        log(songTitle)
        url = getYoutubeURL(song.driver,songTitle.strip())
        try:
            song.sentSongAPI(url,["Szopy Reaktywacja!","Shame"])
        except:
            song.sentSongUI(url,["Szopy Reaktywacja!","Shame"])



if __name__ == '__main__':

   if len(sys.argv) <2:
     f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
     user = f.readline().strip()
     passw = f.readline().strip()
   else:
       user = sys.argv[1]
       passw = sys.argv[2]
   main(user, passw)


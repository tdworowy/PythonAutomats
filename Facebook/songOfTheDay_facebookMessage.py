import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookAPI import FaceBookMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log, mesageByTime, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDayFace():
    def __init__(self):
        self.setUp()


    def sentSong(self, login,passw, songURLs,THREADID):

        log(mesageByTime())
        self.faceBot.logIn(login,passw)
        for songURL in songURLs:
            log(songURL)
            self.faceBot.sendMessage(mesageByTime(),THREADID)
            self.faceBot.sendMessage(songURL,THREADID)
            saveHistory(songURL,"FacebookMessage.txt")

    def setUp(self):
        updateSongs()
        chromeDriverPath = getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.faceBot = FaceBookMessageBot()



    def tearDown(self):
        self.faceBot.logout()
        self.driver.quit()

@logExeption
def main(login, password,THREADID):
        song = songOfTheDayFace()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")
        ran = random.randrange(len(songsList))
        songTitle =songsList[ran]
        log(songTitle)
        saveHistory(songTitle, "FacebookMessage.txt")
        url = getYoutubeURL(song.driver,songTitle.strip())
        song.sentSong(login,password, [url],THREADID)
        song.tearDown()


if __name__ == '__main__':

   THREADID = '1252344071467839'
   if len(sys.argv) <2:
     f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
     user = f.readline().strip()
     passw = f.readline().strip()
   else:
       user = sys.argv[1]
       passw = sys.argv[2]+" "+sys.argv[3]
   main(user, passw,THREADID)
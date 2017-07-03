import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookAPI import FaceBookMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log, mesageByTime
from Youtube.YoutubeBot import getYoutubeURL

THREADID = '1252344071467839'

class songOfTheDay():
    def __init__(self):
        self.setUp()





    def sentSong(self, login,passw, songURLs):

        log(mesageByTime())
        self.faceBot.logIn(login,passw)
        for songURL in songURLs:
            log(songURL)
            self.faceBot.sendMessage(mesageByTime(),THREADID)
            self.faceBot.sendMessage(songURL,THREADID)

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
def main(login, password):
        song = songOfTheDay()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")

        ran = random.randrange(len(songsList))
        log(songsList[ran])
        url = getYoutubeURL(song.driver,songsList[ran].strip())
        song.sentSong(login,password, [url])
        song.tearDown()


if __name__ == '__main__':

   if len(sys.argv) <2:
     f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
     user = f.readline().strip()
     passw = f.readline().strip()
   else:
       user = sys.argv[1]
       passw = sys.argv[2]+" "+sys.argv[3]
   main(user, passw)
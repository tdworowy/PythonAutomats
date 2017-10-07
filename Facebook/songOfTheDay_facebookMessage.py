import os
import random
import sys

from fbchat.models import *
from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookAPI import FaceBookMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import log_exeption
from Utils.utils import log, mesageByTime, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDayFace:
    def __init__(self):
        self.faceBot = FaceBookMessageBot()




    def loginFB(self,login,passw):
        self.faceBot.logIn(login, passw)


    def sentSong(self, songURLs,THREADID,message = mesageByTime(),ThreadType = ThreadType.GROUP ):

        log(mesageByTime())

        for songURL in songURLs:
            log(songURL)
            self.faceBot.sendMessage(message,THREADID,ThreadType)
            self.faceBot.sendMessage(songURL,THREADID,ThreadType)
            saveHistory(songURL,"FacebookMessage.txt")

    def setUp(self):
        chromeDriverPath = getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)




    def tearDown(self):
        self.driver.quit()

    def logout(self):
        self.faceBot.logout()

@log_exeption
def main(login, password,THREADID):
        updateSongs()
        song = songOfTheDayFace()
        song.setUp()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")
        ran = random.randrange(len(songsList))
        songTitle =songsList[ran]
        url = getYoutubeURL(song.driver,songTitle.strip())
        song.loginFB(login,password)
        song.sentSong([url],THREADID)
        song.tearDown()
        song.logout()


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
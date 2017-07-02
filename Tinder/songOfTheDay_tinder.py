import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.FacebookToken import get_access_token
from Facebook.facebookAPI import FaceBookMessageBot
from Tinder.TinderApi import TinderMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDay():
    def __init__(self):
        self.setUp()



    def sentSong(self, login,passw, songURLs,to):

        self.faceBot.logIn(login,passw)
        for songURL in songURLs:
            log(songURL)
            token = get_access_token(login,passw)
            tm = TinderMessageBot()
            tm.logIn(100001295284655, token)
            for match in tm.getMatches():
                if match.user.id == to:
                    log("Send message to: %s " % match.user.id)
                    match.message("Automatyczna piosenka dla Ilony :D")
                    match.message(songURL)

    def setUp(self):
        updateSongs()
        chromeDriverPath = getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.faceBot = FaceBookMessageBot()



    def tearDown(self):
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
        song.sentSong(login,password, [url],'Ilona')
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
import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookID import getFacebookID
from Facebook.facebookToken import get_access_token
from Tinder.TinderApi import TinderMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDay():
    def __init__(self):
        self.setUp()


    def logIN(self,login,passw,name):
        token = get_access_token(login, passw)
        self.tm = TinderMessageBot()
        id = getFacebookID(self.driver, name)
        self.tm.logIn(id, token)

    def sentSong(self,songURL,to):
            log(songURL)
            for match in self.tm.getMatches():
                if match.user.name == to:
                    log("Send message to: %s " % match.user.name)
                    match.message("[ Auto song for: %s :D ]" % match.user.name)
                    match.message(songURL)
                    saveHistory("Song for %s" % match.user.name, "Tinder.txt")
                    saveHistory(songURL,"Tinder.txt")

    def setUp(self):
        updateSongs()
        chromeDriverPath = getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)


@logExeption
def main(login, password,names):
        song = songOfTheDay()
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")

        ran = random.randrange(len(songsList))
        songTitle = songsList[ran]
        log(songTitle)
        saveHistory(songTitle, "Tinder.txt")
        song.logIN(login, password,'tomasz.dworowy')
        for name in names:
            url = getYoutubeURL(song.driver,songTitle.strip())
            song.sentSong(url,name)



if __name__ == '__main__':
   if len(sys.argv) <2:
     f= open(os.path.dirname(os.path.abspath(__file__))+'\\aut.txt')
     user = f.readline().strip()
     passw = f.readline().strip()
   else:
       user = sys.argv[1]
       passw = sys.argv[2]+" "+sys.argv[3]

   # namesList = ['Ilona','Carol']
   namesList = ['Ilona']
   main(user, passw,namesList)
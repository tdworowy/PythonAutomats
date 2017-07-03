
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookPost import FaceBookPost
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log
from Youtube.YoutubeBot import getYoutubeURL


class songOfTheDay():
    def __init__(self,pageID, appid, app_secred):
        self.setUp(pageID, appid, app_secred)




    def sentSong(self,songURLs):

        # log(mesageByTime())

        for songURL in songURLs:
            log(songURL)
            self.faceBot.facebookPost(songURL)


    def setUp(self,pageID, appid, app_secred):
        updateSongs()
        chromeDriverPath = getDriverPath()+'\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        self.driver.implicitly_wait(2)
        self.faceBot = FaceBookPost(pageID, appid, app_secred)



    def tearDown(self):
        self.driver.quit()

@logExeption
def main(pageID, appid, app_secred):
        song = songOfTheDay(pageID, appid, app_secred)
        f = open(getFilePath(), 'r')
        log("Get random song")
        songsList = f.read()
        songsList = songsList.split("\n")

        ran = random.randrange(len(songsList))
        log(songsList[ran])
        url = getYoutubeURL(song.driver,songsList[ran].strip())
        song.sentSong([url])
        song.tearDown()


if __name__ == '__main__':

       pageid = sys.argv[1]
       appid = sys.argv[2]
       app_secred = sys.argv[3]

       main(pageid, appid,app_secred)
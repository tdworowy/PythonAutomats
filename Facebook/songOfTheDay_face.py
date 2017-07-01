
import calendar
import datetime
import random
from datetime import date

from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookAPI import FaceBookMessageBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import logExeption
from Utils.utils import log
from Youtube.YoutubeBot import getYoutubeURL

THREADID = '1252344071467839'

class songOfTheDay():
    def __init__(self):
        self.setUp()

    def mesageByTime(self):
        now = datetime.datetime.now()
        dateToday = date.today()
        log("Today is: "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today()))
        return "Song for "+str(calendar.day_name[dateToday.weekday()])+" "+str(date.today()) + " [AUTO] "



    def sentSong(self, login,passw, songURLs):

        log(self.mesageByTime())
        self.faceBot.logIn(login,passw)
        for songURL in songURLs:
            log(songURL)
            self.faceBot.sendMessage(self.mesageByTime(),THREADID)
            self.faceBot.sendMessage(songURL,THREADID)

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
        authentication = [login, password]

        ran = random.randrange(len(songsList))
        log(songsList[ran])
        url = getYoutubeURL(song.driver,songsList[ran].strip())
        song.sentSong(authentication, [url])
        song.tearDown()
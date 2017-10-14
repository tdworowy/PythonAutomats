import os
import random
import sys

from ChromedriverFolder.driverPath import get_driver_path
from Facebook.facebookAPI import FaceBookMessageBot
from Utils.Songs_.Songs import update_songs, get_file_path
from Utils.decorators import log_exception
from Utils.utils import log, message_by_time, save_history
from Youtube.Youtube_Bot import get_youtube_URL
from fbchat.models import *
from selenium import webdriver


class SongOfTheDayFace:
    def __init__(self):
        self.faceBot = FaceBookMessageBot()

    def login_FB(self, login, passw):
        self.faceBot.login(login, passw)

    def sentSong(self, songURLs, THREADID, message=message_by_time(), ThreadType=ThreadType.GROUP):
        log(message_by_time())

        for songURL in songURLs:
            log(songURL)
            self.faceBot.send_message(message, THREADID, ThreadType)
            self.faceBot.send_message(songURL, THREADID, ThreadType)
            save_history(songURL, "FacebookMessage.txt")

    def setUp(self):
        chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)

    def tear_down(self):
        self.driver.quit()

    def logout(self):
        self.faceBot.logout()


@log_exception()
def main(login, password, threadid):
    update_songs()
    song = SongOfTheDayFace()
    song.setUp()
    f = open(get_file_path(), 'r')
    log("Get random song")
    songsList = f.read()
    songsList = songsList.split("\n")
    ran = random.randrange(len(songsList))
    songTitle = songsList[ran]
    url = get_youtube_URL(song.driver, songTitle.strip())
    song.login_FB(login, password)
    song.sentSong([url], threadid)
    song.tear_down()
    song.logout()


if __name__ == '__main__':

    THREADID = '1252344071467839'
    if len(sys.argv) < 2:
        f = open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt')
        user = f.readline().strip()
        passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2] + " " + sys.argv[3]
    main(user, passw, THREADID)

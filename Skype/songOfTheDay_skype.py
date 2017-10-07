import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import get_driver_path
from Skype.SkypeApi_ import SkypeApi
from Skype.SkypeBot import SkypeBot
from Utils.Songs_.Songs import updateSongs, getFilePath
from Utils.decorators import log_exeption
from Utils.utils import log, mesageByTime, saveHistory
from Youtube.YoutubeBot import getYoutubeURL


class SongOfTheDay():
    def __init__(self, authentication):
        self.set_up(authentication)

    def sent_song_API(self, songURL, gropus):

        log(mesageByTime())
        log(songURL)
        self.sa.set_chats(gropus)
        self.sa.sned_message(mesageByTime())
        self.sa.sned_message(songURL)

        for group in gropus:
            saveHistory(group, "Skype.txt")
            saveHistory(songURL, "Skype.txt")

    def sent_song_UI(self, songURL, gropus):
        log(mesageByTime())
        log(songURL)
        self.sb.login(self.authentication)

        for group in gropus:
            self.sb.select("echo")
            self.sb.select(group)
            self.sb.send_message_to_selected(songURL)
            saveHistory(group, "Skype.txt")
            saveHistory(songURL, "Skype.txt")

    def set_up(self, authentication):
        updateSongs()
        chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        # self.driver = webdriver.PhantomJS(getPhantomPath()+'\\Phantomjs.exe')
        self.driver.implicitly_wait(2)
        self.authentication = authentication
        self.sa = SkypeApi(self.authentication[0], self.authentication[1])
        self.sb = SkypeBot(self.driver)

    def tear_down(self):
        self.driver.quit()


@log_exeption(False)
def main(login, password):
    authentication = [login, password]
    song = SongOfTheDay(authentication)
    f = open(getFilePath(), 'r')
    log("Get random song")
    songsList = f.read()
    songsList = songsList.split("\n")

    ran = random.randrange(len(songsList))
    songTitle = songsList[ran]
    log(songTitle)
    url = getYoutubeURL(song.driver, songTitle.strip())
    try:
        song.sent_song_API(url, ["Szopy Reaktywacja!", "Shame"])
    except Exception as e:
        log("API error %s" % str(e) )
        song.sent_song_UI(url, ["Szopy Reaktywacja!", "Shame"])


if __name__ == '__main__':

    if len(sys.argv) < 2:
        f = open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt')
        user = f.readline().strip()
        passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2]
    main(user, passw)

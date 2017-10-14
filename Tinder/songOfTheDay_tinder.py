import os
import random
import sys

from ChromedriverFolder.driverPath import get_driver_path
from Facebook.facebookID import getFacebookID
from Facebook.facebookToken import get_access_token
from Tinder.TinderApi import TinderMessageBot
from Utils.Songs_.Songs import update_songs, get_file_path
from Utils.decorators import log_exception
from Utils.utils import log, save_history
from Youtube.YoutubeBot import get_youtube_URL
from selenium import webdriver


class SongOfTheDay():
    def __init__(self):
        self.set_up()

    def log_in(self, login, passw, name):
        token = get_access_token(login, passw)
        self.tm = TinderMessageBot()
        id = getFacebookID(self.driver, name)
        self.tm.logIn(id, token)

    def sent_song(self, songURL, to):
        log(songURL)
        for match in self.tm.get_matches():
            if match.user.name == to:
                log("Send message to: %s " % match.user.name)
                match.message("[ Auto song for: %s :D ]" % match.user.name)
                match.message(songURL)
                save_history("Song for %s" % match.user.name, "Tinder.txt")
                save_history(songURL, "Tinder.txt")

    def set_up(self):
        update_songs()
        chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)


@log_exception()
def main(login, password, names):
    song = SongOfTheDay()
    f = open(get_file_path(), 'r')
    log("Get random song")
    songsList = f.read()
    songsList = songsList.split("\n")

    ran = random.randrange(len(songsList))
    songTitle = songsList[ran]
    song.log_in(login, password, 'tomasz.dworowy')
    for name in names:
        url = get_youtube_URL(song.driver, songTitle.strip())
        song.sent_song(url, name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        f = open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt')
        user = f.readline().strip()
        passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2] + " " + sys.argv[3]

    # namesList = ['Ilona','Carol']
    namesList = ['Ilona']
    main(user, passw, namesList)

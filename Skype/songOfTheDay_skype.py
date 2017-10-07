import os
import random
import sys

from selenium import webdriver

from ChromedriverFolder.driverPath import get_driver_path
from Skype.SkypeApi_ import SkypeApi
from Skype.SkypeBot import SkypeBot
from Utils.Songs_.Songs import update_songs, get_file_path
from Utils.decorators import log_exeption
from Utils.utils import log, mesage_by_time, save_history
from Youtube.YoutubeBot import getYoutubeURL


class SongOfTheDay():
    def __init__(self, authentication):
        update_songs()
        chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        self.driver.implicitly_wait(2)
        self.authentication = authentication

    def sent_song_API(self, songURL, gropus):
        sa = SkypeApi(self.authentication[0], self.authentication[1])
        log(mesage_by_time())
        log(songURL)
        sa.set_chats(gropus)
        sa.sned_message(mesage_by_time())
        sa.sned_message(songURL)

        for group in gropus:
            save_history(group, "Skype.txt")
            save_history(songURL, "Skype.txt")

    def sent_song_UI(self, songURL, gropus):
        log(mesage_by_time())
        log(songURL)
        sb = SkypeBot(self.driver)
        sb.login(self.authentication)

        for group in gropus:
            sb.select("echo")
            sb.select(group)
            sb.send_message_to_selected(songURL)
            sb.send_message_to_selected(mesage_by_time())
            save_history(group, "Skype.txt")
            save_history(songURL, "Skype.txt")

    def tear_down(self):
        self.driver.quit()


@log_exeption(False)
def main(login, password):
    authentication = [login, password]
    song = SongOfTheDay(authentication)
    f = open(get_file_path(), 'r')
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
        log("API error: %s" % str(e) )
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

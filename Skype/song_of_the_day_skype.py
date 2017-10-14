import os
import random
import sys

from Chrome_Driver_Folder.driver_path import get_driver_path
from Skype.skype_api_ import SkypeApi
from Skype.skype_bot import SkypeBot
from Utils.Songs_.Songs import update_songs, get_file_path
from Utils.decorators import log_exception
from Utils.utils import log, message_by_time, save_history
from Youtube.Youtube_Bot import get_youtube_URL
from selenium import webdriver


class SongOfTheDay():
    def __init__(self, authentication):
        update_songs()
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)
        self.authentication = authentication

    def sent_song_API(self, songURL, gropus):
        sa = SkypeApi(self.authentication[0], self.authentication[1])
        log(message_by_time())
        log(songURL)
        sa.set_chats(gropus)
        sa.sned_message(message_by_time())
        sa.sned_message(songURL)

        for group in gropus:
            save_history(group, "Skype.txt")
            save_history(songURL, "Skype.txt")

    def sent_song_UI(self, songURL, gropus):
        log(message_by_time())
        log(songURL)
        sb = SkypeBot(self.driver)
        sb.login(self.authentication)

        for group in gropus:
            sb.select("echo")
            sb.select(group)
            sb.send_message_to_selected(message_by_time())
            sb.send_message_to_selected(songURL)
            save_history(group, "Skype.txt")
            save_history(songURL, "Skype.txt")

    def tear_down(self):
        self.driver.quit()


@log_exception(False)
def main(login, password):
    authentication = [login, password]
    song = SongOfTheDay(authentication)
    f = open(get_file_path(), 'r')
    log("Get random song")
    songs = f.read()
    songs = songs.split("\n")

    ran = random.randrange(len(songs))
    song_title = songs[ran]
    log(song_title)
    url = get_youtube_URL(song.driver, song_title.strip())
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

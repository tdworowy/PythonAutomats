import os
import sys
from random import choice

from selenium import webdriver

from Chrome_Driver_Folder.driver_path import get_driver_path
from Skype.skype_api_ import SkypeApi
from Skype.skype_bot import SkypeBot
from Utils.Songs_.Songs import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import log, message_by_time, save_history
from Youtube.Youtube_Bot import get_youtube_url


class SongOfTheDay():
    def __init__(self, authentication):
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)
        self.authentication = authentication

    def sent_song_API(self, songURL, gropus):
        sa = SkypeApi(self.authentication[0], self.authentication[1])
        log().info(songURL)
        sa.set_chats(gropus)
        sa.send_message(message_by_time())
        sa.send_message(songURL)

        for group in gropus:
            save_history(group, "Skype.txt")
            save_history(songURL, "Skype.txt")

    def sent_song_UI(self, songURL, gropus):
        log().info(songURL)
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
        try:
            self.driver.quit()
        except Exception as ex:
            print(ex)


@log_exception()
def main(login, password):
    update_songs_distribution()
    log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()
    songs = songs.split("\n")

    song_title = choice(songs.split("\n")
                        )
    song = SongOfTheDay([login, password])
    url = get_youtube_url(song.driver, song_title.strip())
    try:
        song.sent_song_API(url, ["Szopy Reaktywacja!", "Shame"])
    except Exception as e:
        log().error("API error: %s" % str(e))
        song.sent_song_UI(url, ["Szopy Reaktywacja!", "Shame"])


if __name__ == '__main__':

    if len(sys.argv) < 2:
        with  open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt') as f:
            user = f.readline().strip()
            passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2]
    main(user, passw)

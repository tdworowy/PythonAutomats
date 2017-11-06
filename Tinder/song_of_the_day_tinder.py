import os
import random
import sys

from selenium import webdriver

from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_id import get_facebook_ID
from Facebook.facebook_token import get_access_token
from Tinder.tinder_Api import TinderMessageBot
from Utils.Songs_.Songs import update_songs, get_file_path
from Utils.decorators import log_exception
from Utils.utils import log, save_history
from Youtube.Youtube_Bot import get_youtube_URL


class SongOfTheDay():
    def __init__(self):
        self.set_up()

    def log_in(self, login, passw, name):
        token = get_access_token(login, passw)
        self.tm = TinderMessageBot()
        id = get_facebook_ID(self.driver, name)
        self.tm.logIn(id, token)

    def sent_song(self, song_URL, to):
        log(song_URL)
        for match in self.tm.get_matches():
            if match.user.name == to:
                log("Send message to: %s " % match.user.name)
                match.message("[ Auto song for: %s :D ]" % match.user.name)
                match.message(song_URL)
                save_history("Song for %s" % match.user.name, "Tinder.txt")
                save_history(song_URL, "Tinder.txt")

    def set_up(self):
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)


@log_exception()
def main(login, password, names):
    update_songs()
    log("Get random song")
    with open(get_file_path(), 'r') as f:
        songs_list = f.read()
    songs_list = songs_list.split("\n")

    ran = random.randrange(len(songs_list))
    song_title = songs_list[ran]
    song = SongOfTheDay()
    song.log_in(login, password, 'tomasz.dworowy')
    for name in names:
        url = get_youtube_URL(song.driver, song_title.strip())
        song.sent_song(url, name)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt') as f:
            user = f.readline().strip()
            passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2] + " " + sys.argv[3]

    # namesList = ['Ilona','Carol']
    names = ['Ilona']
    main(user, passw, names)

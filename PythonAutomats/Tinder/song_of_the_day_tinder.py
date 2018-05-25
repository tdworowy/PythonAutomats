import sys
from random import choice

from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_id import get_facebook_ID
from Facebook.facebook_token import get_access_token
from Tinder.tinder_Api import TinderMessageBot
from Utils.Songs_.Songs import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import MyLogging
from Youtube.Youtube_Bot import get_youtube_url
from selenium import webdriver


class SongOfTheDay():
    def __init__(self):
        self.set_up()
        self.mylogging = MyLogging()

    def log_in(self, login, passw, name):
        token = get_access_token(login, passw)
        self.tm = TinderMessageBot()
        id = get_facebook_ID(self.driver, name)
        self.tm.logIn(id, token)

    def sent_song(self, song_URL, to):
        self.mylogging.log().info(song_URL)
        for match in self.tm.get_matches():
            if match.user.name == to:
                self.mylogging.log("Send message to: %s " % match.user.name)
                match.message("[ Auto song for: %s :D ]" % match.user.name)
                match.message(song_URL)
                self.mylogging.save_history("Song for %s" % match.user.name, "Tinder.txt")
                self.mylogging.save_history(song_URL, "Tinder.txt")

    def set_up(self):
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)


@log_exception()
def main(login, password, names):
    update_songs_distribution()
    song = SongOfTheDay()
    song.mylogging.log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs_list = f.read()
    songs_list = songs_list.split("\n")

    song_title = choice(songs_list)

    song.log_in(login, password, 'tomasz.dworowy')
    for name in names:
        url = get_youtube_url(song.driver, song_title.strip())
        song.sent_song(url, name)


if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    nams = sys.argv[4]
    # namesList = ['Ilona','Carol']
    names = [nams]
    main(user, passw, names)

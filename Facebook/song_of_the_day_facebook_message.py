import os
import sys
from random import choice

from fbchat.models import *
from selenium import webdriver

from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_api import FaceBookMessageBot
from Utils.Songs_.Songs import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import message_by_time, MyLogging
from Youtube.Youtube_Bot import get_youtube_url


class SongOfTheDayFace:
    def __init__(self):
        self.face_bot = FaceBookMessageBot()
        self.mylogging = MyLogging()

    def login_FB(self, login, passw):
        self.face_bot.login(login, passw)

    def sent_song(self, songs_urls, thread_id, message=message_by_time(), thread_type=ThreadType.GROUP):

        for songURL in songs_urls:
            self.mylogging.log().info(songURL)
            self.face_bot.send_message(message, thread_id, thread_type)
            self.face_bot.send_message(songURL, thread_id, thread_type)
            self.mylogging.save_history(songURL, "FacebookMessage.txt")

    def set_up(self):
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)

    def tear_down(self):
        try:
            self.driver.quit()
        except Exception as ex:
            print(ex)

    def logout(self):
        self.face_bot.logout()


@log_exception()
def main(login, password, thread_id):
    update_songs_distribution()
    log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()
    song_title = choice(songs.split("\n"))

    song = SongOfTheDayFace()
    song.set_up()
    url = get_youtube_url(song.driver, song_title.strip())
    song.login_FB(login, password)
    song.sent_song([url], thread_id)
    song.tear_down()
    song.logout()


if __name__ == '__main__':

    THREADID = '1252344071467839'
    if len(sys.argv) < 2:
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt') as f:
            user = f.readline().strip()
            passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2] + " " + sys.argv[3]
    main(user, passw, THREADID)

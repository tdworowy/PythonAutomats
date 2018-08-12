import sys
from random import choice

from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_post import FaceBookPost
from Songs.last_fm_parser import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import MyLogging
from Youtube.Youtube_Bot import get_youtube_url
from selenium import webdriver


class SongOfTheDay:
    def __init__(self, page_id, app_id, app_secret):
        self.set_up(page_id, app_id, app_secret)
        self.mylogging = MyLogging()

    def sent_song(self, songs_urls):
        for songURL in songs_urls:
            self.mylogging.log().info(songURL)
            self.face_bot.facebook_post(songURL)

    def set_up(self, page_id, app_id, app_secret):
        update_songs_distribution()
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)
        self.face_bot = FaceBookPost(page_id, app_id, app_secret)

    def tear_down(self):
        self.driver.quit()


@log_exception
def main(page_id, app_id, app_secred):
    song = SongOfTheDay(page_id, app_id, app_secred)

    song.mylogging.log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()

    url = get_youtube_url(song.driver, choice(songs.split("\n")))
    song.sent_song([url])
    song.tear_down()


if __name__ == '__main__':
    page_id = sys.argv[1]
    app_id = sys.argv[2]
    app_secret = sys.argv[3]

    main(page_id, app_id, app_secret)

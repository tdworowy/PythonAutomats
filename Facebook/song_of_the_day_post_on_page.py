import random
import sys

from selenium import webdriver

from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_post import FaceBookPost
from Utils.Songs_.Songs import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import log
from Youtube.Youtube_Bot import get_youtube_url


class SongOfTheDay:
    def __init__(self, page_id, app_id, app_secred):
        self.set_up(page_id, app_id, app_secred)

    def sent_song(self, songs_urls):
        for songURL in songs_urls:
            log(songURL)
            self.face_bot.facebook_post(songURL)

    def set_up(self, page_id, app_id, app_secred):
        update_songs_distribution()
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)
        self.face_bot = FaceBookPost(page_id, app_id, app_secred)

    def tear_down(self):
        self.driver.quit()


@log_exception
def main(page_id, app_id, app_secred):
    song = SongOfTheDay(page_id, app_id, app_secred)
    f = open(FILE_PATH, 'r')
    log("Get random song")
    songs = f.read()
    songs = songs.split("\n")

    ran = random.randrange(len(songs))
    log(songs[ran])
    url = get_youtube_url(song.driver, songs[ran].strip())
    song.sent_song([url])
    song.tear_down()


if __name__ == '__main__':
    page_id = sys.argv[1]
    app_id = sys.argv[2]
    app_secret = sys.argv[3]

    main(page_id, app_id, app_secret)

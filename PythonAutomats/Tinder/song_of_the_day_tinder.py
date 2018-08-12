import sys
from random import choice

from Chrome_Driver_Folder.driver_path import get_driver_path
from Songs.Songs import SongOfTheDay
from Songs.last_fm_parser import FILE_PATH, update_songs_distribution
from Tinder.tinder_Api import TinderMessageBot, TinderAdapter
from Utils.decorators import log_exception
from Youtube.Youtube_bot_requests import get_youtube_url
from selenium import webdriver


@log_exception()
def main(login, password, names):
    update_songs_distribution()
    tinder_bot = TinderMessageBot()
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    with open(FILE_PATH, 'r') as f:
        songs_list = f.read()
    songs_list = songs_list.split("\n")
    song_title = choice(songs_list)
    adapter = TinderAdapter(tiderBot=tinder_bot, name='tomasz.dworowy', receivers=names, driver=driver)
    song = SongOfTheDay(adapter)
    song.my_logging.log().info("Get random song")
    song.login(login, password)
    url = get_youtube_url(song_title.strip())
    song.sent_songs([url])


if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    nams = sys.argv[4]
    # namesList = ['Ilona','Carol']
    names = [nams]
    main(user, passw, names)

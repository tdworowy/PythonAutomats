import os
import sys
from random import choice

from Chrome_Driver_Folder.driver_path import get_driver_path
from Skype.skype_api_ import SkypeApi, SkypeApiAdapter
from Skype.skype_bot import SkypeBot, SkypeBotAdapter
from Songs.Songs import SongOfTheDay
from Songs.last_fm_parser import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Youtube.Youtube_bot_requests import get_youtube_url
from selenium import webdriver


@log_exception()
def main(login, password, groups):
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    update_songs_distribution()
    skype_api = SkypeApi()
    skype_bot = SkypeBot(driver)
    skype_adapter = SkypeApiAdapter(skype_api, groups=groups)
    skype_bot_adapter = SkypeBotAdapter(skype_bot, groups=groups)
    song_api = SongOfTheDay(skype_adapter)
    song_ui = SongOfTheDay(skype_bot_adapter)
    song_api.my_logging.log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()
    songs = songs.split("\n")
    song_title = choice(songs)

    url = get_youtube_url(song_title.strip())
    try:
        song_api.login(login, password)
        song_api.sent_songs([url])
    except Exception as e:
        song_ui.my_logging.log().error("API error: %s" % str(e))
        song_ui.login(login, password)
        song_ui.sent_songs(url)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt') as f:
            user = f.readline().strip()
            passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2]
    main(user, passw, ["Szopy Reaktywacja!", "Shame"])

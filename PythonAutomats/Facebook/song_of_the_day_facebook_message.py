import os
import sys
from random import choice

from Facebook.facebook_api import FaceBookMessageBot
from Songs.Songs import SongOfTheDay
from Songs.last_fm_parser import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import message_by_time
from Youtube.Youtube_bot_requests import get_youtube_url
from fbchat.models import *


@log_exception()
def main(login, password, thread_id):
    update_songs_distribution()
    face_bot = FaceBookMessageBot(thread_id=thread_id, thread_type=ThreadType.GROUP)
    song = SongOfTheDay(face_bot)
    song.my_logging.log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()

    songs = songs.split("\n")
    song_title = choice(songs)

    url = get_youtube_url(song_title.strip())
    song.login(login, password)
    song.sent_messages([message_by_time(), "Title: %s" % song_title, "Total songs count: %s" % len(songs)])
    song.sent_songs([url])
    song.save_history("Title: %s url: %s " % (song_title, url), "FacebookMessage.txt")
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

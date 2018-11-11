import os
import sys
from random import choice

from Api.Songs import ApiAdapter
from Facebook.facebook_api import FaceBookMessageBot
from Songs.last_fm_parser import FOLDER_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Youtube.Youtube_bot_requests import get_youtube_url
from fbchat.models import *


@log_exception()
def main(login, password, thread_id):
    update_songs_distribution()
    face_bot = FaceBookMessageBot(thread_id=thread_id, thread_type=ThreadType.GROUP)
    song = ApiAdapter(face_bot)
    song.my_logging.log().info("Get random song")
    with open(os.path.join(FOLDER_PATH, "thomasList.Txt"), 'r') as f:
        thomsa_songs = f.read().split("\n")

    with open(os.path.join(FOLDER_PATH, "roobalList.Txt"), 'r') as f:
        roobal_songs = f.read().split("\n")

    thomas_song_title = choice(thomsa_songs)
    roobal_song_title = choice(roobal_songs)

    thomas_url = get_youtube_url(thomas_song_title.strip())
    roobal_url = get_youtube_url(thomas_song_title.strip())
    song.login(login, password)
    song.sent_messages(["Thomas songs", "Title: %s" % thomas_song_title, "Total songs count: %s" % len(thomsa_songs)])
    song.sent_messages([thomas_url])
    song.sent_messages(["Roobal songs", "Title: %s" % roobal_song_title,  "Total songs count: %s" % len(roobal_songs)])
    song.sent_messages([roobal_url])
    song.save_history("Title: %s url: %s " % (thomas_song_title, thomas_url), "FacebookMessage.txt")
    song.save_history("Title: %s url: %s " % (roobal_song_title, roobal_url), "FacebookMessage.txt")
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

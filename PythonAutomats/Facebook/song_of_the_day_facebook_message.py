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

    def temp1():
        send_song_fasade(login, password, thread_id, "thomas")

    def temp2():
        send_song_fasade(login, password, thread_id, "roobal")

    funcs = [temp1, temp2]
    choice(funcs)()


def send_song_fasade(login, password, thread_id, last_fm_user):
    update_songs_distribution()
    face_bot = FaceBookMessageBot(thread_id=thread_id, thread_type=ThreadType.GROUP)
    song = ApiAdapter(face_bot)
    song.my_logging.log().info("Get random song")

    with open(os.path.join(FOLDER_PATH, "%sList.Txt" % last_fm_user), 'r') as f:
        songs = f.read().split("\n")

    song_title = choice(songs)

    url = get_youtube_url(song_title.strip())
    song.login(login, password)

    song.sent_messages(["%s song" % last_fm_user, "Title: %s" %  url, "Total songs count: %s" % len(songs)])
    song.sent_messages([url])
    song.logout()


if __name__ == '__main__':

    THREADID = '1252344071467839'
    if len(sys.argv) < 2:
        with open(os.path.dirname(os.path.abspath(__file__)) + '\\aut.txt') as f:
            user = f.readline().strip()
            passw = f.readline().strip()
    else:
        user = sys.argv[1]
        passw = sys.argv[2]
    main(user, passw, THREADID)

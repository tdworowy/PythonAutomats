import os
import sys
from random import choice

from Facebook.facebook_api import FaceBookMessageBot
from Utils.Songs_.Songs import FILE_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Utils.utils import message_by_time, MyLogging
from Youtube.Youtube_bot_requests import get_youtube_url
from fbchat.models import *


class SongOfTheDayFace:
    def __init__(self):
        self.face_bot = FaceBookMessageBot()
        self.mylogging = MyLogging()

    def login_FB(self, login, passw):
        self.face_bot.login(login, passw)

    def sent_messages(self, messages, thread_id, thread_type=ThreadType.GROUP):
        for message in messages:
            self.mylogging.log().info(messages)
            self.face_bot.send_message(message, thread_id, thread_type)

    def sent_songs(self, songs_urls, thread_id, thread_type=ThreadType.GROUP):
        for songURL in songs_urls:
            self.mylogging.log().info(songURL)
            self.face_bot.send_message(songURL, thread_id, thread_type)

    def save_history(self, message):
        self.mylogging.save_history(message, "FacebookMessage.txt")

    def logout(self):
        self.face_bot.logout()


@log_exception()
def main(login, password, thread_id):
    update_songs_distribution()
    song = SongOfTheDayFace()
    song.mylogging.log().info("Get random song")
    with open(FILE_PATH, 'r') as f:
        songs = f.read()

    songs = songs.split("\n")
    song_title = choice(songs)

    url = get_youtube_url(song_title.strip())
    song.login_FB(login, password)
    song.sent_messages([message_by_time(), "Title: %s" % song_title, "Total songs count: %s" % len(songs)], thread_id)
    song.sent_songs([url], thread_id)
    song.save_history("Title: %s url: %s " % (song_title, url))
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

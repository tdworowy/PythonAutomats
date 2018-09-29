import os
import sys

from Api.Songs import ApiAdapter
from Facebook.facebook_api import FaceBookMessageBot
from Songs.last_fm_parser import update_songs_distribution
from Utils.decorators import log_exception
from Wiki.wiki_bot import get_random_wiki_page_title
from Youtube.Youtube_bot_requests import get_youtube_url
from fbchat.models import *


@log_exception()
def main(login, password, thread_id):
    update_songs_distribution()
    face_bot = FaceBookMessageBot(thread_id=thread_id, thread_type=ThreadType.GROUP)
    api = ApiAdapter(face_bot)

    title = get_random_wiki_page_title()
    url = get_youtube_url(title)
    api.login(login, password)
    api.sent_messages(["Random staff of the day:", title, url])
    api.logout()


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

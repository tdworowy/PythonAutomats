import os
import sys
from random import choice

from Api.Songs import ApiAdapter
from Slack.slack_api import SlackMessageBot
from Songs.last_fm_parser import FOLDER_PATH, update_songs_distribution
from Utils.decorators import log_exception
from Youtube.Youtube_bot_requests import get_youtube_url


@log_exception()
def main(channel, token):
    last_fm_user = choice(["thomas", "roobal"])
    send_song_fasade(channel, last_fm_user, token)


def send_song_fasade(channel, last_fm_user, token):
    update_songs_distribution()
    slack_bot = SlackMessageBot(channel=channel, token=token)
    song = ApiAdapter(slack_bot)
    song.my_logging.log().info("Get random song")

    with open(os.path.join(FOLDER_PATH, "%sList.Txt" % last_fm_user), 'r') as f:
        songs = f.read().split("\n")

    song_title = choice(songs)

    url = get_youtube_url(song_title.strip())

    song.sent_messages(["%s song" % last_fm_user, "Title: %s" % song_title, "Total songs count: %s" % len(songs)])
    song.sent_messages([url])


if __name__ == '__main__':
    token = sys.argv[1]
    main(channel="mitologia-bobrów", token=token)

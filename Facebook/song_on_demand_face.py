import os
import random
import sys
import time
from os import listdir
from os.path import isfile, join

from fbchat import ThreadType

from Facebook.song_of_the_day_facebook_message import SongOfTheDayFace
from Utils.Songs_.Songs import FILE_PATH
from Utils.utils import create_file_if_not_exist, log, save_history
from Youtube.Youtube_Bot import get_youtube_URL


def check_queue(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    ids = []
    for file in files:
        file_name = os.path.splitext(file)[0]
        checked = path + "checked\\" + file_name + "_checked.txt"
        create_file_if_not_exist(checked)
        f2 = open(checked, 'r+')
        with open(path + "\\" + file, 'r') as f:
            for line in f.readlines():
                line_found = any(line in line2 for line2 in f2)
                if not line_found:
                    print(file_name)
                    ids.append(file_name)
                    f2.write(line + '\n')
    return ids


def main(song_, thread_id, thread_type):
    f = open(FILE_PATH, 'r')
    log("Get random song")
    songs = f.read()
    songs = songs.split("\n")
    ran = random.randrange(len(songs))
    song_title = songs[ran]
    log(song_title)
    save_history(song_title, "FacebookMessage.txt")
    song_.set_up()
    url = get_youtube_URL(song_.driver, song_title.strip())
    song_.sent_song([url], thread_id, "SONG ON DEMAND", thread_type)
    song_.tear_down()


def thread(song_, path, thread_type):
    threads = check_queue(path)
    for thread in threads:
        main(song_, thread, thread_type)


if __name__ == '__main__':
    path1 = 'D:\Google_drive\QueueGroup\\'
    path2 = 'D:\Google_drive\QueueUser\\'

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]

    song = SongOfTheDayFace()
    song.login_FB(user, passw)

    while 1:
        thread(song, path1, ThreadType.GROUP)
        thread(song, path2, ThreadType.USER)
        time.sleep(60)

import os
import random
import sys
import time
from functools import partial
from multiprocessing import Process
from os import listdir
from os.path import isfile, join
from threading import Thread

from fbchat import ThreadType

from Facebook.facebook_monitor import FaceThreadMonitor, start_monitor
from Facebook.song_of_the_day_facebook_message import SongOfTheDayFace
from Utils.Songs_.Songs import FILE_PATH
from Utils.file_utils import create_file_if_not_exist
from Utils.utils import log, save_history
from Youtube.Youtube_Bot import get_youtube_URL


def get_ides(path, file, checked):
    ids = []
    file_name = os.path.splitext(file)[0]
    f2 = open(checked, 'r+')
    with open(path + "\\" + file, 'r') as f:
        for line in f.readlines():
            if not any(line in line2 for line2 in f2):
                print("File name: %s" % file_name)
                ids.append(file_name)
                f2.write(line + '\n')
    return ids


def check_queue(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    checked_list = [path + "checked\\" + os.path.splitext(file)[0] + "_checked.txt" for file in files]
    map(create_file_if_not_exist, checked_list)
    partial_get_ides = partial(get_ides, path)
    thread_ides = list(map(partial_get_ides, files, checked_list))
    print("Thread ID's %s" % thread_ides)
    return thread_ides


def send_song(song_, thread_id, thread_type):
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


def send_songs_threads(song_, path, thread_type):
    while 1:
        threads_ids = check_queue(path)
        threads = []
        if threads_ids:
            for thread_id in threads_ids:
                try:
                    thread = Thread(target=send_song, args=(song_, thread_id, thread_type))
                    threads.append(thread)
                    thread.start()
                except Exception:
                    import traceback
                    traceback.print_exc()

            for thread in threads:
                thread.join()
        else:
            time.sleep(60)


if __name__ == '__main__':
    PHASE = ["[SONG]", "[song]"]
    path1 = 'E:\Google_drive\QueueGroup\\'
    path2 = 'E:\Google_drive\QueueUser\\'
    THREADID1 = '1252344071467839'  # group
    THREADID2 = '100000471818643'  # user

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    song = SongOfTheDayFace()
    song.login_FB(user, passw)

    fm1 = FaceThreadMonitor(song.face_bot, path1, THREADID1)
    fm2 = FaceThreadMonitor(song.face_bot, path2, THREADID2)

    process1 = Process(target=start_monitor, args=(PHASE, [fm1, fm2]))
    process2 = Process(target=send_songs_threads, args=(song, path1, ThreadType.GROUP))
    process3 = Process(target=send_songs_threads, args=(song, path2, ThreadType.USER))

    for process in [process1, process2, process3]:
        process.start()

    for process in [process1, process2, process3]:
        process.join()

    while 1:
        pass

import sys
import time
from multiprocessing import Process
from queue import Queue
from random import choice
from threading import Thread

from fbchat import ThreadType

from Facebook.facebook_monitor import FaceThreadMonitor, start_monitor
from Facebook.song_of_the_day_facebook_message import SongOfTheDayFace
from Utils.Songs_.Songs import FILE_PATH
from Utils.utils import MyLogging
from Youtube.Youtube_Bot import get_youtube_url

# from os.path import isfile, join

time_stumps = []

mylogging = MyLogging()


def check_queue(queue):
    msg = queue.get()
    msq = msg.split(',')
    time_stump = msq[1]
    if time_stump not in time_stumps:
        time_stumps.append(time_stump)
    return msq[0]


def send_song(song_, thread_id, thread_type):
    with open(FILE_PATH, 'r') as f:
        songs = f.read()
    song_title = choice(songs.split("\n"))
    song_.set_up()
    url = get_youtube_url(song_.driver, song_title.strip())
    song_.sent_song([url], thread_id, "SONG ON DEMAND", thread_type)
    song_.tear_down()


def send_songs_threads(song_, thread_type, queue):
    threads = []
    while 1:
        if queue.not_empty:
            threads_ids = check_queue(queue)
            if threads_ids:
                for thread_id in threads_ids:
                    try:
                        thread = Thread(target=send_song, args=(song_, thread_id, thread_type))
                        threads.append(thread)
                        thread.start()
                    except Exception as ex:
                        mylogging.log().error(ex)

                for thread in threads:
                    thread.join()
        else:
            time.sleep(2)


if __name__ == '__main__':
    queue = Queue()
    queue.not_empty()
    PHASE = ["[SONG]", "[song]"]

    THREADID1 = '1252344071467839'  # group
    THREADID2 = '100000471818643'  # user

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    song = SongOfTheDayFace()
    song.login_FB(user, passw)

    fm1 = FaceThreadMonitor(song.face_bot, THREADID1)
    # fm2 = FaceThreadMonitor(song.face_bot, THREADID2)

    # process1 = Process(target=start_monitor, args=(PHASE, [fm1, fm2], queue))
    process1 = Process(target=start_monitor, args=(PHASE, [fm1], queue))
    process2 = Process(target=send_songs_threads, args=(song, ThreadType.GROUP, queue))

    for process in [process1, process2]:
        process.start()

    for process in [process1, process2]:
        process.join()

    while 1:
        pass

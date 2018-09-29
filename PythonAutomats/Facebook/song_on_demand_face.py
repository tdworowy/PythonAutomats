import os
import re
import sys
import time
from multiprocessing import Process, Queue, Manager
from random import choice

from Facebook.facebook_monitor import FaceThreadMonitor, start_monitor
from Facebook.song_of_the_day_facebook_message import ApiAdapter
from Songs.last_fm_parser import FILE_PATH
from Utils.file_utils import write_to_file_no_duplicates
from Youtube.Youtube_bot_requests import get_youtube_url
from fbchat import ThreadType


def check_queue(queue, time_stumps):
    msg = queue.get()
    msq = msg.split(',')
    time_stump = re.search(r"\d+", msq[1]).group()
    if time_stump not in time_stumps:
        time_stumps.append(time_stump)
        return re.search(r"\d+", msq[0]).group()


def send_song(api):
    with open(FILE_PATH, 'r') as f:
        songs = f.read()
    song_title = choice(songs.split("\n"))
    url = get_youtube_url(song_title.strip())
    api.sent_messages([url])


def send_songs_threads(api):
    while 1:
        if not queue.empty():
            thread_id = check_queue(queue, time_stumps)
            if thread_id:
                api.thread_id = thread_id
                send_song(api)
        else:
            time.sleep(60)


def save_time_stumps(file, time_stumps):
    while 1:
        if time_stumps:
            write_to_file_no_duplicates(file, time_stumps)
        time.sleep(120)


if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]

    file = os.path.dirname(os.path.abspath(__file__)) + "\\time_stumps.txt"
    manager = Manager()
    time_stumps = manager.list()
    try:
        if os.path.isfile(file) and os.path.getsize(file) > 0:
            with open(file) as f:
                time_stumps = manager.list(f.read().split('\n'))
        else:
            open(file, 'w').close()

        queue = Queue()

        PHASE = ["[SONG]", "[song]"]

        THREADID1 = '1252344071467839'  # group
        # THREADID2 = '100000471818643'  # user

        face_bot = FaceBookMessageBot(thread_id=THREADID1, thread_type=ThreadType.GROUP)
        song = ApiAdapter(api=face_bot)
        song.login(user, passw)

        fm1 = FaceThreadMonitor(face_bot, THREADID1)
        # fm2 = FaceThreadMonitor(song.face_bot, THREADID2)

        # process1 = Process(target=start_monitor, args=(PHASE, [fm1, fm2], queue))
        process1 = Process(target=start_monitor, args=(PHASE, [fm1], queue))
        process2 = Process(target=send_songs_threads, args=(song, ThreadType.GROUP, queue, time_stumps))
        process3 = Process(target=save_time_stumps, args=(file, time_stumps))

        for process in [process1, process2, process3]:
            process.start()

        for process in [process1, process2, process3]:
            process.join()

        while 1:
            pass
    finally:
        if time_stumps:
            write_to_file_no_duplicates(file, time_stumps)

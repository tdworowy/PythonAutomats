import sys
import time

from Facebook.facebookAPI import FaceBookMessageBot
from Utils.utils import create_file_if_not_exist


class FaceThreadMonitor:
    def __init__(self, email, passw, path):
        self.face_bot = FaceBookMessageBot()
        self.face_bot.login(email, passw)
        self.path = path

    def monitor_threads(self, phrase, threads_ids):
        for thread in threads_ids:
            for massage in self.face_bot.get_messages(thread):
                if str(massage.text) == phrase:
                    path = self.path + thread + ".txt"
                    create_file_if_not_exist(path)
                    with open(path, 'r+') as f:
                        msg = str((massage.text, massage.timestamp))
                        line_found = any(msg in line for line in f)
                        if not line_found:
                            f.write(msg + "\n")
                            f.flush()

    def set_thread_ides(self, threadIDs):
        self.threadIDs = threadIDs


def start_monitor(phraze, face_thread_monitor_list):
    while 1:
        for ftm in face_thread_monitor_list:
            ftm.monitor_threads(phraze, ftm.threadIDs)
            time.sleep(60)


if __name__ == '__main__':
    # THREADIDs = ['1252344071467839','100000471818643']
    THREADIDs1 = ['1252344071467839']  # group
    THREADIDs2 = ['100000471818643']  # user

    user = sys.argv[1]
    passw = sys.argv[2] + " " + sys.argv[3]
    path1 = 'D:\Google_drive\QueesGroup\\'
    path2 = 'D:\Google_drive\QueesUser\\'

    fm1 = FaceThreadMonitor(user, passw, path1)
    fm1.set_thread_ides(THREADIDs1)

    fm2 = FaceThreadMonitor(user, passw, path2)
    fm2.set_thread_ides(THREADIDs2)

    start_monitor("[SONG]", [fm1, fm2])

import time
from threading import Thread

from Utils.utils import create_file_if_not_exist


class FaceThreadMonitor:
    def __init__(self, face_bot, path, thread_ID):
        self.face_bot = face_bot
        self.path = path
        self.thread_ID = thread_ID

    def monitor_thread(self, phrases):
        for massage in self.face_bot.get_messages(self.thread_ID): #TODO optimize (on event)
            if str(massage.text) in phrases:
                path = self.path + self.thread_ID + ".txt"#TODO change to queue
                create_file_if_not_exist(path)
                with open(path, 'r+') as f:
                    msg = str((massage.text, massage.timestamp))
                    line_found = any(msg in line for line in f)
                    if not line_found:
                        f.write(msg + "\n")
                        f.flush()

    def monitor(self, phrase):
        while 1:
            self.monitor_thread(phrase)
            time.sleep(300)


def start_monitor(phraze, face_thread_monitor_list):
        threads = []
        for ftm in face_thread_monitor_list:
            try:
                thread = Thread(target=ftm.monitor, args=(phraze,))
                threads.append(thread)
                thread.start()
            except Exception:
                import traceback
                traceback.print_exc()

        for thread in threads:
            thread.join()


import time
from threading import Thread

from Utils.utils import MyLogging

mylogging = MyLogging()


class FaceThreadMonitor:
    def __init__(self, face_bot, thread_ID):
        self.face_bot = face_bot
        self.thread_ID = thread_ID

    def monitor_thread(self, phrases, queue):
        for message in self.face_bot.get_messages(self.thread_ID):
            if str(message.text) in phrases:
                msg = str((self.thread_ID, message.timestamp))
                queue.put(msg)

    def monitor(self, phrase, queue):
        while 1:
            self.monitor_thread(phrase, queue)
            time.sleep(300)


def start_monitor(phraze, face_thread_monitor_list, queue):
    threads = []
    for ftm in face_thread_monitor_list:
        try:
            thread = Thread(target=ftm.monitor, args=(phraze, queue))
            threads.append(thread)
            thread.start()
        except Exception as ex:
            mylogging.log().error(ex)

    for thread in threads:
        thread.join()

import calendar
import logging
import os
import time
from datetime import date

history_path = "E:\Google_drive\Songs\History"

loggers = []


class MyLogging:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s|%(asctime)s|%(message)s")


    @staticmethod
    def claer_loggers():
        while loggers: loggers.pop()

    def log(self, path=os.path.dirname(os.path.abspath(__file__)) + "\\log.log"):
        for logger in loggers:
            if path in [handler.baseFilename for handler in logger.handlers if
                                             hasattr(handler, 'baseFilename')]:
                return logger
        else:

            file_handler = logging.FileHandler(path)
            file_handler.setFormatter(logging.Formatter("%(levelname)s|%(asctime)s|%(message)s"))
            file_handler.setLevel(logging.DEBUG)

            new_logger = logging.getLogger("Logger%s" % get_millis())
            new_logger.setLevel(logging.DEBUG)
            new_logger.addHandler(file_handler)

            loggers.append(new_logger)
            return new_logger

    def save_history(self, text, file):
        self.log(history_path + file).info(text)

    def log_result(self, test_name, result):
        message = "Name: {x} Result {y}".format(x=test_name, y=result)
        self.log("TestsResultLog.txt").info(message)


def create_dir(context, name):
    if not os.path.exists(name):
        os.makedirs(name)


def take_screenshot(context, path, file):
    context.driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def take_screenshot_(driver, path, file):
    driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def message_by_time():
    date_today = date.today()
    return "Song for " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()) + " [AUTO] "


def characters(frm, to):
    return ','.join([chr(x) for x in range(frm, to)])  # max 1114111


def get_millis():
    return int(round(time.time() * 1000))



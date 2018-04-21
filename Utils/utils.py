import calendar
import logging
import os
import time
from datetime import date

history_path = "E:\Google_drive\Songs\History"


class MyLogging:
    def __init__(self):
        logging.basicConfig(format="%(levelname)s|%(asctime)s|%(message)s")
        self.loggers = []
        self.index = 1

    def log(self, path=os.path.dirname(os.path.abspath(__file__)) + "\\log.log"):
        file_handler = logging.FileHandler(path)
        file_handler.setFormatter(logging.Formatter("%(levelname)s|%(asctime)s|%(message)s"))
        file_handler.setLevel(logging.DEBUG)

        for logger in self.loggers:

            if file_handler.baseFilename in [handler.baseFilename for handler in logger.handlers if
                                             hasattr(handler, 'baseFilename')]:
                return logger
        else:
            new_logger = logging.getLogger("Logger%s" % self.index)
            self.index += 1
            new_logger.setLevel(logging.DEBUG)
            new_logger.addHandler(file_handler)
            self.loggers.append(new_logger)
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
    mylogging = MyLogging()
    date_today = date.today()
    mylogging.log("Today is: " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()))
    return "Song for " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()) + " [AUTO] "


def characters(frm, to):
    return ','.join([chr(x) for x in range(frm, to)])  # max 1114111


def get_millis():
    return int(round(time.time() * 1000))


if __name__ == "__main__":
    mylogging = MyLogging()
    mylogging.log("log1.log").info("TEST")
    mylogging.log("log2.log").info("TEST2")
    mylogging.log("log3.log").info("TEST3")

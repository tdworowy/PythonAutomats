import calendar
import logging
import os
import time
from datetime import date

history_path = "E:\Google_drive\Songs\History"

logging.basicConfig(format="	%(levelname)s|%(asctime)s|%(message)s ")


def log(path=os.path.dirname(os.path.abspath(__file__)) + "\\log.log"):
    file_handler = logging.FileHandler(path)
    # stream_handler = logging.StreamHandler()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)
    return logger


def save_history(text, file):
    log(history_path + file).info(text)


def log_result(test_name, result):
    message = "Name: {x} Result {y}".format(x=test_name, y=result)
    log("TestsResultLog.txt").info(message)


def create_dir(context, name):
    if not os.path.exists(name):
        os.makedirs(name)


def take_screenshot(context, path, file):
    context.driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def take_screenshot_(driver, path, file):
    driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def message_by_time():
    date_today = date.today()
    log("Today is: " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()))
    return "Song for " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()) + " [AUTO] "


def characters(frm, to):
    return ','.join([chr(x) for x in range(frm, to)])  # max 1114111


def get_millis():
    return int(round(time.time() * 1000))

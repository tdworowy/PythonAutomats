import calendar
import os
import time
from datetime import date

history_path = "D:\Google_drive\Songs\History"


def log(text, path=os.path.dirname(os.path.abspath(__file__)) + "\\log.txt"):
    try:
        text = str(text)
        time_stump = time.strftime('%Y-%m-%d %H:%M:%S')
        log = time_stump + " " + text + "\n"
        print(log)
        print(path)
        with open(path, "a") as logFile:
            logFile.write(log)
    except Exception as ex:
        print("ERROR while logging")
        print(str(ex))
        # raise RuntimeError


def save_history(text, file):
    log(text, history_path + file)


def log_result(test_name, result):
    message = "Name: {x} Result {y}".format(x=test_name, y=result)
    print(message)
    log(message, "TestsResultLog.txt")


def create_dir(context, name):
    if not os.path.exists(name):
        os.makedirs(name)


def take_screenshot(context, path, file):
    context.driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def take_screenshot_(driver, path, file):
    driver.save_screenshot(path + file.replace(' ', '_') + '.png')


def mesage_by_time():
    date_today = date.today()
    log("Today is: " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()))
    return "Song for " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()) + " [AUTO] "


def characters(frm, to):
    return ','.join([chr(x) for x in range(frm, to)])  # max 1114111


def create_file_if_not_exist(path):
    if not os.path.isfile(path):
        open(path, 'w').close()


def write_to_file_no_duplicates(path, elements):
    with (open(path, 'a')) as f1, (open(path, 'r')) as f2:
        for ele in elements:
            in_file = [line.strip() for line in f2.readlines()]
            # print("if %s not in %s " %(ele,list))
            if ele not in in_file:
                f1.write(ele + '\n')
            f2.seek(0)


def get_milis():
    return int(round(time.time() * 1000))

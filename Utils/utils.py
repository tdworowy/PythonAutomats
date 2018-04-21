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
        self.milis = lambda: int(round(time.time() * 1000))

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
            new_logger = logging.getLogger("Logger%s" % self.milis())
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
    mylogging = MyLogging()
    date_today = date.today()
    mylogging.log("Today is: " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()))
    return "Song for " + str(calendar.day_name[date_today.weekday()]) + " " + str(date.today()) + " [AUTO] "


def characters(frm, to):
    return ','.join([chr(x) for x in range(frm, to)])  # max 1114111


def get_millis():
    return int(round(time.time() * 1000))


if __name__ == "__main__":
    import unittest
    import os


    class LogsTests(unittest.TestCase):

        def setUp(self):
            loggers = []
            self.mylogging = MyLogging()

        #
        # def tearDown(self):
        #     os.system('del /f /q *.log')

        def test_logging_single(self):
            pref = "test_logging_single"

            message = "TEST"
            self.mylogging.log(pref + "log1.log").info(message)
            with open(pref + "log1.log") as f1:
                assert message in f1.read()

        def test_logging_more_times(self):
            pref = "test_logging_more_times"
            message1 = "TEST1"
            message2 = "TEST2"
            self.mylogging.log(pref + "log1.log").info(message1)
            self.mylogging.log(pref + "log1.log").info(message2)
            with open(pref + "log1.log") as f1:
                assert message1 in f1.read()
                assert message2 in f1.read()

        def test_logging_more_fies(self):
            pref = "test_logging_more_fies"
            message1 = "TEST1"
            message2 = "TEST2"
            message3 = "TEST3"
            self.mylogging.log(pref + "log1.log").info(message1)
            self.mylogging.log(pref + "log2.log").info(message2)
            self.mylogging.log(pref + "log3.log").info(message3)

            with open(pref + "log1.log") as f1:
                assert message1 in f1.read()
                assert message2 not in f1.read()
                assert message3 not in f1.read()
            with open(pref + "log2.log") as f1:
                assert message1 not in f1.read()
                assert message2 in f1.read()
                assert message3 in f1.read()
            with open(pref + "log3.log") as f1:
                assert message1 not in f1.read()
                assert message2 not in f1.read()
                assert message3 in f1.read()

        def test_logging_more_fies_and_loggers(self):
            pref = "test_logging_more_fies_and_loggers"
            mylogging2 = MyLogging()
            message1 = "TEST1"
            message2 = "TEST2"
            message3 = "TEST3"
            message4 = "TEST4"
            self.mylogging.log(pref + "log1.log").info(message1)
            self.mylogging.log(pref + "log2.log").info(message2)
            self.mylogging.log(pref + "log3.log").info(message3)

            mylogging2.log(pref + "log1.log").info(message4)

            with open(pref + "log1.log") as f1:
                assert message1 in f1.read()
                assert message4 in f1.read()
                assert message2 not in f1.read()
                assert message3 not in f1.read()
            with open(pref + "log2.log") as f1:
                assert message1 not in f1.read()
                assert message4 not in f1.read()
                assert message2 in f1.read()
                assert message3 in f1.read()
            with open(pref + "log3.log") as f1:
                assert message1 not in f1.read()
                assert message4 not in f1.read()
                assert message2 not in f1.read()
                assert message3 in f1.read()


    unittest.main()

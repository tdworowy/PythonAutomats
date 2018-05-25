import unittest

from Utils.utils import MyLogging


class LogsTests(unittest.TestCase):

    def setUp(self):
        self.mylogging = MyLogging()

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
            lines = f1.read()
        assert message1 in lines
        assert message2 in lines

    def test_logging_more_fies(self):
        pref = "test_logging_more_fies"
        message1 = "TEST1"
        message2 = "TEST2"
        message3 = "TEST3"
        self.mylogging.log(pref + "log1.log").info(message1)
        self.mylogging.log(pref + "log2.log").info(message2)
        self.mylogging.log(pref + "log3.log").info(message3)

        with open(pref + "log1.log") as f1:
            lines = f1.read()
        assert message1 in lines
        assert message2 not in lines
        assert message3 not in lines
        with open(pref + "log2.log") as f1:
            lines = f1.read()
        assert message1 not in lines
        assert message2 in lines
        assert message3 not in lines
        with open(pref + "log3.log") as f1:
            lines = f1.read()
        assert message1 not in lines
        assert message2 not in lines
        assert message3 in lines

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
            lines = f1.read()
        assert message1 in lines
        assert message4 in lines
        assert message2 not in lines
        assert message3 not in lines
        with open(pref + "log2.log") as f1:
            lines = f1.read()
        assert message1 not in lines
        assert message4 not in lines
        assert message2 in lines
        assert message3 not in lines

        with open(pref + "log3.log") as f1:
            lines = f1.read()
        assert message1 not in lines
        assert message4 not in lines
        assert message2 not in lines
        assert message3 in lines


if __name__ == '__main__':
    unittest.main()

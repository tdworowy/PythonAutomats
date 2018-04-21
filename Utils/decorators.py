import sys

from Utils.utils import MyLogging


def catch_assertion(f):
    def func(self):
        mylogging = MyLogging()
        try:
            res = f(self)
            mylogging.log_result(f.__name__, "Pass")
            return res
        except AssertionError:
            mylogging.log_result(f.__name__, "Fail")
            self.fail("fail")

    return func


def log_exception(rize=True):
    def _log_exception(f):
        def func(*args, **kwargs):
            mylogging = MyLogging()
            try:
                return f(*args, **kwargs)
            except Exception as err:
                mylogging.log().error(str(err))
                mylogging.log().error(sys.exc_info())
                if rize: raise RuntimeError

        return func

    return _log_exception

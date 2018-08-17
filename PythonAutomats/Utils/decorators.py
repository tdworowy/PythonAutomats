import sys

from Utils.utils import MyLogging


def catch_assertion(f):
    def func(self):
        my_logging = MyLogging()
        try:
            res = f(self)
            my_logging.log_result(f.__name__, "Pass")
            return res
        except AssertionError:
            my_logging.log_result(f.__name__, "Fail")
            self.fail("fail")

    return func


def log_exception(rize=True):
    def _log_exception(f):
        def func(*args, **kwargs):
            my_logging = MyLogging()
            try:
                return f(*args, **kwargs)
            except Exception as err:
                my_logging.log().error(str(err))
                my_logging.log().error(sys.exc_info())
                if rize: raise RuntimeError

        return func

    return _log_exception

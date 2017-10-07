import sys

from Utils.utils import logResult, log


def catch_assertion(f):
    def func(self):
        try:
            f(self)
            logResult(f.__name__, "Pass")
        except AssertionError:
            logResult(f.__name__, "Fail")
            self.fail("fail")

    return func


def log_exeption(rize=False):
    def _log_exeption(f):
        def func(*args):
            try:
                f(*args)
            except Exception  as err:
                log(str(err))
                log(sys.exc_info())
                if rize: raise RuntimeError

        return func

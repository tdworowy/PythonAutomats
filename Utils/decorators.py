import sys

from Utils.utils import log_result, log


def catch_assertion(f):
    def func(self):
        try:
            res = f(self)
            log_result(f.__name__, "Pass")
            return res
        except AssertionError:
            log_result(f.__name__, "Fail")
            self.fail("fail")

    return func


def log_exception(rize=True):
    def _log_exception(f):
        def func(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as err:
                log().error(str(err))
                log().error(sys.exc_info())
                if rize: raise RuntimeError

        return func

    return _log_exception

from Utils.utils import logResult, log


def catchAssertion(f):
    def func(self):
        try:
            f(self)
            logResult(f.__name__, "Pass")
        except AssertionError:
            logResult(f.__name__, "Fail")
            self.fail("fail")
    return func



def logExeption(f):
    def func(*args):
        try:
            f(*args)
        except Exception  as err:
            log(str(err))
            raise err
        finally:
            quit()
    return func
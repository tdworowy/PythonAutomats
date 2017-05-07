from Utils.utils import logResult


def catchAssertion(f):
    def func(self):
        try:
            f(self)
            logResult(f.__name__, "Pass")
        except AssertionError:
            logResult(f.__name__, "Fail")
            self.fail("fail")
    return func
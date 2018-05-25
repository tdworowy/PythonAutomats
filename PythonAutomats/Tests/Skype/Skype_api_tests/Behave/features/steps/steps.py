from unittest.mock import MagicMock

from Skype.skype_api_ import SkypeApi
from behave import *
from skpy import Skype


@given('User logged to skype API')
def log_in(context):
    user = "Test_user"
    passw = "Test_password"
    SkypeApi.skype = MagicMock(Skype)
    context.skype_api = SkypeApi(user, passw)

#TODO make mock work
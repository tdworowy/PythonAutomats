from time import sleep

from facepy import utils
from fbchat import Client
from fbchat.models import *


class FaceBookMessageBot:
    def login(self, email, password):
        self.email = email
        self.passwd = password
        self.client = Client(email, password)

    def send_message(self, message, thread_id, thread_type=ThreadType.GROUP, repeat_on_fail=7):
        # self.client.sendMessage(message, thread_id=thread_id, thread_type=thread_type)
        repeat = repeat_on_fail
        try:
            self.client.send(Message(text=message), thread_id=thread_id, thread_type=thread_type)
        except Exception as ex:
            print(str(ex))
            if repeat > 0:
                sleep(30)
                self.login(self.email, self.passwd)
                self.send_message(message, thread_id, thread_type, repeat - 1)
            else:
                raise ex

    def send_message_my(self, message):
        thread_type = ThreadType.USER
        self.client.sendMessage(message, thread_id=self.client.client_id, thread_type=thread_type)

    def get_messages(self, thread_id, limit=30, before=None):
        return self.client.fetchThreadMessages(thread_id, limit, before)

    def logout(self):
        self.client.logout()

    @staticmethod
    def get_aut_token(app_id, app_secred):  # not log user token
        return utils.get_application_access_token(app_id, app_secred)

    def get_user_id(self):
        return self.client.client_id

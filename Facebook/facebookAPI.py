from fbchat import Client
from fbchat.models import *


class FaceBookMessageBot:
    def logIn(self,email,password):
        self.client = Client(email, password)

    def sendMessage(self,message,thread_id):
        thread_type = ThreadType.GROUP
        self.client.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

    def sendMessageMy(self, message):
        thread_type = ThreadType.USER
        self.client.sendMessage(message, thread_id=self.client.client_id, thread_type=thread_type)

    def logout(self):
        self.client.logout()



# '1252344071467839'


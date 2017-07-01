from fbchat import Client
from fbchat.models import *


class FaceBookMessageBot():
    def logIn(self,email,password):
        self.client = Client(email, password)

    def sendMessage(self,message,threadID):
        thread_id = threadID
        thread_type = ThreadType.GROUP
        self.client.client.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

    def logout(self):
        self.client.logout()



# '1252344071467839'

from facepy import utils
from fbchat import Client
from fbchat.models import *


class FaceBookMessageBot:
    def logIn(self,email,password):
        self.client = Client(email, password)

    def sendMessage(self,message,thread_id,thread_type = ThreadType.GROUP):
            self.client.sendMessage(message, thread_id=thread_id, thread_type=thread_type)

    def sendMessageMy(self, message):
        thread_type = ThreadType.USER
        self.client.sendMessage(message, thread_id=self.client.client_id, thread_type=thread_type)

    def getMessages(self,thread_id,limit = 30,before=None):
        return self.client.fetchThreadMessages(thread_id,limit,before)


    def logout(self):
        self.client.logout()

    def getAutToken(self,appid,app_secred):#not loged user token
        return utils.get_application_access_token(appid, app_secred)

    def getUserID(self):
        return self.client.client_id




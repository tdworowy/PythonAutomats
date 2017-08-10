import re

from skpy import Skype


def untilExeption(f):
    def func(self,*args):
     while 1:
        try:
          f(self,*args)
        except Exception:
            break
    return func


class skypeApi:
    def __init__(self,login,passw):
        self.skype = Skype(login, passw)


    def getChats(self):
        return self.skype.chats.recent()

    def getChatIDByTopic(self,name):
        for chat in  self.skype.chats.recent().values():
            if hasattr(chat, 'topic') and chat.topic == name: return chat



    def getAllMessages(self,name):
        messages = []
        chat = self.getChatIDByTopic(name)
        self.__getAllMessages(chat,messages)
        return messages

    @untilExeption
    def __getAllMessages(self,chat,list):
        list.extend(chat.getMsgs())
        print(list)


    def getLinks(self,name):
        links = []
        for msg in self.getAllMessages(name):
            match = re.search(r'href=[\'"]?([^\'" >]+)', msg.content)
            if match:
               links.append(match.group(1))
        return links


if __name__ == '__main__':
    sa = skypeApi("mrcripted","JudasPrist1970")
    # print(sa.getMessages("Learning is an awesome journey"))
    print(sa.getLinks("Learning is an awesome journey"))

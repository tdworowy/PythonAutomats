import re

from skpy import Skype


class SkypeApi:
    def clear_chats(self):
        self.skype = Skype(self.login, self.passw)
        self.chats = None

    def __init__(self, login, passw):
        self.login = login
        self.passw = passw
        self.clear_chats()

    def get_contact_ID(self, first, last):
        for contact in self.skype.contacts.search(first + ' ' + last):
            if contact.name.first == first and contact.name.last == last:
                print("Name: %s ID: %s" % (contact.name, contact.id))
                return contact.id

    def get_chats(self):
        return self.skype.chats.recent()

    def get_chat_by_topic(self, names):
        self.chats = set()
        for chat in self.skype.chats.recent().values():
            print(chat)
            if hasattr(chat, 'topic') and chat.topic in names:
                print("Found: %s" % chat)
                self.chats.add(chat)

    def set_chats(self, chatsNames):
        if self.chats == None:
            self.get_chat_by_topic(chatsNames)
        print("Chats in cache: %s" % self.chats)

    def sned_message(self, message):
        for chat in self.chats:
            chat.sendMsg(message)

    def get_all_messages(self, name):
        messages = []
        chat = self.get_chat_by_topic(name)
        self.__get_all_messages(chat[0], messages)
        return messages

    def __get_all_messages(self, chat, list_):
        lastLen = 0
        while 1:
            list_.extend(chat.getMsgs())
            if lastLen == len(list_):
                break
            else:
                lastLen = len(list_)

    def add_person(self, chatName, SkypeID):
        chat = self.get_chat_by_topic(chatName)
        chat.addMember(SkypeID)

    def get_links(self, name):
        links = []
        for msg in self.get_all_messages(name):
            match = re.search(r'href=[\'"]?([^\'" >]+)', msg.content)
            if match:
                links.append(match.group(1))
        return links


if __name__ == '__main__':
    pass
    # user = sys.argv[1]
    # passw = sys.argv[2]
    # sa = skypeApi(user,passw)
    # links = sa.getLinks("Learning is an awesome journey")
    # writeToFileNoDuplicates("D:\Google_drive\links_from_skype\links.txt",links)

import re
import sys

from skpy import Skype


class SkypeApi:
    def clear_chats(self):
        self.skype = Skype(self.login, self.passw)
        self.chats = None

    def __init__(self, login, passw):
        self.login = login
        self.passw = passw
        self.clear_chats()

    def get_contact_id(self, first, last):
        for contact in self.skype.contacts.search(first + ' ' + last):
            if contact.name.first == first and contact.name.last == last:
                print("Name: %s ID: %s" % (contact.name, contact.id))
                return contact.id

    def get_chats(self):
        return self.skype.chats.recent()

    def add_chat_by_topic(self, names):
        self.chats = set()
        for chat in self.skype.chats.recent().values():
            print(chat)
            if hasattr(chat, 'topic') and chat.topic in names:
                print("Found: %s" % chat)
                self.chats.add(chat)

    def set_chats(self, chats_names):
        if self.chats is None:
            self.add_chat_by_topic(chats_names)
        print("Chats in cache: %s" % self.chats)

    def send_message(self, message):
        for chat in self.chats:
            chat.sendMsg(message)

    def get_all_messages(self, name):
        messages = []
        self.add_chat_by_topic(name)
        self.__get_all_messages(list(self.chats)[0], messages)
        return messages

    def __get_all_messages(self, chat, list_):
        last_len = 0
        while 1:
            list_.extend(chat.getMsgs())
            if last_len == len(list_):
                break
            else:
                last_len = len(list_)

    def add_person(self, chat_name, skype_id):
        self.add_chat_by_topic(chat_name)
        list(self.chats)[0].addMember(skype_id)

    def get_links(self, name):
        links = []
        for msg in self.get_all_messages(name):
            match = re.search(r'href=[\'"]?([^\'" >]+)', msg.content)
            if match:
                links.append(match.group(1))
        return links


if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    sa = SkypeApi(user, passw)
    print(sa.skype.conn.connected)
    # links = sa.getLinks("Learning is an awesome journey")
    # writeToFileNoDuplicates("D:\Google_drive\links_from_skype\links.txt",links)

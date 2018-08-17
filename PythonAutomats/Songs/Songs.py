from Utils.utils import MyLogging


class SongOfTheDay:
    def __init__(self, api):
        self.api = api
        self.my_logging = MyLogging()

    def login(self, login, passw):
        self.api.login(login, passw)

    def sent_messages(self, messages):
        self.my_logging.log().info(messages)
        for message in messages:
            self.api.send_message(message)

    def sent_songs(self, songs_urls):
        for songURL in songs_urls:
            self.my_logging.log().info(songURL)
            self.api.send_message(songURL)

    def save_history(self, message, file):
        self.my_logging.save_history(message, file)

    def logout(self):
        self.api.logout()
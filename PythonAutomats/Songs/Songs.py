from Utils.utils import MyLogging


class SongOfTheDay:
    def __init__(self, api):
        self.api = api
        self.mylogging = MyLogging()

    def login(self, login, passw):
        self.api.login(login, passw)

    def sent_messages(self, messages):
        for message in messages:
            self.mylogging.log().info(messages)
            self.api.send_message(message)

    def sent_songs(self, songs_urls):
        for songURL in songs_urls:
            self.mylogging.log().info(songURL)
            self.api.send_message(songURL)

    def save_history(self, message, file):
        self.mylogging.save_history(message, file)

    def logout(self):
        self.api.logout()
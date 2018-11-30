from slackclient import SlackClient


class SlackMessageBot:
    def __init__(self, channel, token):
        self.channel = channel
        self.client = SlackClient(token)

    def login(self, email, password):
        pass

    def send_message(self, message):
        self.client.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=message
        )

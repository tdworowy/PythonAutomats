from slackclient import SlackClient


class SlackMessageBot:
    def __init__(self, channel):
       # slack_token = "k23bJLBblTRldt0R6KzYq6Ue"
        slack_token = "xoxp-492033747443-492033747795-493574383846-9177db6ea00ed7bccf26fc0aaf48de22"
        self.channel = channel
        self.client = SlackClient(slack_token)

    def login(self, email, password):
        pass

    def send_message(self, message):
        self.client.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=message
        )

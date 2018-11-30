from slackclient import SlackClient


# https://api.slack.com/apps/AEG1HTY2X/oauth?success=1
class SlackMessageBot:
    def __init__(self, channel):
        slack_token = "xoxp-492033747443-492033747795-491994425636-5ab2826053d45947d6665050bb37584d"
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

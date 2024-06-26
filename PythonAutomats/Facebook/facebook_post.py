import facebook

# from Utils.utils import log
from Utils.utils import MyLogging
from facepy import utils


class FaceBookPost:
    @staticmethod
    def get_aut_token(app_id, app_secred):
        return utils.get_application_access_token(app_id, app_secred)

    def __init__(self, page_id, app_id, app_secret):
        self.cfg = {"page_id": page_id, "access_token": "TODO"}
        self.mylogging = MyLogging()

    def facebook_post(self, message):
        api = self.get_api()
        self.mylogging.log().info("Post message %s" % message)
        status = api.put_wall_post(message)
        self.mylogging.log().info(status)

    def get_api(self):
        graph = facebook.GraphAPI(self.cfg["access_token"])

        resp = graph.get_object("me/accounts")
        page_access_token = None
        for page in resp["data"]:
            if page["id"] == self.cfg["page_id"]:
                page_access_token = page["access_token"]
        graph = facebook.GraphAPI(page_access_token)
        return graph

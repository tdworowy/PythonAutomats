import facebook
from facepy import utils

from Utils.utils import log


class FaceBookPost:
    def getAutToken(self,appid, app_secred):
        return utils.get_application_access_token(appid, app_secred)


    def __init__(self,pageID, appid, app_secred):
        self.cfg = {
            "page_id": pageID,
            "access_token":"TODO"
        }

    def facebookPost(self,message):
        api = self.get_api()
        log("Post message %s" % message)
        status = api.put_wall_post(message)
        log(status)

    def get_api(self):
        graph = facebook.GraphAPI(self.cfg['access_token'])

        resp = graph.get_object('me/accounts')
        page_access_token = None
        for page in resp['data']:
            if page['id'] == self.cfg['page_id']:
                page_access_token = page['access_token']
        graph = facebook.GraphAPI(page_access_token)
        return graph

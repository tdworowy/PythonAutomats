import random

import pynder

from Facebook.FacebookToken import get_access_token
from Utils.Songs_.Songs import getFilePath
from Utils.utils import log
from Youtube.YoutubeBot import getYoutubeURL


class TinderMessageBot:

    def logIn(self, id, token):
        self.session = pynder.Session(facebook_id=id, facebook_token=token)


    def getMatches(self):
        return self.session.matches()

    def getNerby(self):
        return self.session.nearby_users()


if __name__ == '__main__':

    f = open(getFilePath(), 'r')
    log("Get random song")
    songsList = f.read()
    songsList = songsList.split("\n")

    ran = random.randrange(len(songsList))
    log(songsList[ran])
    url = getYoutubeURL(song.driver, songsList[ran].strip())

    token = get_access_token("dworowytomasz@gmail.com","Jefferson Airplane1966!")
    tm = TinderMessageBot()
    tm.logIn(100001295284655,token)
    matches = list(tm.getMatches())
    print(matches[0])
    if matches[0] =='Ilona':
      matches[0].message("Automatyczna piosenka dla Ilony :D")
      matches[0].message("Automatyczna piosenka dla Ilony :D")

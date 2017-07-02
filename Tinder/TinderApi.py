
import pynder


class TinderMessageBot:

    def logIn(self, id, token):
        self.session = pynder.Session(facebook_id=id, facebook_token=token)


    def getMatches(self):
        return self.session.matches()

    def getNerby(self):
        return self.session.nearby_users()




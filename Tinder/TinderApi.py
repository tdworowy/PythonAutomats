
import pynder
from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Facebook.facebookID import getFacebookID
from Facebook.facebookToken import get_access_token


class TinderMessageBot:

    def logIn(self, id, token):
        self.session = pynder.Session(facebook_id=id, facebook_token=token)


    def getMatches(self):
        return self.session.matches()

    def getNerby(self):
        return self.session.nearby_users(100)


    def getFBfriends(self):
        return self.session.get_fb_friends()

    def updateLocation(self,latitude,longitude):
        self.session.update_location(latitude,longitude)



if __name__ == "__main__":

    login = ''
    passw = ''
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    token = get_access_token(login, passw)
    tm = TinderMessageBot()
    id = getFacebookID(driver, 'tomasz.dworowy')
    driver.quit()
    tm.logIn(id, token)
    # for friend in tm.getFBfriends():
    #     print(friend)

    for neer in tm.getNerby():
        try:
            print('%s, %s' % (neer.id,neer.distance_km))
        except Exception as ex:
            print(ex)


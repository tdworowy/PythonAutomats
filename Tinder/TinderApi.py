
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
        return self.session.nearby_users(200)


    def getFBfriends(self):
        return self.session.get_fb_friends()

    def updateLocation(self,latitude,longitude):
        self.session.update_location(latitude,longitude)


def printMatches(tm):
    for match in tm.getMatches():
        print(match)



def logIn(login,passw,fbname):

    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    token = get_access_token(login, passw)
    tm = TinderMessageBot()
    id = getFacebookID(driver, fbname)
    driver.quit()
    tm.logIn(id, token)
    return tm


def printFBFriends(tm):
    for friend in tm.getFBfriends():
        print(friend)
        user = friend.get_tinder_information()
        print(user.name)
        print(user.bio)
        print(user.photos_obj)

def likeFB(tm,friendName):

   for friend in tm.getFBfriends():
     if  friend.get_tinder_information().name == friendName:
         user = friend.get_tinder_information()
         for near in tm.getNerby():
             print('check %s %s' % (near.name, near.id))
             print('fb friedn ID: %s' % user.id)
             if user.id == near.id:
                print(near.name)
                near.like()

def getNearData(tm):
    return ['Name: %s \nage: %s\ndistance: %s\nbio: %s\nphotos: %s' % (near.name,near.age,near.distance_km,near.bio,near.photos_obj) for near in tm.getNerby()]




if __name__ == "__main__":

    tm = logIn('','','')
    # likeFB(tm,"")
    # printFBFriends(tm)
    printMatches(tm)


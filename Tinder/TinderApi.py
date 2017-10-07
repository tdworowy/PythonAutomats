import pynder
from selenium import webdriver

from ChromedriverFolder.driverPath import get_driver_path
from Facebook.facebookID import getFacebookID
from Facebook.facebookToken import get_access_token


class TinderMessageBot:
    def logIn(self, id, token):
        self.session = pynder.Session(facebook_id=id, facebook_token=token)

    def get_matches(self):
        return self.session.matches()

    def get_nerby(self):
        return self.session.nearby_users(200)

    def get_FB_friends(self):
        return self.session.get_fb_friends()

    def update_location(self, latitude, longitude):
        self.session.update_location(latitude, longitude)


def print_matches(tm):
    for match in tm.get_matches():
        print(match)


def logIn(login, passw, fbname):
    chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    token = get_access_token(login, passw)
    tm = TinderMessageBot()
    id = getFacebookID(driver, fbname)
    driver.quit()
    tm.logIn(id, token)
    return tm


def print_FB_friends(tm):
    for friend in tm.get_FB_friends():
        print(friend)
        user = friend.get_tinder_information()
        print(user.name)
        print(user.bio)
        print(user.photos_obj)


def like_FB(tm, friendName):
    for friend in tm.get_FB_friends():
        if friend.get_tinder_information().name == friendName:
            user = friend.get_tinder_information()
            for near in tm.get_nerby():
                print('check %s %s' % (near.name, near.id))
                print('fb friedn ID: %s' % user.id)
                if user.id == near.id:
                    print(near.name)
                    near.like()


def get_near_data(tm):
    return ['Name: %s \nage: %s\ndistance: %s\nbio: %s\nphotos: %s' % (
    near.name, near.age, near.distance_km, near.bio, near.photos_obj) for near in tm.get_nerby()]


if __name__ == "__main__":
    tm = logIn('', '', '')
    # likeFB(tm,"")
    print_FB_friends(tm)
    # printMatches(tm)

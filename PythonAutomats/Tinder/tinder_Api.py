import pynder
from Chrome_Driver_Folder.driver_path import get_driver_path
from Facebook.facebook_id import get_facebook_ID
from Facebook.facebook_token import get_access_token
from Utils.utils import MyLogging
from selenium import webdriver


class TinderMessageBot:
    def logIn(self, id, token):
        self.session = pynder.Session(facebook_id=id, facebook_token=token)

    def get_matches(self):
        return self.session.matches()

    def get_nearby(self):
        return self.session.nearby_users(200)

    def get_FB_friends(self):
        return self.session.get_fb_friends()

    def update_location(self, latitude, longitude):
        self.session.update_location(latitude, longitude)


class TinderAdapter:

    def __init__(self, name, receivers, driver, tiderBot):
        self.tm = tiderBot
        self.name = name
        self.mylogging = MyLogging()
        self.receivers = receivers
        self.driver = driver

    def login(self, login, passw):
        token = get_access_token(login, passw)

        id = get_facebook_ID(self.driver, self.name)
        self.tm.logIn(id, token)

    def send_message(self, message):
        for match in self.tm.get_matches():
            if match.user.name in self.receivers:
                self.mylogging.log("Send message to: %s " % match.user.name)
                match.message("[ Auto song for: %s :D ]" % match.user.name)
                match.message(message)


def print_matches(tm):
    for match in tm.get_matches():
        print(match)


def login(login, passw, fbname):
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    token = get_access_token(login, passw)
    tm = TinderMessageBot()
    id = get_facebook_ID(driver, fbname)
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
            for near in tm.get_nearby():
                print('check %s %s' % (near.name, near.id))
                print('fb friedn ID: %s' % user.id)
                if user.id == near.id:
                    print(near.name)
                    near.like()


def get_near_data(tm):
    return ['Name: %s \nage: %s\ndistance: %s\nbio: %s\nphotos: %s' % (
        near.name, near.age, near.distance_km, near.bio, near.photos_obj) for near in tm.get_nearby()]


if __name__ == "__main__":
    tm = login('', '', '')
    # likeFB(tm,"")
    print_FB_friends(tm)
    # printMatches(tm)

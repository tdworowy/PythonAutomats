import sys

from selenium import webdriver
from selenium.webdriver import ActionChains

from chromedriverFolder.driverPath import getDriverPath
from skype.SkypeBot.SkypeBot import SkypeBot


class AddPersonToChat:


    def setUp(self):
        chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chromeDriverPath)
        self.driver.implicitly_wait(2)
        self.skypeBot = SkypeBot(self.driver)

    def __init__(self):
        self.setUp()

    def login(self,authentication):
        self.skypeBot.login(authentication)

    def addPersonToChat(self,name,chat="Szopy Reaktywacja!"):
        self.skypeBot.select("Echo")
        self.skypeBot.select(chat)
        self.skypeBot.addPersonButtonClick()

        actions = ActionChains(self.driver)
        actions.send_keys(name)
        actions.perform()
        self.skypeBot.searchItemClick(name)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    user = sys.argv[1]
    passw = sys.argv[2]
    ap = AddPersonToChat()
    ap.login([user,passw])
    # while(1):
    ap.addPersonToChat("Adam Franica")

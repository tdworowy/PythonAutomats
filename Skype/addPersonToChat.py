import sys

from selenium import webdriver
from selenium.webdriver import ActionChains

from ChromedriverFolder.driverPath import getDriverPath
from Skype.SkypeBot import SkypeBot
from Utils.utils import log


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

    def addPersonToChat(self,names,chat="Szopy Reaktywacja!"):

        self.skypeBot.select("Echo")
        self.skypeBot.select(chat)
        self.skypeBot.addPersonButtonClick()
        actions = ActionChains(self.driver)
        for name in names:
            log("Try add %s to chat %s" % (name, chat))
            actions.send_keys(name)
            actions.perform()
            self.skypeBot.searchItemClick(name)
            # takeScreenshot_(self.driver,"D:\\","Add_ADAM")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    ap = AddPersonToChat()
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
        ap = AddPersonToChat()
        ap.login([user,passw])
        # while(1):
        ap.addPersonToChat(["Adam Franica"])
    except Exception as ex:
        log(str(ex))

    finally:
        ap.tearDown()

from selenium import webdriver
from selenium.webdriver import ActionChains

from SkypeBot.SkypeBot import SkypeBot
from chromedriverFolder.driverPath import getDriverPath


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

    def addPersonToChat(self,name,chat="A smiechom i szopom nie było konca"):
        self.skypeBot.select("Echo")
        self.skypeBot.select(chat)
        self.skypeBot.addPersonButtonClick()

        actions = ActionChains(self.driver)
        actions.send_keys(name)
        actions.perform()
        self.skypeBot.searchItemClick(name)


    def tearDown(self):
        self.driver.quit()

    def checkContent(self):
        self.skypeBot

if __name__ == '__main__':

    ap = AddPersonToChat()
    ap.login(["mrcripted","JudasPrist1970"])
    while(1):
       ap.addPersonToChat("Adam Franica")

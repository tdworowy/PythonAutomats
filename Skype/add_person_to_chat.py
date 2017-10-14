import sys

from Chrome_Driver_Folder.driver_path import get_driver_path
from Skype.skype_bot import SkypeBot
from Utils.utils import log
from selenium import webdriver
from selenium.webdriver import ActionChains


class AddPersonToChat:
    def set_up(self):
        chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(2)
        self.skype_bot = SkypeBot(self.driver)

    def __init__(self):
        self.set_up()

    def login(self, authentication):
        self.skype_bot.login(authentication)

    def add_person_to_chat(self, names, chat="Szopy Reaktywacja!"):
        self.skype_bot.select("Echo")
        self.skype_bot.select(chat)
        self.skype_bot.add_person_button_click()
        actions = ActionChains(self.driver)
        for name in names:
            log("Try add %s to chat %s" % (name, chat))
            actions.send_keys(name)
            actions.perform()
            self.skype_bot.search_item_click(name)

    def tear_down(self):
        self.driver.quit()


if __name__ == '__main__':

    ap = AddPersonToChat()
    try:
        user = sys.argv[1]
        passw = sys.argv[2]
        ap = AddPersonToChat()
        ap.login([user, passw])
        # while(1):
        ap.add_person_to_chat(["Adam Franica"])
    except Exception as ex:
        log(str(ex))

    finally:
        ap.tear_down()

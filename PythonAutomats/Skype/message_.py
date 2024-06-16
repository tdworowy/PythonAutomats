from Chrome_Driver_Folder.driver_path import get_driver_path
from Skype.skype_bot import SkypeBot
from Utils.decorators import log_exception
from Utils.utils import characters
from selenium import webdriver


@log_exception
def main(login, password):
    chrome_driver_path = get_driver_path() + "\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(2)
    skype_bot = SkypeBot(driver)

    authentication = [login, password]
    skype_bot.login(authentication)
    skype_bot.select("Echo")
    skype_bot.select("Szopy Reaktywacja!")
    skype_bot.send_message_to_selected(characters(10000, 10500))


if __name__ == "__main__":
    main("", "")

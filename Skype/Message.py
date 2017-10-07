from selenium import webdriver

from ChromedriverFolder.driverPath import get_driver_path
from Skype.SkypeBot import SkypeBot
from Utils.decorators import log_exeption
from Utils.utils import characters


@log_exeption
def main(login, password):
     chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
     driver = webdriver.Chrome(chromeDriverPath)
     driver.implicitly_wait(2)
     skypeBot = SkypeBot(driver)

     autentycation = [login,password]
     skypeBot.login(autentycation)
     skypeBot.select("Echo")
     skypeBot.select("Szopy Reaktywacja!")
     skypeBot.send_message_to_selected(characters(10000, 10500))



if __name__ == '__main__':
   main("", "")


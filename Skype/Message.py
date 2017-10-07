from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Skype.SkypeBot import SkypeBot
from Utils.decorators import log_exeption
from Utils.utils import characters


@log_exeption
def main(login, password):
     chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
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


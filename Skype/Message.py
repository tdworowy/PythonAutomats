from selenium import webdriver

from ChromedriverFolder.driverPath import getDriverPath
from Skype.SkypeBot import SkypeBot
from Utils.decorators import logExeption
from Utils.utils import characters


@logExeption
def main(login, password):
     chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
     driver = webdriver.Chrome(chromeDriverPath)
     driver.implicitly_wait(2)
     skypeBot = SkypeBot(driver)

     autentycation = [login,password]
     skypeBot.login(autentycation)
     skypeBot.select("Echo")
     skypeBot.select("Szopy Reaktywacja!")
     skypeBot.sendMessageToSelected(characters(10000,10500))



if __name__ == '__main__':
   main("", "")


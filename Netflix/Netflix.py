import sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ChromedriverFolder.driverPath import getDriverPath

netflixUrl = "https://www.netflix.com/browse"
generUrl = "https://www.netflix.com/browse/genre/"

emailField = (By.NAME, 'email')
passwordField = (By.NAME, 'password')
genreTitle = (By.CLASS_NAME, 'genreTitle')
avatar = (By.CLASS_NAME, 'avatar-wrapper')

PATH = "D:\Google_drive\\Netflix\cat.txt"

def getAllCategories(login,password):
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    driver.get(netflixUrl)
    driver.find_element(*emailField).send_keys(login)
    driver.find_element(*passwordField).send_keys(password)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()

    driver.find_element(*avatar).click()
    f = open(PATH, 'a')
    for i in range(0,999999):

        driver.get(generUrl+str(i))
        try:
            category = driver.find_element(*genreTitle).text
            f.write((category,i))
            f.flush()

        except:
            continue



if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    getAllCategories(user,passw)

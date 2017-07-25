import os
import sys

from ChromedriverFolder.driverPath import getDriverPath
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

netflixUrl = "https://www.netflix.com/browse"
generUrl = "https://www.netflix.com/browse/genre/"

emailField = (By.NAME, 'email')
passwordField = (By.NAME, 'password')
genreTitle = (By.CLASS_NAME, 'genreTitle')
avatar = (By.CLASS_NAME, 'avatar-wrapper')

PATH = "D:\Google_drive\\Netflix\cat.txt"
lastCount = "D:\Google_drive\\Netflix\count.txt"

def getAllCategories(login,password):
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    driver.get(netflixUrl)
    driver.find_element(*emailField).send_keys(login)
    driver.find_element(*passwordField).send_keys(password)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()

    driver.find_element(*avatar).click()

    if os.path.isfile(lastCount) :
        f2 = open(lastCount).readline()
        start = str(int(f2)+1)
    else:
        f2 = open(lastCount,'a')
        start = '0'

    f = open(PATH, 'a')
    for i in range(int(start),999999):

        driver.get(generUrl+str(i))
        try:
            category = driver.find_element(*genreTitle).text
            f.write("%s,%s\n" % (i,category))
            f.flush()
            f2.write(str(i))
            f2.flush()
        except Exception as ex:
            print(ex)
            continue



if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    getAllCategories(user,passw)

import sys

from chromedriverFolder.driverPath import getDriverPath
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


def getAllCategories(login,password):
    chromeDriverPath = getDriverPath() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    driver.get(netflixUrl)
    driver.find_element(*emailField).send_keys(login)
    driver.find_element(*passwordField).send_keys(password)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()

    driver.find_element(*avatar).click()
    result = []
    for i in range(1,9999):

        driver.get(generUrl+str(i))
        try:
            category = driver.find_element(*genreTitle).text
            result.append((category,i))
        except:
            continue

    return result



if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    print(getAllCategories(user,passw))

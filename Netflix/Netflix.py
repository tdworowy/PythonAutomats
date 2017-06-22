from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from chromedriverFolder.driverPath import getDriverPath

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
    f = open("cat.txt", 'a')
    for i in range(10100,12000):

        driver.get(generUrl+str(i))
        try:
            category = driver.find_element(*genreTitle).text
            print((category,i),file=f)
            f.flush()

        except:
            continue



if __name__ == '__main__':
    # user = sys.argv[1]
    # passw = sys.argv[2]
    getAllCategories("dworowytomasz@gmail.com","JudasPrist1970")

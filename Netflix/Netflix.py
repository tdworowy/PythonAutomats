import os
import sys

from ChromedriverFolder.driverPath import get_driver_path
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

NETFLIX_URLl = "https://www.netflix.com/browse"
GENRE_URL = "https://www.netflix.com/browse/genre/"

EMAIL_FIELD = (By.NAME, 'email')
PASSWORD_FIELD = (By.NAME, 'password')
GENRE_NAME = (By.CLASS_NAME, 'genreTitle')
AVATAR = (By.CLASS_NAME, 'avatar-wrapper')

PATH = "D:\Google_drive\\Netflix\cat.txt"
LAST_COUNT = "D:\Google_drive\\Netflix\count.txt"


def get_all_categories(login, password):
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get(NETFLIX_URLl)
    driver.find_element(*EMAIL_FIELD).send_keys(login)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()

    driver.find_element(*AVATAR).click()

    if os.path.isfile(LAST_COUNT):
        f2 = open(LAST_COUNT).readline()
        start = str(int(f2) + 1)
    else:
        start = '0'

    f = open(PATH, 'a')

    for i in range(int(start), 99999):

        driver.get(GENRE_URL + str(i))
        try:
            category = driver.find_element(*GENRE_NAME).text
            f.write("%s,%s\n" % (i, category))
            f.flush()

        except Exception as ex:
            print(ex)
            continue
        finally:
            print("Count: %s" % str(i))
            with open(LAST_COUNT, 'w') as f2:
                f2.write(str(i))
                f2.flush()


if __name__ == '__main__':
    user = sys.argv[1]
    passw = sys.argv[2]
    get_all_categories(user, passw)

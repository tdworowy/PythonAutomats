import logging
import os
import sys

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

NETFLIX_URLl = "https://www.netflix.com/browse"
GENRE_URL = "https://www.netflix.com/browse/genre/"

EMAIL_FIELD = (By.NAME, "userLoginId")
PASSWORD_FIELD = (By.NAME, "password")
GENRE_NAME = (By.CLASS_NAME, "genreTitle")
AVATAR = (By.CLASS_NAME, "avatar-wrapper")

PATH = "cat.txt"
LAST_COUNT = "count.txt"
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(
    executable_path="../drivers/geckodriver.exe", options=options
)


def wait_for_element(locator: By, element: str, wait: int):
    wait = WebDriverWait(driver, wait)
    wait.until(expected_conditions.visibility_of_element_located((locator, element)))


def find_element(locator: By, element: str, wait: int | float) -> WebElement:
    wait_for_element(locator, element, wait)
    return driver.find_element(locator, element)


def get_all_categories(login: str, password: str):
    driver.get(NETFLIX_URLl)
    find_element(*EMAIL_FIELD, wait=5).send_keys(login)
    find_element(*PASSWORD_FIELD, wait=5).send_keys(password)

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()

    find_element(*AVATAR, wait=5).click()

    if os.path.isfile(LAST_COUNT):
        last_category_number_file = open(LAST_COUNT).readline()
        start = str(int(last_category_number_file) + 1)
    else:
        start = "0"

    with open(PATH, "a") as categories_file:
        for i in range(int(start), 99999):
            driver.get(GENRE_URL + str(i))
            try:
                category = find_element(*GENRE_NAME, wait=0.5).text
                categories_file.write(f"{i}: {category}\n")
                categories_file.flush()

            except Exception as ex:
                logging.exception(ex)
                continue
            finally:
                print(f"Count: {str(i)}")
                with open(LAST_COUNT, "w") as last_category_number_file:
                    last_category_number_file.write(str(i))
                    last_category_number_file.flush()


if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    get_all_categories(user, passw)

import time

from Chrome_Driver_Folder.driver_path import get_driver_path
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def get_facebook_ID(driver, fullname):
    driver.get('https://findmyfbid.com/')
    actions = ActionChains(driver)

    input = driver.find_element_by_name("url")
    input.click()
    input.send_keys("https://www.facebook.com/" + fullname)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    result = driver.current_url
    result = result[result.index("ss/") + 3:]

    return result


if __name__ == '__main__':
    chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    print(get_facebook_ID(driver, 'tomasz.dworowy'))

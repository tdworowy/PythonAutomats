import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from ChromedriverFolder.driverPath import get_driver_path


def getFacebookID(driver, fullname):
    driver.get('https://findmyfbid.com/')
    actions = ActionChains(driver)

    input = driver.find_element_by_name("url")
    input.click()
    input.send_keys("https://www.facebook.com/"+fullname)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)
    resoult = driver.current_url
    resoult = resoult[resoult.index("ss/")+3:]

    return resoult


if __name__=='__main__':
    chromeDriverPath = get_driver_path() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chromeDriverPath)
    print(getFacebookID(driver,'tomasz.dworowy'))
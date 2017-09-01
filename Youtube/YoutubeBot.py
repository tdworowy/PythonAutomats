import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def actionSend(driver,txt):
    actions = ActionChains(driver)
    actions.send_keys(txt)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)


def getYoutubeURL(driver, phraze):
    driver.get('https://www.youtube.com')
    actionSend(driver,phraze)
    time.sleep(2)
    firstResoult = driver.find_element_by_css_selector("h3 a")

    firstResoult.click()
    time.sleep(1)

    return driver.current_url


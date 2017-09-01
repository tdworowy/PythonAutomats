import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def getYoutubeURL(driver, phraze):
    driver.get('https://www.youtube.com')
    actions = ActionChains(driver)

    input = driver.find_element_by_id("search")
    input.click()
    input.send_keys(phraze)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)
    firstResoult = driver.find_element_by_css_selector("h3 a")

    firstResoult.click()
    time.sleep(1)

    return driver.current_url
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def action_send(driver, txt):
    actions = ActionChains(driver)
    actions.send_keys(txt)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(1)


def get_youtube_URL(driver, phrase):
    driver.get('https://www.youtube.com')
    action_send(driver, phrase)
    time.sleep(2)
    firstResult = driver.find_element_by_css_selector("div[id='title-wrapper'] h3")
    firstResult.click()
    time.sleep(1)

    return driver.current_url


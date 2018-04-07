from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def action_send(driver, txt):
    actions = ActionChains(driver)
    actions.send_keys(txt)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    WebDriverWait(driver, 1)


def get_youtube_url(driver, phrase):
    driver.get('https://www.youtube.com')
    driver.implicitly_wait(10)
    action_send(driver, phrase)
    first_result = driver.find_element_by_css_selector("div[id='title-wrapper'] h3 a")
    first_result.click()
    WebDriverWait(driver, 3,ignored_exceptions=ElementNotVisibleException).until(lambda x: x.find_element_by_id("subscribe-button"))
    url = driver.current_url
    try:
        driver.quit()
    except Exception as ex:
        print(ex)

    return url

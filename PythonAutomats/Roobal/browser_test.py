from Chrome_Driver_Folder.driver_path import get_driver_path
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = get_driver_path() + '\\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
title = (By.CLASS_NAME, "text-logo")
while 1:
    driver.get("http://robertmarek.pl")
    WebDriverWait(driver, 10, ignored_exceptions=ElementNotVisibleException).until(lambda x: x.find_element(*title))



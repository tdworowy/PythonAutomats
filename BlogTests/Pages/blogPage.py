from BlogTests.Pages.postPage import POSTPage
from selenium.webdriver.common.by import By


class BlogPage:
    def initialize_elements(self):
        self.latest_posts = (By.CSS_SELECTOR, "ul[id='Latest_posts'] li")

    def __init__(self, driver_arg):
        self.initialize_elements()
        self.driver = driver_arg

    def open_latest_post(self):
        latests_posts = self.driver.find_elements(*self.latest_posts)
        latests_posts[0].click()
        return POSTPage(self.driver)

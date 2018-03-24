from selenium.webdriver.common.by import By

from Blog_Tests.Pages.post_page import POSTPage


class BlogPage:
    def initialize_elements(self):
        self.latest_posts = (By.CSS_SELECTOR, "ul[id='Latest_posts'] li")

    def __init__(self, driver_arg):
        self.initialize_elements()
        self.driver = driver_arg

    def open_latest_post(self):
        latest_posts = self.driver.find_elements(*self.latest_posts)
        latest_posts[0].click()
        return POSTPage(self.driver)

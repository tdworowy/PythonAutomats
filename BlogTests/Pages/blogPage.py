from BlogTests.Pages.postPage import POSTPage
from selenium.webdriver.common.by import By


class BlogPage:
    def initializeElements(self):
        self.latestPosts = (By.CSS_SELECTOR, "ul[id='Latest_posts'] li")

    def __init__(self, driverArg):
        self.initializeElements()
        self.driver = driverArg


    def openLatestPost(self):
        latestposts = self.driver.find_elements(*self.latestPosts)
        latestposts[0].click()
        return POSTPage(self.driver)

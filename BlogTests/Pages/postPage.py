from selenium.webdriver.common.by import By


class POSTPage:
    def initializeElements(self):
        self.latestPosts = (By.CSS_SELECTOR, "ul[id='Latest_posts'] li")

    def __init__(self, driverArg):
        self.initializeElements()
        self.driver = driverArg

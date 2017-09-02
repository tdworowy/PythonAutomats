from selenium.webdriver.common.by import By


class POSTPage:
    def initializeElements(self):
        self.title = (By.ID, "title")
        self.tags = (By.CSS_SELECTOR, "p[class='tags'] a")
        self.content = (By.CSS_SELECTOR, "div[id='content'] p")

    def __init__(self, driverArg):
        self.initializeElements()
        self.driver = driverArg

    def checkPost(self,POSTobj):
        assert  self.driver.find_element(*self.title).text == POSTobj.title
        assert  self.driver.find_element(*self.content).text == POSTobj.body
        assert self.driver.find_elements(*self.tags).text == POSTobj.tags

from selenium.webdriver.common.by import By


class POSTPage:
    def initializeElements(self):
        self.title = (By.ID, "title")
        self.tags = (By.CSS_SELECTOR, "p[class='tags'] a")
        self.content = (By.CSS_SELECTOR, "div[id='postContent'] p")

    def __init__(self, driverArg):
        self.initializeElements()
        self.driver = driverArg

    def checkPost(self,POSTobj):
        titleText = self.driver.find_element(*self.title).text
        contentText = self.driver.find_element(*self.content).text
        tags  = self.driver.find_element(*self.tags).text
        print("Check if %s == %s" % (titleText,POSTobj.title))
        assert  titleText == POSTobj.title
        print("Check if %s == %s" % (contentText, POSTobj.body))
        assert  contentText == POSTobj.body
        print("Check if %s == %s" % (tags, POSTobj.tags))
        assert  tags == POSTobj.tags

from selenium.webdriver.common.by import By

class AdminPage:

    def initializeElements(self):
        self.siteName = (By.LINK_TEXT, 'Django administration')
        self.addPostButton = (By.CSS_SELECTOR, "tr[class='model-post'] a[class='addlink']")
        self.titleImput = (By.NAME, 'title')
        self.bodyTextArea = (By.NAME, 'body')
        self.tagsImput = (By.NAME, 'tags')
        self.authorImput = (By.NAME, 'author')
        self.savePostButton = (By.NAME, '_save')

    def __init__(self,driverArg):
        self.initializeElements()
        self.driver = driverArg


    def addPost(self,POSTobj):
        self.driver.find_element(*self.addPostButton).click()

        title = self.driver.find_element(*self.titleImput)
        body = self.driver.find_element(*self.bodyTextArea)
        tags = self.driver.find_element(*self.tagsImput)
        author = self.driver.find_element(*self.authorImput)

        title.click()
        title.send_keys(POSTobj.title)

        body.click()
        body.send_keys(POSTobj.body)

        author.click()
        author.send_keys(POSTobj.author)

        tags.click()
        tags.send_keys(POSTobj.tags)

        self.driver.find_element(*self.savePostButton).click()

    def chakIFPageOpened(self):
        assert self.driver.find_element(*self.siteName).is_displayed()
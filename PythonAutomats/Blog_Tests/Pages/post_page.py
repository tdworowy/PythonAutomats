from selenium.webdriver.common.by import By


class POSTPage:
    def initialize_elements(self):
        self.title = (By.ID, "title")
        self.tags = (By.CSS_SELECTOR, "p[class='tags'] a")
        self.content = (By.CSS_SELECTOR, "div[id='postContent'] p")

    def __init__(self, driver_arg):
        self.initialize_elements()
        self.driver = driver_arg

    def check_post(self, POST_obj):
        title_text = self.driver.find_element(*self.title).text
        content_text = self.driver.find_element(*self.content).text
        tags = self.driver.find_element(*self.tags).text
        print("Check if %s == %s" % (title_text, POST_obj.title))
        assert title_text == POST_obj.title
        print("Check if %s == %s" % (content_text, POST_obj.body))
        assert content_text == POST_obj.body
        print("Check if %s == %s" % (tags, POST_obj.tags))
        assert tags == POST_obj.tags

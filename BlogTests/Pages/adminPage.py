from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdminPage:
    def initialize_elements(self):
        self.site_name = (By.LINK_TEXT, 'Django administration')
        self.add_post_button = (By.CSS_SELECTOR, "tr[class='model-post'] a[class='addlink']")
        self.title_imput = (By.NAME, 'title')
        self.body_text_area = (By.NAME, 'body')
        self.tags_imput = (By.NAME, 'tags')
        self.author_imput = (By.NAME, 'author')
        self.save_post_button = (By.NAME, '_save')
        self.status_select = (By.ID, 'id_status')

        self.now = (By.LINK_TEXT, "Now")

    def __init__(self, driver_arg):
        self.initialize_elements()
        self.driver = driver_arg

    def add_post(self, POST_obj):
        self.driver.find_element(*self.add_post_button).click()

        title = self.driver.find_element(*self.title_imput)
        body = self.driver.find_element(*self.body_text_area)
        tags = self.driver.find_element(*self.tags_imput)
        author = self.driver.find_element(*self.author_imput)
        status_select = self.driver.find_element(*self.status_select)

        title.click()
        title.send_keys(POST_obj.title)

        body.click()
        body.send_keys(POST_obj.body)

        author.click()
        author.send_keys(POST_obj.author)

        tags.click()
        tags.send_keys(POST_obj.tags)
        if POST_obj.publish:
            select = Select(status_select)
            select.select_by_value('published')

        self.driver.find_element(*self.now).click()
        self.driver.find_element(*self.save_post_button).click()

    def check_if_page_opened(self):
        assert self.driver.find_element(*self.site_name).is_displayed()

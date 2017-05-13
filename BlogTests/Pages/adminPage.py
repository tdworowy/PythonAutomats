from selenium.webdriver.common.by import By

class AdminPage:

    def initializeElements(self):
        self.siteName = (By.LINK_TEXT, 'Django administration')

    def __init__(self,driverArg):
        self.initializeElements()
        self.driver = driverArg

    def chakIFPageOpened(self):
        assert self.driver.find_element(*self.siteName).is_displayed()

class CalculatorElements:
    def __init__(self, driverArg):
        self.driver = driverArg

    def openCalculator(self):
        return self.driver.find_element_by_link_text("Scientific")

    def scientificCalculator(self):
        return self.driver.find_element_by_id("sciout")

    def result(self):
        return self.driver.find_element_by_id("sciOutPut")

    def numberButton(self,number):
        return self.driver.find_element_by_css_selector("span[onclick=\"r(%s)\"]" % number)

    def plusButton(self):
        return  self.driver.find_element_by_css_selector("span[onclick=\"r('+')\"]")

    def equalButton(self):
        return  self.driver.find_element_by_css_selector("span[onclick=\"r('=')\"]")
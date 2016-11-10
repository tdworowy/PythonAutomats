import time

class CalculatorElements:
    def __init__(self, driverArg):
        self.driver = driverArg

    def openCalculator(self):
        return self.driver.find_element_by_link_text("Scientific")

    def scientificCalculator(self):
        return self.driver.find_element_by_id("sciout")

    def calcResult(self):
        return self.driver.find_element_by_id("sciOutPut")

    def numberButton(self, number):
        return self.driver.find_element_by_css_selector("span[onclick=\"r(%s)\"]" % number)

    def plusButton(self):
        return self.driver.find_element_by_css_selector("span[onclick=\"r('+')\"]")

    def changeButton(self):
        return self.driver.find_element_by_css_selector("span[onclick=\"r('+/-')\"]")

    def equalButton(self):
        return self.driver.find_element_by_css_selector("span[onclick=\"r('=')\"]")

    def sum(self, num1, num2, result):
        res = str(result) + "."

        self.numberButton(abs(num1)).click()
        if num1 < 0: self.changeButton().click()

        self.plusButton().click()

        self.numberButton(abs(num2)).click()
        if num2 < 0: self.changeButton().click()
        self.equalButton().click()
        time.sleep(1)
        if res == self.calcResult().text:
            return True
        else:
            return False

    def bigSum(self, num1, num2, result):
        res = str(result) + "."

        num1List = list(str(num1))
        num2List = list(str(num2))
        for n in num1List:
            self.numberButton(n).click()

        self.plusButton().click()
        for n in num2List:
            self.numberButton(n).click()

        self.equalButton().click()
        time.sleep(1)
        if res == self.calcResult().text:
            return True
        else:
            return False

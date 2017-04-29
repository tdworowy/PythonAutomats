from selenium.webdriver.common.by import By


class CalculatorElements:

    def initializeElements(self):
        self.ScientificCalculatorLink = (By.LINK_TEXT,'Scientific Calculator')
        self.ScientificCalculator = (By.ID,"sciout")
        self.CalculatorResult = (By.ID,"sciOutPut")
        self.PlusButton = (By.CSS_SELECTOR, "span[onclick=\"r('+')\"]")
        self.ChangeButton = (By.CSS_SELECTOR, "span[onclick=\"r('+/-')\"]")
        self.EqualButton = (By.CSS_SELECTOR, "span[onclick=\"r('=')\"]")
        self.NumberButtons = [(By.CSS_SELECTOR, "span[onclick=\"r(%s)\"]" % number) for number in range(0, 10)]



    def __init__(self, driverArg):
        self.driver = driverArg
        self.initializeElements()

    def openCalculator(self):
         self.driver.find_element(*self.ScientificCalculatorLink).click()

    def scientificCalculatorCheck(self):
        return self.driver.find_element(*self.ScientificCalculator).is_displayed()

    def getCalcResult(self):
        return self.driver.find_element(*self.CalculatorResult).text

    def numberButtonClick(self, number):
        self.driver.find_element(*self.NumberButtons[number]).click()

    def plusButtonClick(self):
        self.driver.find_element(*self.PlusButton).click()

    def changeButtonClick(self):
        self.driver.find_element(*self.ChangeButton).click()

    def equalButtonClick(self):
        self.driver.find_element(*self.EqualButton).click()

    def sum(self, num1, num2):
        self.numberButtonClick(abs(num1))
        if num1 < 0: self.changeButtonClick()

        self.plusButtonClick()

        self.numberButtonClick(abs(num2))
        if num2 < 0: self.changeButtonClick()
        self.equalButtonClick()


    def bigSum(self, num1, num2):
        num1List = list(str(num1))
        num2List = list(str(num2))
        self.clickNumbers(num1List)
        self.plusButtonClick()
        self.clickNumbers(num2List)

        self.equalButtonClick()

    def clickNumbers(self,numList):
        for n in numList:
            self.numberButtonClick(int(n))



from Python_Staff.Modules.importStaff import os

from BlogTests.screens.screenPath import getScreenPath


def generateReport():
    screanPath = getScreenPath()
    commend = "allure serve %s "% (screanPath)
    print(commend)
    os.system(commend)

if __name__ == '__main__':
    generateReport()

import os

from BlogTests.screens.screenPath import getScreenPath


def run_behave():
    path = os.path.dirname(os.path.abspath(__file__))
    screanPath = getScreenPath()
    partition = "D:"
    commend ='%s && cd "%s" && behave -f allure_behave.formatter:AllureFormatter -o "%s" ./features' %(partition,path,screanPath)
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    run_behave()

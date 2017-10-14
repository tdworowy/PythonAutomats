import os

from BlogTests.screens.screenPath import get_screen_path


def run_behave():
    path = os.path.dirname(os.path.abspath(__file__))
    screen_path = get_screen_path()
    partition = "D:"
    commend ='%s && cd "%s" && behave -f allure_behave.formatter:AllureFormatter -o "%s" ./features' %(partition,path,screen_path)
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    run_behave()

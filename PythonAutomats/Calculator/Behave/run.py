import os

from Calculator.Behave.screens.screenPath import get_screen_path


def run_behave():
    path = os.path.dirname(os.path.abspath(__file__))
    partition = "E:"
    # commend = partition + " && cd " + path + " && behave"
    commend = '%s && cd "%s" && behave -f allure_behave.formatter:AllureFormatter -o "%s" ./features' % (
        partition, path, get_screen_path())
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    run_behave()
    # input("")

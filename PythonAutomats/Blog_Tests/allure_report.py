import os

from Blog_Tests.screens.screen_path import get_screen_path


def generate_report():
    screen_path = get_screen_path()
    commend = "allure serve %s " % screen_path
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    generate_report()

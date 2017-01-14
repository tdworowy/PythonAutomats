import os


def chromeDriverPath():
    return os.path.dirname(os.path.abspath(__file__))+'\\chromedriver.exe'
import os


def getChromeDriverPath():
    return os.path.dirname(os.path.abspath(__file__))+'\\chromedriver.exe'
import os

from Utils.utils import getMilis
from projectPath import getProjectPath


def runpylint():
     os.system("cd %s && pylint --output-format=json PythonAutomats >> report%s.json" % (getProjectPath(),getMilis()))

if __name__ == '__main__':
    runpylint()
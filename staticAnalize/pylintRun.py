import os
import sys

from Utils.utils import getMilis
from projectPath import getProjectPath


def runpylint(module):
     os.system("cd %s && pylint --output-format=json %s >> report%s.json" % (getProjectPath(),module,getMilis()))

if __name__ == '__main__':
    runpylint(sys.argv[0])
import os
import sys

from Utils.utils import get_milis
from projectPath import getProjectPath


def runpylint(module):
     os.system("cd %s && pylint --output-format=json %s >> report%s.json" % (getProjectPath(), module, get_milis()))

if __name__ == '__main__':
    runpylint(sys.argv[1])
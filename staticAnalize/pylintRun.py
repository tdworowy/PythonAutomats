import os
import sys

from Utils.utils import get_milis
from projectPath import get_project_path


def runpylint(module):
     os.system("cd %s && pylint --output-format=json %s >> report%s.json" % (get_project_path(), module, get_milis()))

if __name__ == '__main__':
    runpylint(sys.argv[1])
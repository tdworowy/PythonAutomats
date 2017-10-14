import os
import sys

from Utils.utils import get_milis
from project_path import get_project_path


def runpy_lint(module):
    os.system("cd %s && pylint --output-format=json %s >> report%s.json" % (get_project_path(), module, get_milis()))


if __name__ == '__main__':
    runpy_lint(sys.argv[1])

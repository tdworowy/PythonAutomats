import os
import sys

from project_path import get_project_path

if __name__ == "__main__":
    sys.path.insert(0, get_project_path())
    os.system("generate_doc.bat")

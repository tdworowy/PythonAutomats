from os import listdir

from os.path import isfile, join


def add_init(path):
    """Add __init__ to all folders"""
    files = [f for f in listdir(path) if isfile(join(path, f))]
    folders =[join(path, f) for f in listdir(path) if not isfile(join(path, f))]
    if "__init__.py" not in files:
        open(path+"\\__init__.py",'w')
    for folder in folders:
        add_init(folder)


if __name__ == "__main__":
    add_init("D:\Python_\PythonAutomats\PythonAutomats")
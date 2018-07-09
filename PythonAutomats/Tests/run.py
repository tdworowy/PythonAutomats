import os


def run():
    path = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files = [f for f in files if "_test" in f]
    list(map(lambda file: os.system(r"python -m pytest --alluredir unit.xml %s" % file), files))


if __name__ == "__main__":
    run()

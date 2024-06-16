import os


def run_behave():
    path = os.path.dirname(os.path.abspath(__file__))
    partition = "E:"
    commend = partition + " && cd " + path + " && behave"
    print(commend)
    os.system(commend)


if __name__ == "__main__":
    run_behave()

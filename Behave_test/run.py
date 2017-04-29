import os

def runBehave():
    path = os.path.dirname(os.path.abspath(__file__))
    partition = "D:"
    commend = partition + " && cd " + path + " && behave"
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    runBehave()
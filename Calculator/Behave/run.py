import os

def runBehave():
    path = os.path.dirname(os.path.abspath(__file__))
    partition = "D:"
    # commend = partition + " && cd " + path + " && behave"
    commend = partition+" && cd "+path + " && behave -i (calculator2)"
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    runBehave()
    input("prompt: ")
import os


def run_behave():
    path = os.path.dirname(os.path.abspath(__file__))
    partition = "D:"
    # commend = partition + " && cd " + path + " && behave"
    commend = '%s && cd "%s" && behave -f allure_behave.formatter:AllureFormatter -o "%s" .\\features' % (
        partition, path, path)
    print(commend)
    os.system(commend)


if __name__ == '__main__':
    run_behave()


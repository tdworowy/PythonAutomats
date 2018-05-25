from subprocess import call

import pip


def generate_reg_txt():
    packages = [dist.project_name for dist in pip.get_installed_distributions()]
    with open("req.txt", 'w') as f:
        for package in packages:
            f.write(package + "\n")


def install_all(file):
    with open(file)as f:
        for line in f.readlines():
            try:
                call("pip install --upgrade " + str(line), shell=True)
            except Exception as ex:
                print(ex)
                continue


if __name__ == "__main__":
    # generate_reg_txt()
    install_all("req.txt")
from subprocess import call

import pip


def update_all():
    packages = [dist.project_name for dist in pip.get_installed_distributions()]
    for package in packages:
        try:
            call("pip install --upgrade " + str(package), shell=True)
        except Exception as Ex:
            print(Ex)
            continue


if __name__ == "__main__":
    update_all()
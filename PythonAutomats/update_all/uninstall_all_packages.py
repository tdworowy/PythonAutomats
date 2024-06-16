from subprocess import call
from pip._internal.operations import freeze


def uninstall_all():
    packages = [dist[: dist.rindex("=") - 1] for dist in freeze.freeze()]
    for package in packages:
        try:
            call("pip uninstall --y " + str(package), shell=True)
        except Exception as Ex:
            print(Ex)
            continue


if __name__ == "__main__":
    uninstall_all()

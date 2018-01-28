import subprocess


def run_artifactory(path_to_bat):
    process = subprocess.Popen(path_to_bat, shell=True, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()
    print(process.returncode)
    print(process.pid)

if __name__ == '__main__':
    run_artifactory(r'D:\artifactory\artifactory-oss-5.5.1\bin\artifactory.bat')

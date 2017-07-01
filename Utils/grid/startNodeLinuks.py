from ChromedriverFolder.driverPath import getDriverPath

seleniumServerPath = "/home/thomas/selenium"
driverPath =getDriverPath()+ '/chromedriver.exe'
node = "java -jar -Dwebdriver.chrome.driver="+driverPath+" selenium-server-standalone-3.3.1.jar -host localhost -role webdriver -hub http://192.168.0.102:4444/grid/register  -port 5555 -browser browserName=chrome,maxInstances=5,platform=LINUX"


nodeExecution = "cd "+ seleniumServerPath+ " &&"+node

print(nodeExecution)


def run(comand):
    import os
    os.system(comand)

run(nodeExecution)

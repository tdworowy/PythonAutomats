from chromedriverFolder.driverPath import getDriverPath

seleniumServerPath = "D:\selenium"
driverPath =getDriverPath()+ '/chromedriver.exe'
node = "java -jar -Dwebdriver.chrome.driver="+driverPath+"selenium-server-standalone-3.3.1.jar -host localhost -role webdriver -hub http://192.168.0.102:4444/grid/register  -port 5555 -browser browserName=chrome,maxInstances=5,platform=WINDOWS"


nodeExecution = "cd "+ seleniumServerPath+ "&& D: &&"+node

print(nodeExecution)


def run(comand):
    import os
    os.system(comand)

run(nodeExecution)

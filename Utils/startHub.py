import _thread

from chromedriverFolder.driverPath import getDriverPath

seleniumServerPath = "D:\selenium"
driverPath =getDriverPath()+ '\\chromedriver.exe'
hub = "java -jar selenium-server-standalone-2.49.1.jar -host http://localhost -port 4444 -role hub"
node ="java -jar selenium-server-standalone-2.49.1.jar -host localhost -role webdriver -hub http://localhost:4444/grid/register  -port 5555 -browser browserName=chrome,maxInstances=5,platform=WINDOWS  -Dwebdriver.chrome.driver="+driverPath

hubExecution = "cd "+ seleniumServerPath+ "&& D: &&"+hub
nodeExecution = "cd "+ seleniumServerPath+ "&& D: &&"+node
print(hubExecution)
print(nodeExecution)

def run(comand):
    import os
    os.system(comand)

_thread.start_new_thread(run(hubExecution), ())
_thread.start_new_thread(run(nodeExecution), ()) # don't start second thread
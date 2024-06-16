from Chrome_Driver_Folder.driver_path import get_driver_path

selenium_server_path = "D:\selenium"
driverPath = get_driver_path() + "\\chromedriver.exe"
hub = "java -jar selenium-server-standalone-2.49.1.jar -host http://localhost -port 4444 -role hub"
node = (
    "java -jar selenium-server-standalone-2.49.1.jar -host localhost -role webdriver -hub "
    "http://localhost:4444/grid/register  -port 5555 -browser browserName=chrome,maxInstances=5,platform=WINDOWS  "
    "-Dwebdriver.chrome.driver=" + driverPath
)

hub_execution = "cd " + selenium_server_path + "&& D: &&" + hub
node_execution = "cd " + selenium_server_path + "&& D: &&" + node
print(hub_execution)
print(node_execution)


def run(command):
    import os

    os.system(command)

from Chrome_Driver_Folder.driver_path import get_driver_path

selenium_server_path = "/home/thomas/selenium"
driver_path = get_driver_path() + '/chromedriver.exe'
hub = "java -jar selenium-server-standalone-3.3.1.jar -host http://localhost -port 4444 -role hub"

hub_execution = "cd " + selenium_server_path + " &&" + hub

print(hub_execution)


def run(command):
    import os
    os.system(command)


run(hub_execution)

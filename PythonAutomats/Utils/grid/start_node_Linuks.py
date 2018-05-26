from Chrome_Driver_Folder.driver_path import get_driver_path

selenium_server_path = "/home/thomas/selenium"
driver_path = get_driver_path() + '/chromedriver.exe'
node = "java -jar -Dwebdriver.chrome.driver=" + driver_path + "selenium-server-standalone-3.3.1.jar -host localhost -role " \
                                                              "webdriver -hub http://192.168.0.102:4444/grid/register  " \
                                                              "-port 5555 -browser browserName=chrome,maxInstances=5," \
                                                              "platform=LINUX "

node_execution = "cd " + selenium_server_path + " &&" + node

print(node_execution)


def run(command):
    import os
    os.system(command)

if __name__ == "__main__":
    run(node_execution)

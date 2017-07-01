from ChromedriverFolder.driverPath import getDriverPath

seleniumServerPath = "/home/thomas/selenium"
driverPath =getDriverPath()+ '/chromedriver.exe'
hub = "java -jar selenium-server-standalone-3.3.1.jar -host http://localhost -port 4444 -role hub"


hubExecution = "cd "+ seleniumServerPath+ " &&"+hub

print(hubExecution)


def run(comand):
    import os
    os.system(comand)

run(hubExecution)

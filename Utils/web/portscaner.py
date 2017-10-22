import _thread
import os
import sys
import time;
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname

from Utils.decorators import log_exception


class PortScanner:
    def __init__(self, host):
        self.host = host
        self.path = os.path.dirname(os.path.abspath(__file__))

    def scan_host(self, port, debug=False):
        code = self.soc.connect_ex((self.host, port))
        if debug: print("Port checked: %s response %s" % (port, code))
        if code == 0: print("Port %s is open" % port)
        return port, code

    @log_exception()
    def scan_ports(self, min, max):
        self.soc = socket(AF_INET, SOCK_STREAM)
        with open("%s\\results\Ports_%s.txt" % (self.path, max), "w") as f1:
            host_ip = gethostbyname(self.host)
            print("Host: %s IP: %s" % (self.host, host_ip))
            print("Scan in progress...")
            results = map(self.scan_host, [port for port in range(min, max + 1)])
            self.soc.close()
            opened_ports = [x[0] for x in list(results) if x[1] == 0]
            print("Scan Done...")
            f1.write(str(opened_ports).replace("[", "").replace("]", ""))


@log_exception()
def distribution(ps, number, parts):
    rest = number % parts
    min = 0
    max = number / parts
    for i in range(1, parts):
        if i == parts: max = max + rest
        max = i * max
        _thread.start_new_thread(ps.scan_ports, (min, max))
        min = max


def main(host="127.0.0.1", min=0, max=65534):
    ps = PortScanner(host)
    distribution(ps, min, max)
    time.sleep(120)
    while _thread._count() > 0:
        time.sleep(120)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        host_ = sys.argv[1]
        min = sys.argv[2]
        max = sys.argv[3]
        main(host=host_, min=min, max=max)
    else:
        main()

import _thread
import os
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, SOL_SOCKET, SO_REUSEADDR

from Utils.decorators import log_exception
from Utils.utils import log


class PortScanner:
    def __init__(self, host):
        self.host = host
        self.path = os.path.dirname(os.path.abspath(__file__))

    def scan_host(self, port, debug=False):
        soc = socket(AF_INET, SOCK_STREAM)
        soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        soc.settimeout(0.3)
        code = soc.connect_ex((self.host, port))
        soc.close()
        if debug: print("Port checked: %s response %s" % (port, code))
        if code == 0: log("Port %s is open" % port)
        return port, code

    @log_exception()
    def scan_ports(self, min, max):
        log("Ports range: %s to %s" % (min, max))
        with open("%s\\results\Ports_%s.txt" % (self.path, max), "w") as f1:
            host_ip = gethostbyname(self.host)
            log("Host: %s IP: %s" % (self.host, host_ip))
            log("Scan in progress...")
            results = map(self.scan_host, [port for port in range(min, max + 1)])
            opened_ports = [x[0] for x in list(results) if x[1] == 0]
            log("Scan Done...")
            f1.write(str(opened_ports).replace("[", "").replace("]", ""))


def distribution(ps, min_, max_, parts):
    rest = max_ % parts
    min = min_
    inc = (max_-min_) // parts
    max =min_+ inc
    for i in range(1, parts+1):
        if i == parts: max = max + rest
        _thread.start_new_thread(ps.scan_ports, (min, max))
        max = max + inc
        min = min + inc


@log_exception()
def main(host="127.0.0.1", min=0, max=65534, parts=4):
    ps = PortScanner(host)
    distribution(ps, min, max, parts)
    time.sleep(120)
    while _thread._count() > 0:
        time.sleep(120)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        host_ = sys.argv[1]
        min = sys.argv[2]
        max = sys.argv[3]
        main(host=host_, min=int(min), max=int(max))
    else:
        main()

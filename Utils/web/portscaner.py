import sys
from socket import *

from Utils.decorators import log_exception
from Utils.utils import log


class PortScanner:
    def __init__(self, host):
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.host = host

    def scan_host(self, port, debug=False):
        code = self.soc.connect_ex((self.host, port))
        self.soc.close()
        if debug: print("Port checked: %s response %s" % (port, code))
        return port, code

    @log_exception()
    def scan_ports(self, min, max):
        host_ip = gethostbyname(self.host)
        print("Host: %s IP: %s" % (self.host, host_ip))
        print("Scan in progress...")
        results = map(self.scan_host, [port for port in range(min, max + 1)])
        print("Scan Done...")
        return [x[0] for x in results if x[1] == 0]


if __name__ == '__main__':
    ps = PortScanner(sys.argv[1])
    open_ports = ps.scan_ports(0, 65535)
    log(open_ports)

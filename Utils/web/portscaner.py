import sys
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname

from Utils.decorators import log_exception
from Utils.utils import log


class PortScanner:
    def __init__(self, host):
        self.host = host

    def scan_host(self, port, debug=False):
        soc = socket(AF_INET, SOCK_STREAM)
        code = soc.connect_ex((self.host, port))
        soc.close()
        if debug: print("Port checked: %s response %s" % (port, code))
        return port, code

    @log_exception()
    def scan_ports(self, min, max):
        host_ip = gethostbyname(self.host)
        print("Host: %s IP: %s" % (self.host, host_ip))
        print("Scan in progress...")
        results = map(self.scan_host, [port for port in range(min, max + 1)])
        print("Scan Done...")
        return [x[0] for x in list(results) if x[1] == 0]


if __name__ == '__main__':
    host_ = sys.argv[1]
    ps = PortScanner(host_)
    open_ports = ps.scan_ports(0, 65534)
    log(str(open_ports))
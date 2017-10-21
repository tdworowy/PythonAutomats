import _thread
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname

from Utils.decorators import log_exception


class PortScanner:
    def __init__(self, host):
        self.host = host

    def scan_host(self, port, debug=False):
        soc = socket(AF_INET, SOCK_STREAM)
        code = soc.connect_ex((self.host, port))
        soc.close()
        if debug: print("Port checked: %s response %s" % (port, code))
        if code == 0: print("Port %s is open" % port)
        return port, code

    @log_exception()
    def scan_ports(self, min, max):
        path = os.path.dirname(__file__)
        with open("%s\\results\Ports_%s.txt" %(path,max),"w") as f1:
            host_ip = gethostbyname(self.host)
            print("Host: %s IP: %s" % (self.host, host_ip))
            print("Scan in progress...")
            results = map(self.scan_host, [port for port in range(min, max + 1)])
            opened_ports = [x[0] for x in list(results) if x[1] == 0]
            print("Scan Done...")
            f1.write(opened_ports)



if __name__ == '__main__':
    host_ = sys.argv[1]
    ps = PortScanner(host_)
    _thread.start_new_thread(ps.scan_ports, (0, 16384))
    _thread.start_new_thread(ps.scan_ports, (16384, 49150))
    _thread.start_new_thread(ps.scan_ports, (49150, 55534))
    _thread.start_new_thread(ps.scan_ports, (55534, 65534))
    # open_ports = ps.scan_ports(0, 65534)


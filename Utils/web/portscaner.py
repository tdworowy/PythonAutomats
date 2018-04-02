import os
import sys
from multiprocessing import Process
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, SOL_SOCKET, SO_REUSEADDR
from threading import Thread

from Utils.decorators import log_exception
from Utils.file_utils import combine_all_files


class PortScanner:
    def __init__(self, host):
        self.host = host
        self.path = "%s\\results" % os.path.dirname(os.path.abspath(__file__))

    def scan_host(self, port, debug=False):
        soc = socket(AF_INET, SOCK_STREAM)
        soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        soc.settimeout(0.1)
        code = soc.connect_ex((self.host, port))
        soc.close()
        if debug: print("Port checked: %s response %s" % (port, code))
        return port, code

    def scan_ports(self, min, max):
        print("Ports range: %s to %s" % (min, max))
        file_name = "%s\Ports_%s_%s_%s.txt" % (self.path, self.host, min, max)
        with open(file_name, "w") as f1:
            host_ip = gethostbyname(self.host)
            print("Host: %s IP: %s" % (self.host, host_ip))
            print("Scan in progress...")
            results = map(self.scan_host, [port for port in range(min, max + 1)])
            opened_ports = [x[0] for x in list(results) if x[1] == 0]
            print("Scan Done...")
            for port_number in opened_ports:
                f1.write(str(port_number)+"\n")

        if os.stat(file_name).st_size == 0:
                os.remove(file_name)


def distribution_threads(ps, min_, max_, parts):
    rest = max_ % parts
    min = min_
    inc = (max_ - min_) // parts
    max = min_ + inc
    threads = []
    for i in range(1, parts + 1):
        if i == parts: max = max + rest
        threads.append(Thread(target=ps.scan_ports, args=(min, max)))
        max = max + inc
        min = min + inc

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def distribution_processes(parts, target, ps, min_, max_, ):
    rest = max_ % parts
    min = min_
    inc = (max_ - min_) // parts
    max = min_ + inc
    processes = []
    for i in range(1, parts + 1):
        if i == parts: max = max + rest
        process = Process(target=target, args=(ps, min, max, 10))
        max = max + inc
        min = min + inc
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


@log_exception()
def main(host="127.0.0.1", min=0, max=100, parts=10):
    ps = PortScanner(host)
    distribution_processes(parts=parts, target=distribution_threads, min_=min, max_=max, ps=ps)
    combine_all_files(ps.path, "%s/ports.txt" % ps.path)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host_ = sys.argv[1]
        min = sys.argv[2]
        max = sys.argv[3]
        main(host=host_, min=int(min), max=int(max))
    else:
        main()

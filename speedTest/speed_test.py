import time

import speedtest
from Utils.decorators import log_exeption
from Utils.utils import log


@log_exeption()
def test_speed(log_=True):
    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    if log_: log(res)
    print(res)
    return res


if __name__ == "__main__":
    with open("D:\Google_drive\statistics\speed.csv", 'a') as f:
        time_stump = time.strftime('%Y-%m-%d %H:%M:%S')
        res = str(test_speed())
        print(res)
        f.write("%s, %s\n" % (time_stump, res))

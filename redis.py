import sys

class Center(object):
    def __init__(self, cid):
        self.cid = cid
        self.cluster_list = []
        self.host = []



class Cluster(object):
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.redis_list = []
        self.corvus_list = []

class Corvus(object):
    def __init__(self, corvus_threads, port, ip):
        self.corvus_threads = corvus_threads
        self.port = port
        self.ip = ip


class Redis(object):
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip


def data():
    wg = Center('1')
    xg = Center('2')
    aa1 = Cluster('test1')
    aa2 = Cluster('test2')

    c1 = Corvus(10, 10, '192.168.0.1')
    c2 = Corvus(10, 10, '192.168.0.2')

    a1 = Redis('1000', '127.0.0.1')
    a2 = Redis('1001', '127.0.0.2')

    aa1.redis_list.append(a1)
    aa1.corvus_list.append(c1)

    wg.cluster_list.append(aa1)
    xg.cluster_list.append(aa2)
if __name__ == '__main__':
    data()

import requests
import csv

class ProxyPool:
    def __init__(self, path):
        self.counter = 0
        self.proxyList = []
        self.test_url = 'http://www.baidu.com/'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        
        f = open(path, 'r')
        reader = csv.reader(f)
        self.proxyList = list(reader)[0]
        print('proxyPool in the type of list: \n', self.proxyList)

    def get_proxy_pool(self):
        for proxy in self.proxyList:
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        proxies = {
            'http' : 'http://{}'.format(proxy),
            'https' : 'https://{}'.format(proxy)
        }
        self.counter += 1
        try:
            res = requests.get(url = self.test_url, proxies = proxies,\
                headers = self.headers, timeout = 2)
            if res.status_code == 200:
                print("NO.", self.counter,' ', proxy, '\033[31mwork\033[0m')
                with open('../files/workingProxies.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(proxy)
        except Exception as e:
            print("NO.", self.counter,' ', proxy, 'not work')

if __name__ == '__main__':
    path = './files/proxy_pool.csv'
    pp = ProxyPool(path)
    pp.get_proxy_pool()
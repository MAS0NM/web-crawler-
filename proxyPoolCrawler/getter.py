from proxyPoolCrawler.proxyCrawler import Crawler
import csv

class Getter():
    def __init__(self):
        self.crawler = Crawler()

    def run(self):
        print('获取器开始执行')
        for callback_label in range(self.crawler.__CrawlFuncCount__):
            callback = self.crawler.__CrawlFunc__[callback_label]
            # 获取代理
            all_ip = self.crawler.get_proxies(callback)
            print(all_ip)
            with open('../files/proxy_pool.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(all_ip)

if __name__ == '__main__':
    get = Getter()
    get.run()
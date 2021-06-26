import requests
import re
from urllib.parse import urlencode
import time

def get_html(url, page):
    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    }
    params = {
        # 'callBack': 'fetchJSON_comment98',
        'productID': 100019867468,
        'score': 0,
        'sortType': 6,
        'page': page,
        'pageSize': 10,
        'isShadowSku': 0,
        'rid': 0,
        'fold': 1
    }
    res = ""
    url = url + urlencode(params)
    try:
        req = requests.get(url = url, params = params, headers = header)
        time.sleep(0.5)
        print(req.text)

    except Exception as e:
        print('erro', e)

if __name__ == '__main__':
    url = 'https://club.jd.com/comment/productPageComments.action?'
    for i in range(10):
        get_html(url, i)
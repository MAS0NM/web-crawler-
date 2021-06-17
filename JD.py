import json
from urllib import request
import time

header_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
}


def get_http(load_url, header=None):
    res = ""
    try:
        req = request.Request(url=load_url, headers=header)  # 创建请求对象
        coonect = request.urlopen(req)  # 打开该请求
        byte_res = coonect.read()  # 读取所有数据，很暴力
        try:
            res = byte_res.decode(encoding='utf-8')
        except:
            try:
                res = byte_res.decode(encoding='gbk')
            except:
                res = ""
    except Exception as e:
        print(e)
    return res


pid = "100019867468"  # 页面上的产品id
fout = open("./" + pid + ".csv", "w", encoding='utf-8')  # 输出文件
fout.write("uid,nickname,time,star,comment\n")  # 写csv头 微软的表格打开可能是乱码，解决方法是另存为带BOM头的编码
for score in ["3", "2", "1"]:  # 爬取好中差评3好评，2中评，1差评，0默认评论
    # 这个链接和从网页上的链接不太一样，少了几个参数，加载出来的是json数据。
    url0 = "https://club.jd.com/comment/productPageComments.action?productId=" + pid + "&score=" + score + "&sortType=6&page="
    # 调整页码，这里只爬取前10页，用于演示，可以写成while True的
    for page in range(10):
        url = url0 + str(page) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
        res = get_http(url, header_dict)
        time.sleep(0.1)
        if res == None or len(res) <= 30:
            print("加载错误", url)
            continue
        jobj = json.loads(res, strict = False)  # 解析json

        comments = jobj["comments"]
        if len(comments) == 0:
            break
        # 提取每一页的评论数据并保存
        for comment in comments:
            userImage = comment["userImage"]
            nickname = comment["nickname"]
            uid = str(hash(userImage + nickname))[0:18]
            content = comment["content"]
            creationTime = comment["creationTime"]
            score1 = str(comment["score"])
            fout.write(uid + "," + nickname + "," + creationTime + "," + score1 + "," + content + "\n")
fout.close()
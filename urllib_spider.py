import json
from urllib import request
import time
import random

header_dict = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
}


def get_http(load_url, header=None):
    res = ""
    try:
        req = request.Request(url=load_url, headers=header)  # 创建请求对象
        connect = request.urlopen(req)  # 打开该请求
        byte_res = connect.read()  # 读取所有数据
        try:
            res = byte_res.decode(encoding='utf-8')
        except:
            try:
                res = byte_res.decode(encoding='gbk')
            except:
                res = ""
    except Exception as e:
        print(e)
    print("res", res)
    return res


def spider():
    counter = 0
    # pid = "100019867468"  # 页面上的产品id
    pid = "30191573825"
    fout = open("./files/" + pid + ".csv", "w", encoding='utf-8')  # 输出文件
    fout.write("uid,nickname,time,star,comment\n")
    for score in ["3", "2", "1"]:  # 3好评，2中评，1差评，0默认评论
        print("crawling comments that score ", score)
        url0 = "https://club.jd.com/comment/productPageComments.action?productId="\
               + pid + "&score=" + score + "&sortType=6&page="
        for page in range(100):
            print("page NO.", page)
            url = url0 + str(page) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
            res = get_http(url, header_dict)
            sleepTime = random.uniform(0.5, 2)
            time.sleep(sleepTime)
            if res == None or len(res) <= 30:
                print("加载错误", url)
                continue
            jobj = json.loads(res, strict = False)  # 解析json

            comments = jobj["comments"]
            #comments：[{},{},{},{}]
            if len(comments) == 0:
                break
            # 提取每一页的评论数据并保存
            for comment in comments:
                counter += 1
                print("comments NO.", counter)
                if counter >= 1000:
                    return
                userImage = comment["userImage"]
                nickname = comment["nickname"]
                uid = str(hash(userImage + nickname))[0:18]
                content = comment["content"]
                creationTime = comment["creationTime"]
                score1 = str(comment["score"])
                fout.write(
                             uid + ","
                           + nickname + ","
                           + creationTime + ","
                           + score1 + ","
                           + content.replace('\n', '')
                           + "\n"
                )
    fout.close()


if __name__=='__main__':
    spider()
import requests
import json
url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的英文单词")
data = {
    "kw" : s
}

resp = requests.post(url, data = data)
# result = json.loads(resp.text)
print(resp.json())
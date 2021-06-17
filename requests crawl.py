import requests
query = input("输入一个关键字")
url = f'https://cn.bing.com/search?q={query}'
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37"
}

resp = requests.get(url, headers  = headers)
print(resp.text)
import requests


url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": "11",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}


headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37"
}

resp = requests.get(url = url, params = param, headers = headers)

print(resp.json())
resp.close()
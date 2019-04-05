import requests as r
import urllib
import sys
import json


host = 'https://music-jp-api.line-apps.com/v3/'

lct = ''
#x-lctを入力

did = ''
#x-lm-didを入力

sesid = ''
#生成方法がわからない。アプリを開く度に生成されてるっぽい？

header = {'x-lct': lct, 'Accept': 'application/json', 'x-lm-did': did, 'timeout': 30, 'User-Agent': 'LineMusic/3.9.2  (iPhone; U; iOS 12.1.4; ja-JP;)', 'Accept-Language': 'ja-JP;q=1', 'Accept-Encoding': 'br, gzip, deflate', 'Cookie': ''}

query = input("please input keywords: ")
enc = urllib.parse.quote(query)
points = host + 'search/title?keyword=' + enc + '&sessionId=' + sesid
p = r.get(points, headers=header)
if p.status_code == 200:
    print(str(p))
    data = p.json()
    print(json.dumps(data["result"]["albumList"], indent=4))
else:
    p.raise_for_status()
    print(p.text)

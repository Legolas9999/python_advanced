import re
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
res = requests.get("https://missav.com/ja/sone-239-chinese-subtitle", headers=header)

# html str
res = res.content.decode("utf-8")

pic_url = re.finditer('img src="(.*?)"',res)
url_list = []
if pic_url:
    for i in pic_url:
        url_list.append(i.group(1))


num = 20
for i in url_list:
    res = requests.get(i)
    res = res.content
    with open(f'pic/{num}.jpg','wb') as f:
        f.write(res)

    num += 1
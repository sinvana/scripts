import requests

url = "http://demo.edu.cn/eams/login.action"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://demo.edu.cn/eams/login.action",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
    }

kv = {
            "username":"demo",
            "password":"demo",
            "encodedPassword":"",
    #        "captcha":"ceems",
            "message":""
            }

session = requests.Session()
r = session.post(url,kv,headers=headers)
#print(r.headers)
#print(dir(r))
url_0 = "http://demo.edu.cn/eams/studentDetail.action"
m = session.get(url_0)
print(m.text)
with open("01.html","w",encoding="utf-8")as f:
    f.write(m.text)

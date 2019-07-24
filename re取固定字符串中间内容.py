import re

string = "xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"
result = re.findall(".*entry(.*)for.*",string)

for x in result:
    print(x)

s1 = "sdasda\
dasdad\
sadasdad\
dasdad"
s2 = '''sdasda
daszxcdad
sadasdad
dasxxdad'''
print(s1)
print(s2)
print(len(s1))
print(len(s2))
print()
r = re.findall(".*da(.*)da.*",s2)
print(r)

sg = "4.18微信站点[192.168.120.33_16361]_漏洞详情_756.txt"
r1 = re.findall("\[(.*)\]",sg)
r2 = re.findall("\[.*\]",sg)
print(r1)
print(r2)

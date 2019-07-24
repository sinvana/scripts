import os

#print(os.listdir())
lt = os.listdir()
print(lt)
for i in lt:
    if "漏洞详情"and"txt" not in i:
        lt.remove(i)
try:
    lt.remove(os.path.basename(os.path.realpath(__file__)))
except:
    pass
print(lt)
print(os.path.realpath(__file__))  #获取当前文件路径
print(os.path.dirname(os.path.realpath(__file__)))  #从当前文件路径中获取目录
print(os.path.basename(os.path.realpath(__file__)))  #获取文件名

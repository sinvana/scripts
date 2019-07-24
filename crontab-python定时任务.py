import os
from datetime import datetime
import time


s = os.path.realpath(__file__)
a = s[:-10]
print(a)
#print(os.system("cd"))
#print(os.system("python "+a+"hello_world.py"))

lt = ["41","42","43","44","55","46","47","48","49","50","00","01","02","11","12","13"]
while 1:
    t = datetime.now()
    minute = str(t).split(":")[-2]
    print(minute)
    if minute in lt:
        print(os.system("cd"))
        print(os.getpid())
        time.sleep(60)
        

with open("demo_in.txt") as f:
    s = f.readlines()

#print(len(s))
lt = []
for i in s:
    if "http" in i:
        ss = i.split(" ")
        for j in ss:
            if "http" in j:
                #print(j.strip())
                lt.append(j.strip())
lt_x = []
for i in lt:
    if i not in lt_x:
        lt_x.append(i)
#print(len(lt_x))
with open("demo_out.txt","w+")as ff:
    for i in lt_x:
        ff.write(i+"\n")


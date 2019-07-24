with open ("./url_未去重.txt") as f:
    lt_0 = f.readlines()
    lt_1 = [i.strip() for i in lt_0]

#print(lt_1)
#print(len(lt_1))

lt = []
for i in lt_1:
    if i not in lt:
        lt.append(i)

with open("./url_已去重.txt","a") as ff:
    num = 0
    for i in lt:
        ff.write(i+"\n")
        num+=1
        print(num)

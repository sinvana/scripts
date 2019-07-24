import os
a = os.listdir()
a.remove("启明天镜web提取漏洞信息-工具版(扫描url+漏洞url+漏洞名称+漏洞级数).py")
a.remove("lt_sin.txt")
a.remove("lt_sin.xlsx")
print(a)
for m in a:
    
    with open(m,encoding="utf-8")as f:
        s = f.readlines()
    lt_sin =[]
    lt_x = []
    lt_y = []
    lt_z = []
    lt_1 = []

    # 扫描目标
    lt_11 = []
    for i in range(len(s)):
        if "扫描目标" in s[i]:
            url = s[i+1].strip()
            print(url)

    # 漏洞链接
    lt = []
    for i in range(len(s)):
        if "问题链接" in s[i]:
            lt.append(i)
    print(lt)
    for i in lt:
        print(s[i+1].strip())
        lt_x.append(s[i+1].strip())

    # 漏洞名称
    lt_a = []
    for i in range(len(s)):
        if "漏洞名称" in s[i]:
            lt_a.append(i)
    print(lt_a)
    del(lt_a[0])
    for i in lt_a:
        print(s[i+1].strip().split("\t")[-1])
        lt_y.append(s[i+1].strip().split("\t")[-1])


    # 危险级别    
    lt_b = []
    for i in range(len(s)):
        if "危险级别" in s[i]:
            lt_b.append(i)
    print(lt_b)
    del(lt_b[0])
    for i in lt_b:
        print(s[i+1].strip().split("\t")[-1])
        lt_z.append(s[i+1].strip().split("\t")[-1])

    for j in range(len(lt_x)):
        print(lt_x[j]+"\t"+lt_y[j]+"\t"+lt_z[j])
        lt_sin.append("\t"+lt_x[j]+"\t"+lt_y[j]+"\t"+lt_z[j])
    print(lt_sin)

    with open("lt_sin.txt","a")as ff:
        #ff.write(m+"\n")
        #ff.write(url+"\n")
        for i in lt_sin:
            ff.write(url+i+"\n")




with open("直销低1.txt",encoding="utf-8")as f:
    s = f.readlines()

lt_x = []
lt_y = []
lt_z = []

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
    print(s[i].strip().split("\t")[-1])
    lt_y.append(s[i].strip().split("\t")[-1])


# 危险级别    
lt_b = []
for i in range(len(s)):
    if "危险级别" in s[i]:
        lt_b.append(i)
print(lt_b)
del(lt_b[0])
for i in lt_b:
    print(s[i].strip().split("\t")[-1])
    lt_z.append(s[i].strip().split("\t")[-1])

for j in range(len(lt_x)):
    print(lt_x[j]+"\t"+lt_y[j]+"\t"+lt_z[j])


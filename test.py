a=[]
for i in range(1,30):
    s=0
    i='STD'+str(i)
    for j in i:
        s += ord(j)
    v=s%100
    a.append(v)


print(len(a))
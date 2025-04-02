l=[1,3,4,1,7,4,4,9,3,5,9,2,1,3,6,3,9]
a=[]
b=[]
for i in range(len(l)):
    if l[i] not in a:
        a.append(l[i])
for i in range (len(a)):
    c=0
    for j in range(len(l)):
        if a[i]==l[j]:
            c=c+1
    b.append(c)
d={k: v for k, v in zip(a,b)}
print(d)



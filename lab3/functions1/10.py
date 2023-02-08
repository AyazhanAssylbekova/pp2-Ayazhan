def uni(*l):
    for i in range(len(l)):
         d[l[i]]=l.count(l[i])

    s=list()
    s.extend(d)
    print(s)
l=list()
while True:
    a=int(input())
    if a==0:
        break
    else:
        l.append(a)
d=dict()

uni(*l)
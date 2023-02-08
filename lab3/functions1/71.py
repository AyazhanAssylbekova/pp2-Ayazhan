def has33(l):
    ok=False
    for i in range(len(l)-1):
        if l[i]==l[i+1]==3:
            ok=True
    print(ok)
l=list()
while True:
    a=int(input())
    if a==0:
        break
    else:
        l.append(a)

has33(l)
        
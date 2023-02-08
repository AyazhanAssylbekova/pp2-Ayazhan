def has33(l):
    ok=False
    for i in range(len(l)-1):
        if l[i]==l[i+1]==3:
            ok=True
    print(ok)
l=[1,3,3,5,4]
has33(l)
        
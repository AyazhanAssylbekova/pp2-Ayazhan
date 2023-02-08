def myfunc(l):
    x=l.index(0)
    l.remove(0)
    y=l.index(0)+1
    z=l.index(7)+1

    if x<y<z:
        print("True")
    else:
        print("No")

l=list((0,2,0,5,7))
myfunc(l)

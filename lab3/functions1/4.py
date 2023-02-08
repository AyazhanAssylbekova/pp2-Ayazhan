def myfunc(l):
    k=[]
    for x in l:
        if x==1:
            continue
        else:
            ok=False
            i=2
            while i<x//2:
                if x%i==0:
                    ok=True
                i+=1
        
            if ok==False:
                k.append(x)
    print(k)

s=input()
l=[]
j=s.split(" ")
for x in j:
    l.append(int(x))

myfunc(l)



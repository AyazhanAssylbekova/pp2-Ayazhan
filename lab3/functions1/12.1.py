def hist(l):
    i=0
    while i!=len(l):
        j=0
        while j!=l[i]:
            print("*",end="")
            j+=1
        print(" ")
        i+=1


l=list()
while True:
    a=int(input())
    if a==0:
        break
    else:
        l.append(a)
hist(l)


   


def rever(s):
    x=s.split(" ")
    i=len(x)
    while i>0:
        print(x[i-1],end=" ")
        i-=1
       
s=input()
rever(s)

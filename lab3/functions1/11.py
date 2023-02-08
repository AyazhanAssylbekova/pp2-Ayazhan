def pol(a):
    b=str()
    for i in range(len(a)):
        b+=a[len(a)-i-1]
    if a==b:
        print("YES")
    else:
        print("NO")

a=input()
pol(a)

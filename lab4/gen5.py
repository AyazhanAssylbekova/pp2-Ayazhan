n=int(input())
def  simple():
    for i in range(n,-1,-1):
        yield i

for i in simple():
    print(i,end=" ")
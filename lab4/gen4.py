a=int(input())
b=int(input())
def square():
    for i in range(a,b+1):
        yield i*i

for i in square():
    print(i,end=" ")
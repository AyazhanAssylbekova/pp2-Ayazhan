n=int(input())
def simple():
    for i in range(n+1):
        if i%2==0:
            yield i

for i in simple():
    print(i)
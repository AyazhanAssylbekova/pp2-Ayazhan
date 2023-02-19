n=int(input())

def simple():
    for i in range(n+1):
        yield i**2

for i in simple():
    if i>n:
        break
    else:
        print(i)
def prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def filtr(l):
     result = list(filter(lambda x: prime(x) , l))
     print(result)

n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)

filtr(l)

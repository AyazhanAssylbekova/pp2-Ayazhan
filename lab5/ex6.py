import re
txx=input("Enteer ur string: ")
x=re.sub("[' ',.]",":",txx)
print (x)
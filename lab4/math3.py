import math
from math import pi
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
c=(n*(a**2))/(4*math.tan((pi)/n))
print(int(c))

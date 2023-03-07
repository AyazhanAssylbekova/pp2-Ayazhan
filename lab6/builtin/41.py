import math
import datetime
import time
a=int(input("Enter the square: "))
c=int(input())
# b=int(input("Enter the msec: "))
e=math.sqrt(a)
time.sleep(c/1000)
print(f"Square root of {a} after {c} miliseconds is {e}")
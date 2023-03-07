import math
import datetime
a=int(input("Enter the square: "))
c=datetime.datetime.now()
# b=int(input("Enter the msec: "))
e=math.sqrt(a)
b=datetime.datetime.now()
print("Square root of",a,"after",(b-c).seconds,"miliseconds is",e)
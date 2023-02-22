import datetime
import math
d1=datetime.datetime(2022,12,30,12,55,55)
d2=datetime.datetime.now()
s=abs(d1-d2).seconds
print(s)
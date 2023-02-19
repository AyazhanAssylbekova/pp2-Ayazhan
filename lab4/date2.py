import datetime
d1=datetime.datetime.now()
d2=datetime.date(d1.year,d1.month,d1.day-1)
d3=datetime.date(d1.year,d1.month,d1.day+1)
d4=datetime.date(d1.year,d1.month,d1.day)

print("Yesterday: ",d2)
print("Tomorrow: ",d3)
print("Today: ",d4)
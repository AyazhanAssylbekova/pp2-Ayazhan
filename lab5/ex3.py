import re
a=input("Enter ur string: ")
b=re.findall("[a-z]{0,}_[a-z]{0,}",a)
print(b)
# all characters don`t forget`
import re
a=input("enter ur string: ")
b=re.findall(".*a.*b", a)
print(b)
import re
txx=input("Enter ur string: ")
d=re.findall("ab{0,}", txx)
print(d)


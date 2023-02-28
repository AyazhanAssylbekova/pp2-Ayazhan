import re
txx=input("Enter ur string: ")
d=re.findall("ab{2,3}", txx)
print(d)


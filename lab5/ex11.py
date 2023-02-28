import re
# txx=input("Enter ur string: ")
txx="dvgaabb dsvsab abbb ab kbjbjw jdbv abb hab "
d=re.findall("' '.*ab{0,}. *' '", txx)
print(d)


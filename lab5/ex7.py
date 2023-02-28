import re
txx=input("Enter ur string: ")
# txx="hsv_hewHfvahs fasfd A_gyydffG  Gcc"
x=re.sub(r"_([a-z])",lambda a:a.group(1).upper(),txx)
print(x)
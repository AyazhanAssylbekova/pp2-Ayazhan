import re
txx=input("Enter ur string: ")
# txx="hsvFhewHfvahs fasfd A,gyydffG  Gcc"
x=re.sub(r"(\w)([A-Z])",r"\1 \2",txx)
print(x)
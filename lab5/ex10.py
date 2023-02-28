import re
txx=input("Enter ur string: ")
# txx="hsv_hewHfvahs fasfd A_gyydffG  Gcc"
x=re.sub(r"([A-Z])",r"_\1",txx).lower()
print(x)
import re
# a="Ahvvds Adfcg gvAvsvwGvdgcv"
a=input("Enter ur string: ")
b=re.findall("[A-Z][a-z]{0,}", a)
print(b)
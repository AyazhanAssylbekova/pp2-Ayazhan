import os
a=input("Enter ur path: ")
f=os.listdir(a)
# f=os.listdir("C:/Users/77785/Desktop/pp2-Ayazhan")
for i in f:
    print(i,end="\n")
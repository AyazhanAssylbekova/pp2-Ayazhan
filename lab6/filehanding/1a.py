import os 
# a=input("Enter ur path: ")
# f=os.listdir(a)
a=r"C:/Users/77785/Desktop/pp2-Ayazhan"
f=os.listdir(a)
for i in f:
    if os.path.isdir(i):
        print(i,end="\n")
import os 
a=input("Enter ur path: ")
f=os.listdir(a)
# f=os.listdir("C:/Users/77785/Desktop/pp2-Ayazhan")
for i in f:
    if i.endswith(".py" or ".txt"):
        continue
    else:
        print(i,end="\n")
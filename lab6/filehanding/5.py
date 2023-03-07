import os
files = os.listdir("C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding")
fill = os.listdir("C:/Users/77785/Desktop/pp2-Ayazhan/lab6/builtin")
print("filehanding: ")
for i in files:
    print(i,end="\n")
print("\n")
print("builtin: ")
for i in fill:
    print(i,end="\n")

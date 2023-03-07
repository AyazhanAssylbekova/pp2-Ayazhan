# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
a="C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row.txt"
try:
    f=open(a)
    print("Yes, exist")
    if f.readable():
        print("Yes, readable!")
    if f.writable():
        print("Yes, writable!")
    if f.writable()==False:
        print("Not writable")
    if f.readable()==False:
        print("Not readable")
except:
    print("Not exist!","Not readable","Not writable",sep="\n")




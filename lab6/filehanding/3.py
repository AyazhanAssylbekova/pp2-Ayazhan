""" Write a Python program to test whether
a given path exists or not. If the path exist
find the filename and directory portion of 
the given path."""
import os
a=input("Enter name of the file: ")
if os.path.exists(a):
    f=a.split('/')
    print(f[-1])
    print(f[-2])
else:
    print("Such a file does not exist")


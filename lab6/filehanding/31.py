""" Write a Python program to test whether
a given path exists or not. If the path exist
find the filename and directory portion of 
the given path."""
import os
a=r"C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/31.py "
if os.path.exists(r"C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/31.py "):
    print(os.path.dirname(a))
    
    # print(os.path.filename)
    # f=a.split('/')
    # print(f[-1])
    # print(f[-2])
else:
    print("Such a file does not exist")


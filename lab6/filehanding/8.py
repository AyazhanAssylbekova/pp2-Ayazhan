# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
# C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row1.txt
a=input("Enter ur file: ")
if os.path.exists(a):
    print("Exist!")
    os.remove(a)
    print("Removed!")
else:
    print('Such a file does not exist')


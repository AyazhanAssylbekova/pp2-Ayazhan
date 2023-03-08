# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os
# a="C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row2.txt"
a="C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row.txt"
print("exist!") if os.access(a,os.F_OK) else print("doesn`t exist!")
print("readable!") if os.access(a,os.R_OK) else print("doesn`t readable!")
print("writable") if os.access(a,os.W_OK) else print("doesn`t writable!")




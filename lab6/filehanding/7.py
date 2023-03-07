# Write a Python program to copy the contents of a file to another file
with open("C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row.txt",'r') as i:
    with open("C:/Users/77785/Desktop/pp2-Ayazhan/lab6/filehanding/row1.txt",'a') as j:
          for li in i:
                j.write(li)
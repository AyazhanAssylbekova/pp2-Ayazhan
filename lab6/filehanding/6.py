# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
for i in range(26):
    a=chr(65+i)
    with open(f"{a}.txt","a+") as fi:
        f"{a}.txt"

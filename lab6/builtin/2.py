s=input("enter ur string: ")
a=0
b=0
if s.isalpha()==True:
    for i in s:
        if i.isupper()==True:
            a+=1
        else:
            b+=1
    print(a,b)
else:
    print("False")
        
            



# a=0
# b=0
# for i in range(len(s)):
#     if s[i].isupper()==True:
#         a+=1
#     elif s[i].islower()==True:
#         b+=1

# print(a,b)

    
    
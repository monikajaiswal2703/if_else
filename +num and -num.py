# num1=int(input("enter the number:"))
# if num1>=1:
#     print("-", num1)
# elif num1<0:
#     print(-num1)
# else:
#     print("0,zero")


num1=(input("enter the number"))
l=len(num1)
if l!=3:
    print("enter three digit number")
else:
    print("middle digit is",(int(num1))%100//10)

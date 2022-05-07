# a={"one","two","three","four","five"}
# print(a)
# for i in a:
#     print(i)
# print()
# print(a)
# list1=[45,5,6,7,2]
# dict={}
# i=0
# while i<len (list1):
#     dict.update({list1[i]:a[i]})
#     i+=1
# print(dict)

# a=(1,2,4,5,6)
# b=(1,2,4,5,7)
# i=0
# c={}
# while i<len(a):
#     c.update({a[i]:b[i]})
#     i+=1
# print(c)


"q1 happy sad number"
# num=int(input("entrt the number"))
# a=num
# while a!=1 and a!=4:
#     sum=0
#     while a!=0:
#         rem=int(a%10)
#         sum=sum+rem*rem
#         a//=10
#     a=sum
# if sum==1:
#     print(num,"it is happy number")
# else:
#     print(num,"is a sad number")

"q2 1 to 100 number"
# for i in range(1,11):
#     while i<=100:
#         print(i,end=" ")
#         i+=10
#     print()

# i=0
# while i<=100:
#     print(i)
#     i+=1

"q3 factor number"
# n=int(input("enter the number"))
# b=[]
# for i in range(1,n+1):
#     if n%i==0:
#         b.append(i)
# print(b)

"q4 palindrom number"
# num=input("enter palindrom")
# a=num[::-1]
# print(a)
# i=0
# while i<1:
#     if num==a:
#         print(a,"is a palindrom ")
#     else:
#         print(a,"is a not palindrom")
#     i+=1
"string "
# x = input("enter the name:-")
# w = ""
# for i in x:
#     w = i + w
# if (x == w):
#     print("palindrom")
# else:
#     print("Not palindroim")

"q5 armstrong number"
# n=int(input("enter the number"))
# a = n
# sum=0
# while (n>0):
#     sum+=(n%10)*(n%10)*(n%10)
#     n//=10
# if a==sum:
#     print(a,"number is armstrong")
# else:
#     print(a,"not armstrong")
"q6 table"
# def table():
#     n=int(input("enter the number"))
#     b=[]
#     i=1
#     while i<=n:
#         j=1
#         c=[]
#         while j<=10:
#             r=i*j
#             c.append(r)
#             j+=1
#         b.append(c)
#         i+=1
#     print(b)
# table()

# n=int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(1,11):
#         r=i*j
#         print(r,end=" ")
#     print()

# print(24//1.5)

"q7 sum 2 list in function"
# def list1(a,b):
#     c=0
#     for i in a,b:
#         for j in i:
#             c+=j
#     return(c)
# print(list1([1,2,7],[1,2,4]))
"q8 add dictionary key value present or not"
# def dkv():
#     k=input("enter the key:-")
#     a={"mona":1,"sona":3,"rina":4,"hina":5}
#     for i,j in a.items():
#         if k==i:
#             return("ok")
#         else:
#             v=input("enter the value")
#             a.update({k:v})
#         return(a)
# print(dkv())

"q9 list"
# a=["mona","shivani","prachi","sweety","usha"]
# c=0
# for i in a:
#     c+=len(i)
#     b=i,c
#     c=0
#     print(b)

# a=["mona","shivani","prachi","sweety","usha"]
# n=input("enter the number")
# c=0
# b={}
# for i in a:
#     # a=input("enter the key:-")
#     c+=len(i)
#     b.update({i:c})
#     c=0
# print(b)


# n=int(input("enter the number"))
# l=[]
# for i in range(n):
#     d={}
#     name=input("entr the name")
#     surname=input("entrt the surname")
#     age=int(input("enter the age"))
#     d.update({"name":name,"surname":surname,"age":age})
#     l.append(d)
# print(l)

# d1=["first name","email","password"]
# d2=[name,surname,age]
# for i in range(len(d1)):
#     # d.update({d1[i]:d2[i]})
#     d=dict(zip(d1,d2))
# l.append(d)
# print(l)

# a=int(input("enter the number"))
# i=0
# while i<=a:
#     j=0
#     while j<=i:
#         print(j**2,end=" ")
#         j=j+1
#     print()
#     i=i+1

# date=input("enter the date")
# a=date[0:2]
# b=int(a)
# m= int(date[3:5])
# # y=int(date[6:10])
# if b>=1 and b<31:
#     b+=1
#     if b==31:
#         b=1
#         # m= int(date[3:5])
#         # n = int(m)
#         # y=int(date[6:10])
#         if (m>=1 and m<12):
#             m+=1
#             if m==12:
#               m=1
#               y=int(date[6:10])
#               if  y%100==0:
#                 y+=1
# print(b,"/",m,"/",y)

date=input("enter the date:")
a=date[0:2]
b=int(a)
if b>=1 or b<=31:
    b+=1
    m=date[3:5]
    n=int(m)
    if b>=31 and (n>=1 or n<=12):
        b=1
        n=+1
    y=int(date[6:10])
    if b==31 and n<=12 :
        y+=1
print(b,"/",n,"/",y)

# def evenodd():
#     a=int(input("enter no:"))
#     c=[]
#     for i in range(a):
#         b=int(input("enter the no:"))
#         c.append(b)
#     for j in c:
#         if j%2==0:
#             print("even")
#         else:
#             print("odd")
# evenodd()


# i=1
# k=1
# while i<=5:
#     b=1
#     while b<=5-i:
#         print( " ",end=" ")
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
#     k+=2
# i=5
# k=5
# while i>=0:
#     b=1
#     while b>=5-i:
#         print(" ",end=" ")   
#         b+=1
#     j=1
#     while j<=k:
#         print("*",end=" ")
#         j+=1
#     print()
#     k-=2
#     i-=1

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(i, "*", j, "=",i*j)
#         j+=1
#     print()
#     i+=1

# a=int(input("enter the number")) 
# i=1
# while i<=10:
#     j=1
#     while j<=a:
#         print(j*i, end = " ")
#         j+=1
#     print()
#     i+=1

num=input("enter the date")
a=num[0:2]
b=num[3:5]
c=num[6:]

if (int(c)%4==0) and a<="28" and b=="02":
    print(int(a)+1,"/",b,"/",c)
elif (int(c)%4==0) and a=="29":
    print("01/",int(b)+1,"/",c)
if (b=="01" or b=="03" or b=="05" or b=="07" or b=="09" or b=="10" or b=="12") and a<="30":
    print(int(a)+1,"/",b,"/",c)
elif (b=="01" or b=="03" or b=="05" or b=="7" or b=="09" or b=="10") and a=="31":
    print("01/",int(b)+1,"/",c)
if (b=="04" or b=="06" or b=="08" or b=="11")and a<="29":
    print(int(a)+1,"/",b,"/",c)
elif (b=="04" or b=="06" or b=="08" or b=="11")and a<="30":
    print("01/",int(b)+1,"/",c)
if b=="12" and a=="31":
    print("01/01/",int(c)+1)
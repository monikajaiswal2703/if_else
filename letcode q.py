

# a=[1,2,3]
# b=[4,5,6]
# s=""
# s1=""
# i=1
# while i<len(a)+1:
#     s+=str(a[-i])
#     s1+=str(b[-i])
#     i+=1
# print(s)
# print(s1)
# c=int(s)+int(s1)
# d=str(c)
# e=''
# for i in range(1,(len(d)+1)):
#     e+=d[-i]
# print(e)


# a=[[4,5,6],[6,7,8],[9,10],[4,5,6,7]]
# s=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             s+=a[i][j]
#         if (len(a[i])-1)==j and i!=0:
#             s+=a[i][j]
#         j+=1
#     i+=1
# print(s)


# s='abcabcbb'
# c=[]
# for i in s:
#     if i not in c:
#         c.append(i)
# d=0
# for i in c:
#     d+=1
# print(d)

# nums1 = [1,3]
# nums2 = [2]
# sum=0
# c=nums1+nums2
# print(c)
# for i in c:
#     sum+=i
#     s=sum/len(c)
# print(s)

# n = int(input())
# arr = map(int, input().split())
# arr=sorted(arr)
# l=[]
# for i in range(len(arr)):
#     if arr[i]<max(arr):
#         l.append(arr[i])
# print(max(l))
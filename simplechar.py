# import math
length=int(input())
str1=input()
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for i in l:
    var=str1[i-1]  
    print(str1[:i-1].count(var))
    
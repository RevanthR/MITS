from itertools import combinations
from collections import Counter
a=input()
l=[int(x) for x in a.split()]
# l=[234,567,321,345,123,110,767,111]
l=l[1:]
# print(l)
l1=[]
for i in l:
    i=[int(x) for x in str(i)]
    a=min(i)
    b=max(i)
    c=(b*11)+(a*7)
    c=str(c)
    if len(c)>=3:
        c=c[len(c)-2:len(c)]
    l1.append(int(c))

l2=[]
for i in l1:
    i=str(i)
    c=i[0]
    l2.append(int(c))

even=[]
odd=[]
i=0
for i in range(len(l2)):
    if i%2==0:
        even.append(l2[i])
    else:
        odd.append(l2[i])


o1=list(combinations(odd,2))
e1=list(combinations(even,2))
p1=[]
p2=[]
for i in o1:
    if max(i)==min(i):
        p1.append(i)
for j in e1:
    if max(j)==min(j):
        p1.append(j)
count=0
fin=Counter(p1)
fin=dict(fin)
for i in fin.values():
    if i>2:
        count=count+2
    else:
        count=count+i
print(count)
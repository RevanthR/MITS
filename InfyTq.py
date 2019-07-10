import re
a=input()
s=''
l=re.findall('\w\d*',a)
s=s.join(l)
diff=len(a)-len(s)
l1=re.findall('\d+',s)
s1=''
s1=s1.join(l1)
s1=[int(x) for x in s1]
l1=[]
l2=[]
for i in range(len(s1)):
    if s1[i]%2==0:
        l1.append(s1[i])
    else:
        l2.append(s1[i])
f=[]
i=j=k=0
if diff%2!=0:
    while i<(len(l1)+len(l2)):
        if i%2==0:
            f.append(l2[j])
            j=j+1
        else:
            f.append(l1[k])
            k=k+1
        i=i+1
else:
    while i<(len(l1)+len(l2)):
        if i%2==0:
            f.append(l1[j])
            j=j+1
        else:
            f.append(l2[k])
            k=k+1
        i=i+1

f=[str(x) for x in f]
s3=''
s3=s3.join(f)
print(int(s3))
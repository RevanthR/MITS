l1=input()
l2=input()
l1=[x for x in l1]
print(l1)

l2=[x for x in l2]
print(l2)
l3=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        l3.append(int(l1[i]+l2[-(i+1)]))
    print(l3)
else:
    print("String Length is not equal")

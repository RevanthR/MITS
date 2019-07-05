import re
str1="Write a program to calculate the frequency of words present in a given sentence. Display the output in such a way that the keys are in sorted order where every key and value is separated by “->” symbol?"
x=re.findall('\w+',str1)
x=set(x)

for a in x:
    print(a,str1.count(a))
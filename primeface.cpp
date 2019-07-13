#include <stdio.h> 
#include <string.h>
#include<iostream>
#include<math.h>
using namespace std;

char reVal(int num) 
{ 
	if (num >= 0 && num <= 9) 
		return (char)(num + '0'); 
	else
		return (char)(num - 10 + 'A'); 
} 

// Utility function to reverse a string 
void strev(char *str) 
{ 
	int len = strlen(str); 
	int i; 
	for (i = 0; i < len/2; i++) 
	{ 
		char temp = str[i]; 
		str[i] = str[len-i-1]; 
		str[len-i-1] = temp; 
	} 
} 


int fromDeci(char res[], int base, int inputNum) 
{ 
	int index = 0;  
	while (inputNum > 0) 
	{ 
		res[index++] = reVal(inputNum % base); 
		inputNum /= base; 
	} 
	res[index] = '\0'; 

	 
	strev(res); 

	return index; 
} 



int val(char c) 
{ 
    if (c >= '0' && c <= '9') 
        return (int)c - '0'; 
    else
        return (int)c - 'A' + 10; 
} 

int toDeci(char *str, int base) 
{ 
	int len = strlen(str); 
	int power = 1;  
	int num = 0;  
	int i; 
	
	for (i = len - 1; i >= 0; i--) 
	{ 
		 
		

		num += val(str[i]) * power; 
		power = power * base; 
	} 

	return num; 
} 
 int prime(int n)
{
	int i;
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
			return 0;
	}
	return 1;
}
int main()
{
char N[100],B,N1[100],*N2;
int i=0,l,k1=-1,k=0,num,l1;
cin>>N>>B;
l=strlen(N);
for(i=0;i<l;i++){

if(N[i]>=48&&N[i]<=57)
k=N[i]-47;
else
k=10+N[i]-64;

if(k>k1)k1=k;
}
if(B>=48&&B<=57)
k=B-47;
else
k=10+B-64;

num=toDeci(N,k1);
if(num<k)num=k-1;


while(1)
{

l1=fromDeci(N1,k,num);

if(N1[l1-1]==B)
if(prime(num))break;
num=num+1;
}
cout<<N1;	
}

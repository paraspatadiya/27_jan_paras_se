#include<iostream>
using namespace std;
int n1,n2,choice;

void sum(int a,int b)
{
	cout<<"\nsum:"<<a+b;
}
void min(int a,int b)
{
	cout<<"\nmin:"<<a-b;
}
void mul(int a,int b)
{
	cout<<"\nmul:"<<a*b;
}
void div(int a,int b)
{
	cout<<"\ndiv:"<<a/b;
}
main()
{
	cout<<"enter a:";
	cin>>n1;
	cout<<"enter b:";
	cin>>n2;
	cout<<"enter your choice:1=+,2=-,3=*,4/";
	cin>>choice;
	
	switch (choice)
	{
		case 1:
		sum(n1,n2);	
		break;
	
	
		case 2:
		min(n1,n2);	
		break;
	
	
		case 3:
		mul(n1,n2);	
		break;
	
	
		case 4:
		div(n1,n2);	
		break;
	}
}

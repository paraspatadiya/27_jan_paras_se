#include<iostream>
using namespace std;
main()
{
	int numbers[5],i,sum,avg;
	cout<<"enter 5 numbers:";
    for (i=0;i<5;i++) 
	{
		cout<<"\nenter number"<<i+1<<":";	
		cin>>numbers[i];
	}	
	sum += numbers[i];
	cout<<"\nsum of numbers is:"<<sum;
	avg=sum/2;
	cout<<"\naverage of numbers is:"<<avg;
}

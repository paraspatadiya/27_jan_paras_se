#include<iostream>
using namespace std;

class calculation
{
	public:
	
	int sum(int a,int b)
	{
		cout<<"\nsum:"<<a+b;
	}
	int min(int a,int b)
	{
		cout<<"\nmin:"<<a-b;
	}
	int mul(int a,int b)
	{
		cout<<"\nmul:"<<a*b;
	}
	int div(int a,int b)
	{
		cout<<"\ndiv:"<<a/b;
	}
};
main()
{
	
	calculation cal;
	cal.sum(10,30);
	cal.min(10,30);
	cal.mul(10,30);
	cal.div(10,30);
}

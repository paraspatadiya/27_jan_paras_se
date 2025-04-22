#include<iostream>
using namespace std;
class getdata
{
	public:
	int l,b;

	void enter()
	{
		cout<<"enter value of l:";
		cin>>l;
		cout<<"enter value of b:";
		cin>>b;
	}
	
};
class print : public getdata
{
	public:
	void provide()
	{
		cout<<"area of ractangle is:"<<l*b;
	}
};
main()
{
	print pr;
	pr.enter();
	pr.provide();
}

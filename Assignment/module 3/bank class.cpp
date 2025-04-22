#include<iostream>
using namespace std;
class getdata
{
	public:

	int no,type;
	string name;
	void enterdetail()
	{
		cout<<"account no:";
		cin>>no;
		cout<<"\naccount holder name:";
		cin>>name;
		cout<<"\nenter account type:press 1:saving/2:current";
		cin>>type;
	}
};
class deposite : public getdata
{
	public:
	int dep;
	void enteryamount()
	{
		cout<<"\nenter amount you want to deposite(min-2000)";
		cin>>dep;
		if(dep>2000)
		{
			cout<<"\nyour amount is deposited succsessfully";
		
		}
		else
		{
		cout<<"\nplesase deposite 2000 or above";
		}
	}
};
class withdrawal : public deposite
{
	public:

	int wid;
	void outamount()
	{
		cout<<"\nenter amount you want to withdrawal:";
		cin>>wid;
		if(dep>wid)
		{
			cout<<"\nyour amount is withdrawed successfully";
			
		}
		else
		{
			cout<<"your balance is insuficiant";
		}
	}
};
class statment: public withdrawal
{
	public:
	void laststatment()
	{
	cout<<"\nyour acount number is:"<<no;
	cout<<"\naccount holder's name' is:"<<name;
	cout<<"\nyour diposited amount is:"<<dep;
	cout<<"\nyout withdrawlal amount is :"<<wid;
	cout<<"\nyour current balance is :"<<dep-wid;
	}
	

};

main()
{
	statment st;
	st.enterdetail();
	st.enteryamount();
	st.outamount();
	st.laststatment();

	
}

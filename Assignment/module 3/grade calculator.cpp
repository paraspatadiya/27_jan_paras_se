#include<iostream>
using namespace std;
main()
{
	int s1,s2,s3,s4,total;
	float per;
	
	cout<<"\nenter marks of s1:";
	cin>>s1;
	cout<<"\nenter marks of s2:";
	cin>>s2;
	cout<<"\nenter marks of s3:";
	cin>>s3;
	cout<<"\nenter marks of s4:";
	cin>>s4;
	
	if(s1>=40&& s2>=40&&s3>=40&& s4>=40)
	
	total=s1+s2+s3+s4;
    cout<<"\ntotal="<<total;	
	per=total/4;
	cout<<"\npercentage="<<per;
	
	if(per>=70)
	{
        cout<<"\ngrade:a+";
	}
	else if(per>=50)
	{
		cout<<"\ngrade:b";

	}
	else if(per>=35)
	{
		cout<<"\ngrade:c";
	}
	else
	{
		cout<<"\nfail.....";
	}
}

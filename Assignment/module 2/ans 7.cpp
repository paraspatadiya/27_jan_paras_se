#include<stdio.h>
main()
{
	int p;
	for (p = 1; p <= 10 ; p++)
	{
		if(p==3)
		{
			continue;
		}
		if(p==5)
		{
			break;
		}
		printf("\n%d",p);
	
	}
}

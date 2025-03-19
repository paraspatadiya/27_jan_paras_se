#include<stdio.h>
main()
{
	int number,mon;
	printf("enter any number :");
	scanf("%d",&number);
	
	if (number % 2 == 0)
	{
		printf("\n%d number is even",number);
		
	}
	else 
	{
		printf("\n%d number is odd",number);
	}
	
	printf("\nenter a number between 1-12 for month :");
	scanf("%d",&mon);
	
	switch (mon)
	{
		case 1 :
		printf("\njanuary");
		break;
		case 2 :
		printf("\nfebruary");
		break;
		case 3 :
		printf("\nmarch");
		break;
		case 4 :
		printf("\napril");
		break;
		case 5 :
		printf("\nmay");
		break;
		case 6 :
		printf("\njune");
		break;
		case 7 :
		printf("\njuly");
		break;
		case 8 :
		printf("\naugust");
		break;
		case 9 :
		printf("\nseptember");
		break;
		case 10 : 
		printf("\noctober");
		break;
		case 11 :
		printf("\nnovember");
		break;
		case 12 :
		printf("\ndecember");
		break;
		default :
		printf("invalid number");
	}
	
}

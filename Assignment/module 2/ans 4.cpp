#include<stdio.h>
main()
{
	int n1,n2;
	printf("enter two numbers:");
	scanf("%d %d",&n1,&n2);
	
	printf("\nArithmetic operation");
	printf("\nsum= %d",(n1+n2));
	printf("\nmin= %d",(n1-n2));
	printf("\ndiv= %d",(n1/n2));
	printf("\nmul= %d",(n1*n2));
	
	printf("\nrelational operation");
	printf("\n%d == %d = %d",n1,n2,n1 == n2);
	printf("\n%d != %d = %d",n1,n2,n1 != n2);
	printf("\n%d < %d = %d",n1,n2,n1 < n2); 
	printf("\n%d > %d = %d",n1,n2,n1 > n2);
	
	printf("\nlogical operations");
	printf("\n%d && %d = %d", n1, n2, n1 && n2);
	printf("\n%d || %d = %d", n1, n2, n1 || n2);
	printf("\n!%d = %d = %d", n1, ! n1);

}

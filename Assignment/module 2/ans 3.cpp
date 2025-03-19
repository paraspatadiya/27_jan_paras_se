#include<stdio.h>
#define pi 3.14
main()
{
	int age = 19;
	char personality[10]="dynamic";
	float height = 5.6;
	const int month = 3;
	
	printf("\nage:= %d",age);
	printf("\npersonality:= %s",personality);
	printf("\nheight:= %.2f",height);
	printf("\nmonth:= %d",month);
	printf("\nvalue of pi:= %f",pi);
}

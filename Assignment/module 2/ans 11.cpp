#include<stdio.h>
#include<string.h>
main()
{
	char str1[100],str2[100];
	printf("enter first string:");
	scanf("%s",str1);
	printf("enter second string:");
	scanf("%s",str2);
	
	strcat(str1,str2);
	
	printf("\nConcatenated String: %s",str1,str2);
	printf("\nLength of concatenated string: %lu\n", strlen(str1));
}

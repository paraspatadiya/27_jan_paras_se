#include<stdio.h>
main()
{
	int arr[5] = {1,2,3,4,5},i=0,j=0;
	printf("\none dimensional array elements");
	for (int i=0;i<5;i++);
	{
		printf("%d",arr[i]);
	}
	int matrix [3][3]=
		{
		{1 , 2 , 3},
		{4 , 5 , 6},
		{7 , 8 , 9}
		};
	int sum = 0;
	printf("\n\ntwo dimensional array(3x3 matrix)\n");
	for (int i=0;i<3;i++){
		for(int j=0;j<3;j++){
		printf("%d",matrix[i][j]);
		sum += matrix[i][j];
	}
	printf("\n");
}
	printf("\nsum of all elements: %d\n",sum);
}

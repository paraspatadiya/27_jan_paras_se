#include<stdio.h>
main()
{
	int choice,qty,totalamount = 0,amount;
	char moreOrders;
	do {
		printf("---------menu---------");
		printf("\n1. pizza     price = 200rs/pcs");
		printf("\n2. dosa      price = 120rs/pcs");
		printf("\n3. drink     price = 20rs/pcs");
		printf("\n4. idli      price = 50rs/pcs");
		printf("\nchoose your meal : ");
		scanf("%d",&choice);
		printf("\nenter your quantity :");
		scanf("%d",&qty);   
		switch (choice)
		{
	
			case 1:
			printf("you selected pizza ");
			amount = 200 * qty;
			break;
				
			case 2:
			printf("you selected dosa ");
			amount = 120 * qty;
			break;

			case 3:
			printf("you selected drink ");
			amount = 20 * qty;
			break;
			
			case 4:
			printf("you selected pizza ");
			amount = 50 * qty;
			break;
		
			default: 
			printf("Invalid choice!\n");
		}
			
		totalamount += amount;
		printf("\namount:= %d",amount);
		printf("\ntotal amount:=%d",totalamount);
			
		printf("\ndo you want to place more orders? y or n");
		scanf(" %c",&moreOrders);
	
    }while (moreOrders == 'y' || moreOrders == 'Y');
		
		printf("\nfinal total amount: %d",totalamount),
		printf("\nthank you for orderning....");
		
		return 0;
	
}

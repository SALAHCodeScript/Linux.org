#include <stdio.h>

int main(){

    char symbol;
    int row, column;

    printf("Enter A Symbol Character: ");
    scanf("%c", &symbol);
    printf("Enter A Row Number: ");
    scanf("%d", &row);
    printf("Enter A Column Number: ");
    scanf("%d", &column);

    for(int r=0; r<=row; r+=1){
        for(int c=0; c<=column; c+=1){
            printf("%c", symbol);
        }
        printf("\n");
    }

    return 0;
}

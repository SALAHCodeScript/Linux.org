#include <stdio.h>

int main(){
    // Variables
    int x = 1; int y = 10;

    // While Loop
    while(x <= y){
        if(x == y){
            printf("%d\n", x);
            // Break The Loop
            break;
        }
        printf("%d\t", x);
        x++;
    }

    // Do While Loop
    do{
        // Do Something Even If It's False Once
        if(x == y){
            printf("%d", x);
            // Break The Loop
            break;
        }
        printf("%d\t", x);
        x++;
    } while(x <= y);

    return 0;
}
#include <stdio.h>

// Initializing A Function
void hello(char user[]);
double division(int x, int y);
int swap(int *x, int *y);

int main(){
    // Call A Function
    // // hello function
    printf("void hello():\n");
    hello("SALAH\n\n");
    // // division function
    printf("double division():\n%lf\n\n", division(4, 2));
    // // swap function
    int x = 5, y = 10;
    printf("int swap():\nbefore: %d %d\n", x, y);
    swap(&x, &y);
    printf("after:  %d %d\n", x, y);

    return 0;
}

// A Function
void hello(char user[]){
    printf("Hello, %s", user);
}
double division(int x, int y){
    return x / y;
}
int swap(int *x, int *y){    
    int temp = *x;
    *x = *y;
    *y = temp;
    return 0;
}


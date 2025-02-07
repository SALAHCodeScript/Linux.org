#include <stdio.h>

int main(){
    // Variable
    int start = 0; int end = 10; int step = 1;

    // For Loop
    for(int i = start; i <= end; i += step){
        if(i == end){
            printf("%d", i);
            // Break The Loop
            break;
        }
        if(i == 5){
            // Skip Something
            continue;
        }
        printf("%d\t", i);
    }
    return 0;
}
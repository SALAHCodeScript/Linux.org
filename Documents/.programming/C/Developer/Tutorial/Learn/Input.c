#include <stdio.h>

int main(){
    // Variables
    char name1[512]; int age1;
    char name2[512]; int age2;

    // scanf
    // Enter A New Value in Format Specifier
    printf("Name\n>_");
    scanf("%s", name1);
    printf("Age\n>_");
    scanf("%d", &age1);

    // gets
    // Enter A New Value in A New Line
    printf("Name\n>_");
    gets(name2);
    printf("Age\n>_");
    gets(age2);

    return 0;
}
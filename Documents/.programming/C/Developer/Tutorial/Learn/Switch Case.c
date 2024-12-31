#include <stdio.h>

int main(){

    char grade;

    printf("Enter A Grade: ");
    scanf("%c", &grade);

    switch (grade)
    {
    case 'A':
        printf("Perfect\n")
        break;
    case 'B':
        printf("You Did Good\n")
        break;
    case 'C':
        printf("You Did Okay\n")
        break;
    case 'D':
        printf("At Least It's Not F!\n")
        break;
    case 'F':
        printf("You Failed\n")
        break;
    default:
        printf("Please ENTER Only Grades\n");
    }

    return 0;
}

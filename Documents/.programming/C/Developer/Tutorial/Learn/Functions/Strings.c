#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(){
    // Variables
    char string1[] = "ben";
    char string2[] = "salah";
    char letter = 's';

    // Single Character: toupper()
    printf("%c\n", toupper(letter));
    // Single Character: tolower()
    printf("%c\n", tolower(letter));

    // Multiple Character: strcat()
    // // printf("%s\n", strcat(string1, string2));
    // Multiple Character: strcpy()
    // // printf("%s\n", strcpy(string1, string2));
    // Multiple Character: strncat()
    // // printf("%s\n", strncat(string1, string2, 1));
    // Multiple Character: strncpy()
    // // printf("%s\n", strncpy(string1, string2, 1));
    // Multiple Character: strlen()
    // // printf("%ld\n", strlen(string1));
    // Multiple Character: strstrcmp()
    // // printf("%s\n", strcmp(string1, string2));
    // Multiple Character: strncmp()
    // // printf("%s\n", strncmp(string1, string2, 1));

    return 0;
}

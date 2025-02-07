#include <stdio.h>

typedef char user[25];

typedef struct {
    char name[25];
    char password[12];
    int id;
} User;

int main(){

    user name = "Salah";
    User user = {"Salah", "password123", 1234121233};

    return 0;
}

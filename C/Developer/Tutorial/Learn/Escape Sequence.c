#include <stdio.h>

int main(){

    // Print A New Line
    puts("Hello\nI'm Groot");

    // Print A Tab Space
    puts("Hello\tI'm Groot");

    // Print Single/Double Quote '/" Inside Single/Double Quote
    puts("Hello I\"m Groot");
    puts("Hello I\'m Groot");

    // Print '\'
    puts("Hello I\\m Groot");

    // Print and Reomve One Thing Previous \b
    puts("H\be\bl\bl\bo\bI'm Groot");

    // Print and Reomve Everything Previous \r
    puts("Hello\r I'm Groot");

    // Print and Replace Everything Previous \f with Spaces for Each Thing
    puts("Hello\f I'm Groot");

    // Print Previous \v Normally and Next \v Print in A New Line Replacing Previous \v With Speacs for Each Thing
    puts("Hello\v I'm Groot");

    // Print \xxx Which x is Number
    puts("\241"); // \241 is The First Range ! \xxx | Doesn't Work With 8 & 9

    // Print \uxxxx Which x is Number
    puts("\x21"); // \x21 is The First Range

    return 0;
}

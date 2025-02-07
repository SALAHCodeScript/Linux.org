#include <stdio.h>
#include <math.h>

int main(){
    // Variables
    int x = 4, y = 2;

    // Arithmetic Operator: +
    printf("%d\n", x + y);
    // Arithmetic Operator: -
    printf("%d\n", x - y);
    // Arithmetic Operator: *
    printf("%d\n", x * y);
    // Arithmetic Operator: /
    printf("%f\n", x / (float) y);
    // Arithmetic Operator: %
    printf("%d\n", x % y);

    // Arithmetic Operator: ++
    x++;
    // Arithmetic Operator: --
    y--;

    // Augmented Assignment Operator: +=
    x += 1;
    // Augmented Assignment Operator: -=
    y -= 1;
    // Augmented Assignment Operator: *=
    x *= 1;
    // Augmented Assignment Operator: /=
    y /= 1;
    // Augmented Assignment Operator: %=
    x %= 1;

    // Math: Square Root
    int squareRoot = sqrt(4);
    // Math: Power
    int power = pow(2, 4);
    // Math: Round
    int round_num = round(3.14);
    // Math: Ceil
    int ceil_num = ceil(3.14);
    // Math: Floor
    int floor_num = floor(3.14);
    // Math: Abs
    int abs = fabs(-1);
    // Math: Log
    int log_num = log(3);
    // Math: Sin
    int sin_num = sin(3);
    // Math: Cos
    int cos_num = cos(3);
    // Math: Tan
    int tan_num = tan(3);

    return 0;
}

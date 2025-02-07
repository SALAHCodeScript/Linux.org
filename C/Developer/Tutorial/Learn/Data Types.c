#include <stdio.h>

int main(){
	// String: Single Character
	char letter = 'A';
	// String: Multiple Character
	char name[] = "SALAH";
	// String: Specific Character Numbers
	char three[3] = "333";

	// Number: Integer
	int int_num = 1;
	// Number: Float
	float float_num = 1.0;
	// Number: Double
	double double_num = 1.11111;

	// Long Number: Integer
	long int long_int_num = 111111111111;
	// Long Number: Double
	long double long_double_num = 111111111111111.11111111;
	// Long Long Number: Integer
	long long int long_long_int_num = 111111111111111111;

	// Unsigned Number: Integer
	unsigned int unsigned_int_num = 1;
	// Signed Number: Integer
	signed int signed_int_num = -1;
	// Long Unsigned Number: Integer
	long unsigned int long_unsigned_int_num = 111111111111;
	// Long Signed Number: Integer
	long signed int long_signed_int_num = -111111111111;
	// Long Long Unsigned Number: Integer
	long long unsigned int long_long_unsigned_int_num = 111111111111111111;
	// Long Long Signed Number: Integer
	long long signed int long_long_signed_int_num = -111111111111111111;


	// Pointer: Single Character
	char *string = name;
	// Pointer: Multiple Character
	char *character = &letter;

	// Pointer: Integer
	int *pointer_int_num = &int_num;
	// Pointer: Float
	float *pointer_float_num = &float_num;
	// Pointer: Double
	double *pointer_double_num = &double_num;

	// Pointer: Long Integer
	long int *pointer_long_int_num = &long_int_num;
	// Pointer: Long Long Integer
	long long int *pointer_long_long_int_num = &long_long_int_num;
	// Pointer: Long Double
	long double *pointer_long_double_num = &long_double_num;

	// Pointer: Unsigned Integer
	unsigned int *pointer_unsigned_int_num = &unsigned_int_num;
	// Pointer: Signed Integer
	signed int *pointer_signed_int_num = &signed_int_num;
	// Pointer: Long Unsigned Integer
	long unsigned int *pointer_long_unsigned_int_num = &long_unsigned_int_num;
	// Pointer: Long Signed Integer
	long signed int *pointer_long_signed_int_num = &long_signed_int_num;
	// Long Long Unsigned Number: Integer
	long long unsigned int *pointer_long_long_unsigned_int_num = &long_long_unsigned_int_num;
	// Long Long Signed Number: Integer
	long long signed int *pointer_long_long_signed_int_num = &long_long_signed_int_num;

	return 0;
}

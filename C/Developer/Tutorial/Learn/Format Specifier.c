#include <stdio.h>

int main(){
	// Format Specifier: String
	printf("%s\t", "Hello, World");
	// Format Specifier: Character
	printf("%c\n", 'A');

	// Format Specifier: Integer
	printf("%d\t", 1);
	// Format Specifier: Float
	printf("%f\t", 1.0);
	// Format Specifier: Double
	printf("%lf\t%a\n", 1.0, 1.0);

	// Format Specifier: Long Integer
	long int x = 11111111111;
	printf("%ld\t", x);
	// Format Specifier: Long Double
	long double y = 1111111111.0;
	printf("%La\n", y);

	// Format Specifier: Signed Integer
	signed int xy = -1;
	printf("%d\t", xy);
	// Format Specifier: Unsigned Integer
	unsigned int yx = 1;
	printf("%d\n", xy);

	// Format Specifier: Address
	char charc = 'B'; char word[] = "Words";
	int a = 1; float b = 1.0; double c = 1.0;
	long int ab = 1; long double ac = 1.0;
	unsigned int ba = 1; signed int bc = -1;
	printf("%p  %p\n%p  %p  %p\n%p  %p\n%p  %p", &charc, &word, &a, &b, &c, &ab, &ac, &ba, &bc);

	return 0;
}

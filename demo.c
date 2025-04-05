#include "printff.h"

#define printf printff

int main() {
	printf("Hello %, % + % = %\n", "World", 3.0, 1, 3.0 + 1);
	return 0;
}

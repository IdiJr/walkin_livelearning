#include <stdio.h>

int add(int x, int y)
{
	return (x + y);
}

int main (void)
{
	/* int n; */
	/* int *ptr; */
	/* ptr = &n; */
	int (*func_ptr)(int, int); /* define a function pointer */
	func_ptr = &add; /* "func_ptr = add;" is also valid. removing this line causes a seg error since there is no link to function pointer and func */

	int result;

	result = func_ptr(2, 4); /* "result = (*func_ptr)(2, 4)" also works*/
	printf("%d\n", result);
	return (0);
}

/** 
 * A C program that replaces each element in array with either 0 if the element is divisible by 2 and 1 if otherwise  
 * [5, 4, 3, 7] <=> [1, 0, 1, 1] eg: 5 is not divisible by 2 perfectly hence the result is 1 the same for the rest 
 * demostrates how to create function that has in its arguments another function
 * int func_int *arr, size_t size, void ((*func*ptr)(int, int))
 */
#include <stdio.h>

void replace_odd_even(int *array, size_t size)
{
	for (int i = 0; i < size; i++)
	{
		if (array[i] % 2 == 0)
		{
			array[i] = 0;
		}
		else
		{
			array[i] = 1;
		}
	}
}
void print_array(int *array, size_t size)
{
	printf("[");
	for (int i = 0; i < size; i++)
	{
		printf("%d", array[i]);
		if (i < size -1 )
		{
			printf(", ");
		}
	}
	printf("]\n");
}
void modify_array(int *array, size_t size, void (*func_ptr)(int *, size_t))
{
	if (array  != NULL && func_ptr != NULL)
		func_ptr(array, size);
}

int main(void)
{
	int array[] = {2, 5, 3, 4, 6, 10};
	size_t size = sizeof(array) / sizeof(int);
	printf("This is the original array: ");
	print_array(array, size);
	
	modify_array(array, size, replace_odd_even);
	printf("\nThis is the modified array: ");
	print_array(array, size);
}

// Write a program that prints a string => _putchar & printf

#include <unistd.h>

int _putchar(char c)
{
	return (write(1, &c, 1));
}

int main(void)
{
	char *str = "Hello World";
	int i = 0;

	while(str[i] != '\0')
	{
		_putchar(str[i]);
		i++; //increments the value of i after running the code each time."++i" does the opposite
	}
	_putchar('\n');
	return(0);
}

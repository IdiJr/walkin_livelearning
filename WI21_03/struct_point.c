#include <stdio.h>

struct Student
{
	char *name;
	char *email;
	float scores;
};
int main(void)
{
	struct Student student1; 
	/* "Student" is the struct we defined and "student1" is the variable and can be changed */
	struct Student *ptr;
	ptr = &student1;
	/* dereferencing the pointer before accessing the data with "." symbol */

	(*ptr). name = "John Doe";

	/* We can also use "->" to do the same */
	ptr->email = "j.doe@gmail.com";
	ptr->scores = 124.467;

	printf("\t\nName        :%s",student1.name);
	printf("\t\nEmail   :%s",student1.email);
	printf("\t\nScores  :%f\n",student1.scores);
	return (0);
}

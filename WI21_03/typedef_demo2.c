#include <stdio.h>

typedef struct Student
{
	char *name;
	char *email;
	float scores;
} student_t;
/* renames the datatype "struct Student" to student_t */

int main(void)
{
	student_t student1;
	student1.name = "John Doe";
	student1.email = "j.doe@gmail.com";
	student1.scores = 124.3;
	struct Student student2 = {"Jane Doe", "jane@outlook.com", 199.0094};

	printf("\nName   :%s",student1.name);
	printf("\nEmail	 :%s",student1.email);
	printf("\nScores :%f\n",student1.scores);
	return (0);
}

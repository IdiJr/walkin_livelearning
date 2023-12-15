#include <stdio.h>

struct Student
{
	char *name;
	char *email;
	float scores;
};
int main(void)
{
	/* struct Student student1 = {"John Doe", "j.doe@gmail.com", 124.3}; */
	struct Student student1;
	student1.name = "John Doe";
	student1.email = "j.doe@gmail.com";
	student1.scores = 124.3;
	struct Student student2 = {"Jane Doe", "jane@outlook.com", 199.0094};

	printf("\t\nName	:%s",student1.name);
	printf("\t\nEmail   :%s",student1.email);
	printf("\t\nScores  :%f\n",student1.scores);
	return (0);
}

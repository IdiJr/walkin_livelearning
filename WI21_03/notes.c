int add_two_numbers(int a, int b);
/* "int" is the data type, "add_two_numbers" is the function, and "int a, int b" is the argument */
struct Student *create_new_student(char *name, char *email, float scores);
/**
 * "struct Student" is the data type, "*create_new_student" is the function,
 * and "char *name, char *email, float scores" is the argument
 * creates a function that accepts a name, email and scores then, returns a pointer to student
 */

char a = 'b';
char name = "Jane";
char *name = "Jane"; //base address of the string *name = 'J', *(name+1) = 'a'; .... *(name+5) => '\0';

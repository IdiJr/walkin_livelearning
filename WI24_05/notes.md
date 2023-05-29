# LIFO & FIFO

* LIFO - last in first out (for the stacks) and FIFO - first in first out (for the queues).

* push 1 - `push` is the opp code and `1` is the argument. There can be a number of spaces between the opp code and argument.

* The monty byte codes can contain blank spaces or lines made of spaces only. It only takes into account the opp code and its required arguement and ignoring the remaining texts.
```
eg: push 0 push 0 onto the stack
```
the above example will only execute the first `push 0` and ignore the rest of the line.

* Write the code into `monty.c` and compile into output `monty`. The code should return an error message when more than one argument is run with the programme. It should be able to validate arguments using `argv and argc`. 

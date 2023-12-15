#!/usr/bin/python3
"""A basic console program to help execute python almost a circle
tasks from the terminal 
"""

import cmd
from models.base import Base


class Console(cmd.Cmd):
    prompt = "(Abnb )"
    intro = "Welcome to Ali's Airbnb console"

    def do_exit(self, arg):
        'Quits the console'
        print('Thank you for using Abnb')
        return True

    def do_EOF(self, arg):
        'Exits the console when EOF is input or Ctrl-D is entered'
        return True

    def do_create(self, arg):
        """Creates a object of Base and print it's ID"""
        if arg:
            try:
                id = int(arg)
                object = Base(id)
                print(object.id)
            except ValueError:
                print("Error: Argument is not an integer")
            else:
                object = Base()
                print(object.id)

if __name__ == "__main__":
    Console().cmdloop()

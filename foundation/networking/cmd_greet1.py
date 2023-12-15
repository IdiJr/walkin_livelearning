import cmd
""" This adds help to the greet command.
"""


class HelloWorld(cmd.Cmd):
    """Simple command processor example"""

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print("hi")

    def do_EOF(self, line):
        'Close the cmd window, and exit: when EOF or Ctrl-D is input'
        print('Thank you for using cmd_greet')
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()

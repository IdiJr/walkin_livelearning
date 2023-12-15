import cmd
"""
Live Help: this version makes use of help_greet() method
this help handler produce help text for the named command.
it takes care of the whitespace removed from the docstring
to keep the application well formated
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

    def help_greet(self):
        print ('\n'.join([ 'greet <person>',
            'Greet the named person',
            ]))

    def do_EOF(self, line):
        'Close the cmd window, and exit: when EOF or Ctrl-D is input'
        print('Thank you for using cmd_greet')
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()

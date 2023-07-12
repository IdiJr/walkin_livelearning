#!/usr/bin/python3
import cmd
""" Adds the auto completion functionality to the program.
when <tab> is pressed a completion is triggered, when there are
multiple completions possible, pressing <tab> twice list all
options.
"""


class HelloWorld(cmd.Cmd):
    """Simple command processor example"""
    prompt = "Karibu$ "
    intro = "Welcome to the gretn"

    FRIENDS = [ 'Emmanuel', 'Ellis', 'Cuticle', 'Adams', 'Ahmed', 'John', 'Alice', 'Bobby', 'Barbara' ]

    def do_greet(self, person):
        """Greet the named person"""
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "Hey, " + person
        else:
            greeting = 'Hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                    for f in self.FRIENDS
                    if f.startswith(text)
                    ]
        return completions

    def help_greet(self):
        print ('\n'.join([ 'greet <person>',
            'Greet the named person',
            ]))

    def do_exit(self, arg):
        'Quits the console'
        print('Thank you for using Karibu')
        return True
    
    def do_EOF(self, line):
        'Close the cmd window, and exit: when EOF or Ctrl-D is input'
        print('Thank you for using Karibu')
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()

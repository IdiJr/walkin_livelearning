import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example"""

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        'Close the cmd window, and exit: BYE'
        print('Thank you for using cmd_greet')
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()

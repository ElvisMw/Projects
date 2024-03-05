import cmd

class MyCmd(cmd.Cmd):
    """A simple command line interpreter"""

    def do_greet(self, line):
        """- Greets user."""
        print(f"Hello World")

    def do_EOF(self, line):
        """- Exits cmd with keyboard interrupt."""
        print(f"Exiting Program. Bye!")
        return True

    def default(self, line):
        print(f"Unknown command: {line}")

if __name__ == '__main__':
    """Enter the command loop"""
    MyCmd().cmdloop()

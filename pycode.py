#!/usr/bin/python3
"""This the beautiful code that passes the pycodestyle checks
"""
import cmd


class console(cmd.Cmd):
    """This is body of the class
    """
    def do_greet(self, person):
        """This is go greet method
        """
        print("Hello ,", person)

    def do_EOF(self, line):
        """This is go EOF method
        """
        return True


if __name__ == "__main__":
    console().cmdloop()

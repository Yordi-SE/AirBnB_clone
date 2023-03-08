#!/usr/bin/python3
"""This module contain defination
of console class
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is body of
    the class
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """This method exit
        the programm
        """
        return True
    
    def do_EOF(self, line):
        """This method exit
        the programm
        """
        return True

    def emptyline(self):
        """This method is called
        if the line is empty line
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""This module contain defination
of console class
"""
import cmd
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is body of
    the class
    """
    prompt = "(hbnb) "

    def do_create(self, cl):
        """This method creates new
        instance of BaseModel
        """
        if cl == "":
            print("** class name missing **")
        else:
            try:
                inst = eval(cl)()
                inst.save()
                print(inst.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, cl):
        """This method prints the string
        representation of an instance
        """
        if cl:
            tokens = cl.split()
            if len(tokens) >= 2:
                cll = tokens[0].strip()
                idd = tokens[1].strip()
            elif len(tokens) == 1:
                cll = tokens[0].strip()
                idd = ""
            elif len(tokens) == 0:
                cll = ""
                idd = ""
            try:
                m = "{}.{}".format(eval(cll).__name__, idd)
            except NameError:
                print("** class doesn't exist **")
                return
            if idd == "":
                print("** instance id missing **")
                return
            storage.reload()
            my_dict = storage.all()
            if m not in my_dict.keys():
                print("** no instance found **")
                return
            else:
                print(my_dict[m])
        else:
            print("** class name missing **")

    def do_destroy(self, cl):
        """This method is used
        to destroy an instance
        """
        if cl:
            tokens = cl.split()
            if len(tokens) >= 2:
                cll = tokens[0].strip()
                idd = tokens[1].strip()
            if len(tokens) == 1:
                cll = tokens[0].strip()
                idd = ""
            if len(tokens) == 0:
                cll = ""
                idd = ""
            try:
                m = "{}.{}".format(eval(cll).__name__, idd)
            except NameError:
                print("** class doesn't exist **")
                return
            if idd == "":
                print("** instance id missing **")
                return
            storage.reload()
            my_dict = storage.all()
            if m not in my_dict.keys():
                print("** no instance found **")
                return
            else:
                del my_dict[m]
                storage.save()
        else:
            print("** class name missing **")

    def do_all(self, cl):
        """This method is used
        to show all avialable instances
        """
        if cl:
            try:
                name = eval(cl).__name__
                storage.reload()
                my_dict = storage.all()
                for values in my_dict.values():
                    print(values)
            except NameError:
                print("** class doesn't exist **")
        else:
            storage.reload()
            my_dict = storage.all()
            for values in my_dict.values():
                print(values)

    def do_update(self, cl):
        """This method is used
        to update an instance
        """
        if cl:
            tokens = re.findall(r'(?:"[^"]*"|\S)+', cl)
            if len(tokens) >= 4:
                cll = tokens[0]
                idd = tokens[1]
                att = tokens[2]
                attrv = tokens[3]
                print(attrv)
            elif len(tokens) == 3:
                cll = tokens[0]
                idd = tokens[1]
                att = tokens[2]
                attrv = ""
            elif len(tokens) == 2:
                cll = tokens[0]
                idd = tokens[1]
                att = ""
                attrv = ""
            elif len(tokens) == 1:
                cll = tokens[0]
                idd = ""
                att = ""
                attrv = ""
            try:
                m = "{}.{}".format(eval(cll).__name__, idd)
            except NameError:
                print("** class doesn't exist **")
                return
            if idd == "":
                print("** instance id missing **")
                return
            storage.reload()
            my_dict = storage.all()
            if m not in my_dict.keys():
                print("** no instance found **")
            elif att == "":
                print("** attribute name missing **")
            elif attrv == "":
                print("** value missing **")
            else:
                try:
                    my_dict[m].__dict__[att] = eval(attrv)
                except NameError:
                    my_dict[m].__dict__[att] = attrv
                storage.save()
        else:
            print("** class name missing **")

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

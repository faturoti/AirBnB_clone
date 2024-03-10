#!/usr/bin/python3
"""
Entry point for console class
"""
import cmd
import json
import re
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    """
    This is the console that will run in loops
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Handles the 'quit' command
        
        Args:
            line(args): input argument for quiting
            the terminal
        """
        return True
    
    def do_EOF(self, line):
        """To handle end of file command

        Args:
            line(args): input argument for quiting terminal
        """
        return True

    def handle_empty_line(self, line):
        """ Methos that handle empty lines"""
        return False

    def handle_errors(self, line, num_of_args):
        """
        Displays error messages to user

        Args:
            line(any): gets user input using command lin
            num_of_args(int): number of input arguments
        """
        classes = ["BaseModel", "User", "State", "City", 
                    "Amenity", "Place", "Review"]
        msg = ["** class name missing **",
                "** class doesn't exist **",
                "** instance id missing **",
                "** no instance found **",
                "** attribute name missing **",
                "** value missing **"]

        if not line:
            print (msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute

        Args:
            line(args): receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
        """
        if (self.handle_errors(line, 4) == 1):
            return
        args = line.split()
        d = storage.all()

        for i in range(len(args[1:]) + 1):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + "." + args[1]
        attr_k = args[2]
        attr_v = args[3]

        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        class_attr = type(d[key]).__dict__
        if attr_k in class_attr.keys():
            try:
                attr_v = type(class_attr[key])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return
        setattr(d[key], attr_k, attr_v)
        storage.save()

    def do_create(self, line):
        """It creates new instance of any class specified
        and prints the ID

        Args:
            line(args): Arguments to enter with command: <class name>
        """
        if (self.handle_errors(line, 1) == 1):
            return
        args = line.split(" ")

        """
        args[0] contains class name, create new instance
        """
        obj = eval(args[0])()
        obj.save()

        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance 
        based on the class name
         Args:
            line(line): to enter with command <class name> <id>
        """
        if (self.handle_errors(line, 2) == 1):
            return
        args = line.split()
        d = storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + "." + args[1]
        print(d[key])

if __name__ == '__main__':
    HBNBCommand().cmdloop()

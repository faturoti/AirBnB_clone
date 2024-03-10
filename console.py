#!/usr/bin/python3
"""
Entry point for console class
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

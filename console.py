#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter should implement:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
    a custom prompt: (hbnb)
    an empty line + ENTER shouldn’t execute anything
    Your code should not be executed when imported
    """
    intro = ""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, args):
        """Exits the shell when Ctrl+D is pressed"""
        return True
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
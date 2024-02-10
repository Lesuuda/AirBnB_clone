#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
"""


import cmd
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel}


def validate_class(args, id=True):
        """validates the class and the number of arguments provided"""
        args_list = args.split()

        if len(args_list) < 1:
            print("** classname missing **")
            return False
        if args_list[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        if id and len(args_list) < 2:
            print("** instance id missing **")
            return False
        if id:
            instance_id = args_list[1]
            print(type(instance_id))
            key = "{}".format(instance_id)
            if key not in storage.all():
                print("** no instance found **")
                print(type(key))
                return False
        return True

       

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


    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args_list = args.split()

        if len(args_list) < 1:
            print("** classname missing **")
            return False
        if args_list[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        else:
            new_instance = BaseModel()
            storage.save()
            print(new_instance.id)


    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args_list = args.split()
        if len(args_list) < 1:
            print("** classname missing **")
            return False
        elif args_list[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif id and len(args_list) < 2:
            print("** instance id missing **")
            return False
        else:
            objects = storage.all()
            key = "{}.{}".format(args_list[0], args_list[1])
            required_key = objects.get(key, None)
            if required_key is None:
                print("** no instance found ***")
                return
            print(required_key)

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
        """
        args_list = args.split()
        if len(args_list) < 1:
            print("** classname missing **")
            return False
        elif args_list[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif id and len(args_list) < 2:
            print("** instance id missing **")
            return False
        else:
            objects = storage.all()
            key = "{}.{}".format(args_list[0], args_list[1])
            required_key = objects.get(key, None)
            if required_key is None:
                print("** no instance found ***")
                return
            del objects[key]
            storage.save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, args):
        """Exits the shell when Ctrl+D is pressed"""
        return True
    
    
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
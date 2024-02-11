#!/usr/bin/python3
"""
 contains the entry point of the command interpreter
 it enables us to perfom different tasks like creating, updating
 showing and destroying items
 Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models import storage

classes = {'BaseModel': BaseModel, 'User': User,
           'Amenity': Amenity, 'City': City, 'State': State,
           'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    command interpreter should implement:
    quit and EOF to exit the program
    help (this action is provided by default by cmd but
    you should keep it updated and documented as you work through tasks)
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
            print("** class name missing **")
            return False
        if args_list[0] not in classes.keys():
            print("** class doesn't exist **")
            return False
        else:
            new_instance = classes[args_list[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in classes:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file)
        """
        args_list = args.split()
        if len(args_list) < 1:
            print("** class name missing **")
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

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        args_list = args.split()
        obj = storage.all()
        if len(args_list) < 1:
            print(["{}".format(str(v)) for _, v in obj.items()])
            return
        if args_list[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in obj.items() if type(v).__name__ == args_list[0]])
            return

    def do_update(self, args):
        """
        update <class name> <id> <attribute name> "<attribute value>"
        """
        args_list = args.split(maxsplit=3)
        if len(args_list) < 1:
            print("** class name missing **")
            return
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        instance_objs = storage.all()
        key = "{}.{}".format(args_list[0], args_list[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args_list[2]
        if len(args_list) < 4:
            print("** value missing **")
            return
        attribute_value = args_list[3]
        if attribute_name in ["id", "created_at", "updated_at"]:
            return
        try:
            if isinstance(attribute_value, int):
                attribute_value = int(attribute_value)
            elif isinstance(attribute_value, float):
                attribute_value = float(attribute_value)
        except (ValueError, TypeError):
            print("** invalid value type for the attribute **")
            return
        setattr(req_instance, attribute_name, attribute_value)
        storage.save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exits the shell when Ctrl+D is pressed"""
        return True
    
    def emptyline(self):
        """Override default `empty line + return` behaviour.
        """
        pass
    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

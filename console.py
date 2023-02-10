#!/usr/bin python3
"""Contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand defines the command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, args):
        """create command creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if args:
            if args == "BaseModel":
                base_model = BaseModel()
                file_storage = FileStorage()
                file_storage.new(base_model)
                file_storage.save()
                print(base_model.id)
            elif args not in ('BaseModel', 'FileStorage'):
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show command prints the string representation of an instance based on the class name and id."""
        argv = args.split(' ')
        if argv:
            if argv[0] == 'BaseModel':
                if len(argv) == 1:
                    print("** instance id missing **")
                elif "{}.{}".format(argv[0], argv[1]) not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()["{}.{}".format(argv[0], argv[1])])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """destroy command deletes an instance based on the class name and id."""
        argv = args.split(" ")
        if argv:
            if argv[0] in __class__.classes:
                if len(argv) == 1:
                    print("** instance id missing **")
                elif "{}.{}".format(argv[0], argv[1]) not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()["{}.{}".format(argv[0], argv[1])]
                    storage.save()

            elif argv[0] not in __class__.classes:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """all command prints all string representation of all instances based or not on the class name."""
        argv = args.split(" ")
        if argv[0] not in __class__.classes:
            print("** class doesn't exits **")
        # elif argv[0] in __class__.classes:


    def emptyline(self):
        """override emptyline method when an empty line + ENTER shouldn't execute anything"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program: quit"""
        return True

    def do_EOF(self, args):
        """EOF command to exit program: EOF"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin python3
"""Contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand defines the command interpreter"""

    prompt = "(hbnb) "

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

    # def do_show(self, args):
    #     """show command prints the string representation of an instance based on the class name and id."""
    #     argv = args.split(' ')
    #     if argv[0]:
    #         if argv[0] == 'BaseModel':
    #             for arg in argv:
    #     else:
    #         print("** class name missing **")
            


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

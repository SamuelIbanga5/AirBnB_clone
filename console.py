#!/usr/bin python3
"""Contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand defines the command interpreter"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_create(self, args):
        """create command creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if args:
            if args in __class__.classes:
                model_instance = HBNBCommand.classes[args]()
                storage.save()
                print(model_instance.id)
            elif args not in __class__.classes:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show command prints the string representation
        of an instance based on the class name and id.
        """
        argv = args.split(' ')
        if argv[0] == '':
            argv.remove('')
        if argv:
            if argv[0] in __class__.classes:
                if len(argv) == 1:
                    print("** instance id missing **")
                elif "{}.{}".format(argv[0], argv[1]) not in storage.all():
                    print(storage.all())
                    print("** no instance found **")
                else:
                    print(storage.all()["{}.{}".format(argv[0], argv[1])])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """destroy command deletes an instance
        based on the class name and id.
        """
        argv = args.split(" ")
        if argv[0] == '':
            argv.remove('')
        if argv:
            if argv[0] in __class__.classes:
                if len(argv) == 1:
                    print("** instance id missing **")
                elif "{}.{}".format(argv[0], argv[1])\
                     not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()["{}.{}".format(argv[0], argv[1])]
                    storage.save()

            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """all command prints all string representation of all instances based or not on the class name."""
        argv = args.split(" ")
        model_list = []
        if argv[0] == '':
            argv.remove('')
        if argv:
            if argv[0] not in __class__.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if value.to_dict()['__class__'] == argv[0]:
                        model_list.append(str(value))
                print(model_list)

    def do_update(self, args):
        """update command updates an instance based on the class name and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        argv = args.split(" ")
        if argv[0] == '':
            argv.remove('')
        if len(argv) == 0:
            print("** class name missing **")
        if argv[0] not in __class__.classes:
            print("** class doesn't exist **")
        if len(argv) == 1:
            print("** instance id missing **")
        if len(argv) == 2:
            print("** attribute name missing **")
        if "{}.{}".format(argv[0], argv[1]) not in storage.all().keys():
            print("** no instance found **")
        if len(argv) == 3:
            try:
                type(eval(argv[2])) != dict
            except NameError:
                print("** value missing **")
        if len(argv) == 4:
            obj = storage.all()[f"{argv[0]}.{argv[1]}"]
            if argv[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[argv[2]])
                obj.__class__.__dict__[argv[2]] = value_type(argv[3])
            else:
                obj.__class__.__dict__ = argv[3]
        else:
            obj = storage.all()[f"{argv[0]}.{argv[1]}"]
            for key, value in eval(argv[2]).items():
                if (key in obj.__class__.__dict__.keys() and type(obj.__class__.__dict__[key]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

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

#!/usr/bin python3
"""Contains the entry point of the command interpreter"""


import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

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

    def default(self, line):
        """Parse and interpretates a line if not found on regular commands"""
        count = 0
        splitline = line.split('.', 1)
        if len(splitline) >= 2:
            line = splitline[1].split('(')
            """ Execute <class name>.all()"""
            if line[0] == 'all':
                self.do_all(splitline[0])
                """Execute <class name>.count() """
            elif line[0] == 'count':
                for key in storage.all():
                    if splitline[0] == key.split(".")[0]:
                        count += 1
                print(count)
                """Execute <class name>.show(<id>) """
            elif line[0] == 'show':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_show(str_id)
                """Execute <class name>.destroy(<id>)"""
            elif line[0] == 'destroy':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_destroy(str_id)
                """Execute <class name>.update(<id>"""
            elif line[0] == 'update':
                update = line[1].split(')')
                split = update[0].split('{')
                if len(split) == 1:
                    line = update[0].split(",")
                    str_id = str(splitline[0]) + " " + str(line[0]) + \
                        " " + str(line[1]) + " " + str(line[2])
                    self.do_update(str_id)
                else:
                    id = split[0][:-2]
                    str_dict = split[1][:-1]
                    delim = str_dict.split(',')
                    for row in delim:
                        key_value = row.split(':')
                        str_id = str(splitline[0]) + " " + str(id) + \
                            " " + str(key_value[0]) + " " + str(key_value[1])
                        self.do_update(str_id)

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
        """all command prints all string representation of all instances
        based or not on the class name."""
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

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, cls_name):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def emptyline(self):
        """override emptyline method when an empty line + ENTER
        shouldn't execute anything"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit program."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

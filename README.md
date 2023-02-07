# AirBnB Clone

![Airbnb image](airbnb.png)

## Description
AirBnB is a complete web application integrated using HTML/CSS templating, database storage, API, frontend integration, backend integration and server deployment.

This is part 1 of our AirBnB clone project centered on creating a console or command interpreter.

## Concepts learnt: 
1. How to create a python package
2. How to create a command interpreter in python usinf the `cmd` module
3. What is Unit testin and how to implement it in a large project
4. Hw to serialize and deserialize a Class
5. How to manage datetime
6. How to manage `datetime`
7. What is an `UUID`
8. What is `*args` and how to use it
9. What is `**kwargs` and how to use it
10. How to handle named arguments in a function

## Data Diagram
![Data Diagram](data_diagram.jpg)

## The Command Interpreter
The command interpreter is exactly the same as a shell but limited to specific use-case. In this interpreter, we want to be ale to manage the objects of our project by creating a new object(ex: a new USer or new Place), retrieve an object from a file or database, do operations on objects (count, compute stats, etc), update attributes of an object and destroy an object.

### Starting the command interpreter
The command line interpreter can be started by executing the command `./console.py`. The `console` can `create`, `read`, `update` and `delete` objects (basic `CRUD` operations).

### How to use it
Type `help` within the console to get a list of all commands to be used. Type `help <command>` to get full description of a partcular command and how to use it.

### Example:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF create help quit

Undocumented commands:
======================
all destroy show update

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
$

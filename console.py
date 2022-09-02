#!/usr/bin/python3
'''Contains the definition of the 'HBNBCommand' class which is
to serve as the console for the HBNB project.'''


import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_names = ('BaseModel', )

    def emptyline(self):
        '''Is called when an empty line is passed to the console.
        '''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''Exits when CTRL+D on the keyboard is pressed
        '''
        return True

    def do_create(self, line):
        '''Creates a new instance of a specified class.
        '''
        args = line.split()
        if len(args) != 1:
            print("** class name missing **")
        else:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                obj = eval(class_name)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''Prints the string representation of an instance with the exact id
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                    search_id = args[1].strip()
                    search_key = "{}.{}".format(class_name, search_id)
                    storage.reload()
                    obj_dict = storage.all()
                    if search_key in obj_dict.keys():
                        obj = obj_dict[search_key]
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id
        '''
        args = line.split()
        if len(args) >= 1:
            class_name = args[0].strip()
            if class_name in HBNBCommand.class_names:
                if len(args) == 2:
                    search_id = args[1].strip()
                    search_key = "{}.{}".format(class_name, search_id)
                    storage.reload()
                    obj_dict = storage.all()
                    if search_key in obj_dict.keys():
                        del obj_dict[search_key]
                        # Overwrite the JSON file with the present contents of
                        # obj_dict dictionary.
                        temp_dict = {}
                        file_name = storage.file_path
                        for key in obj_dict.keys():
                            obj = obj_dict[key]
                            temp_dict[key] = obj.to_dict()
                        with open(file_name, 'w', encoding='utf-8') as fp:
                            json.dump(temp_dict, fp)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        '''Prints the string form of all instances of the specified class name
        '''
        if line in HBNBCommand.class_names or line == "":
            obj_dict = storage.all()
            if line:
                obj_list = [str(item) for item in obj_dict.values()
                            if item.__class__.__name__ == line]
            else:
                obj_list = [str(item) for item in obj_dict.values()]
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''Updates an instance based on a class name and id.
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

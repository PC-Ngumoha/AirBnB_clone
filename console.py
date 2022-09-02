#!/usr/bin/python3
'''Contains the definition of the 'HBNBCommand' class which is
to serve as the console for the HBNB project.'''
from cmd import Cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(Cmd):
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
        pass

    def do_show(self, line):
        '''Prints the string representation of an instance with the exact id
        '''
        pass

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id
        '''
        pass

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

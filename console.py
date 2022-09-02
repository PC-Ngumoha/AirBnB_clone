#!/usr/bin/python3
'''Contains the definition of the 'HBNBCommand' class which is
to serve as the console for the HBNB project.'''
from cmd import Cmd


class HBNBCommand(Cmd):
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

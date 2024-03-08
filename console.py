#!/usr/bin/python3
'''This module create a console.'''
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''Objec inherits from cmd.Cmd class.'''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quite command to exit the program.'''

        return True

    def do_create(self, line):
        print("created")

    def do_show(self, line):
        print("haha")

    def do_EOF(self, line):
        '''Method exits the console.'''

        return True

    def def_help(self, line):
        '''Method displays information on how to use the console.'''

        print("nothing for now")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3
'''This module create a console.'''
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
import json


class HBNBCommand(cmd.Cmd):
    '''Objec inherits from cmd.Cmd class.'''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quite command to exit the program.'''

        return True

    def do_create(self, line):
        '''Create command create new nstance if BaseModel.'''

        if line:
            parts = line.split(" ")
            class_name = parts[0]
            try:
                globals()[class_name]
                if class_name == "BaseModel":
                    new_instance = BaseModel()
                if class_name == "User":
                    new_instance = User()
                    print("hello")
                print(new_instance.id)
                storage.save()
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        '''Show command prints string representation based on class name and id.'''

        if line:
            parts = line.split(" ")
            class_name = parts[0]
            try:
                globals()[class_name]
                if len(parts) > 1:
                    class_id = parts[1]
                    key = class_name + "." + class_id
                    data_base = storage.reload()
                    if key in data_base:
                        instance = BaseModel(**data_base[key])
                        print(instance.__str__())
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_destroy(self, line):
        '''Destroy command deletes a class instance based on class name and id.'''

        if line:
            parts = line.split(" ")
            class_name = parts[0]
            try:
                globals()[class_name]
                if len(parts) > 1:
                    class_id = parts[1]
                    key = class_name + "." + class_id
                    data_base = storage.reload()
                    if key in data_base:
                        del(data_base[key])
                        with open("file.json", 'w') as f:
                            f.write(json.dumps(data_base))
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError():
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        '''All command prints string prepresentation of all class instances.'''

        if line:
            parts = line.split(" ")
            class_name = parts[0]
            try:
                globals()[class_name]
                all_instances = storage.reload()
                list_representation = []
                for key in all_instances.keys():
                    if class_name in key:
                        recreate = BaseModel(**all_instances[key])
                        list_representation.append(recreate.__str__())
                    else:
                        continue
                print(list_representation)
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, line):
        '''Update command updates an instance based of class name and id.'''

        if line:
            parts = line.split(" ")
            class_name = parts[0]
            try:
                globals()[class_name]
                if len(parts) > 1:
                    class_id = parts[1]
                    key = class_name + "." + class_id
                    data_base = storage.reload()
                    if key in data_base:
                        if len(parts) > 2:
                            attribute = parts[2]
                            if len(parts) > 3:
                                attribute_value = parts[3]

                                instance_dict = data_base[key]
                                instance_dict[attribute] = attribute_value

                                instance = BaseModel(**instance_dict)
                                data_base[key] = instance.__dict__
                                with open("file.json", 'w') as f:
                                    f.write(json.dumps(data_base, default=str))
                            else:
                                print("** vale missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        '''Method exits the console.'''

        return True

    def def_help(self, line):
        '''Method displays information on how to use the console.'''

        print("nothing for now")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

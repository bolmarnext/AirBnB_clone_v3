import os
import cmd
from models import base_model, user, storage, CNC

BaseModel = base_model.BaseModel
User = user.User


class HBNBCommand(cmd.Cmd):
    """
        Command inerpreter class
    """
    prompt = '(hbnb) '
    ERR = [
        '** class name missing **',
        '** class doesn\'t exist **',
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
        ]

    def preloop(self):
        """
            handles intro to command interpreter
        """
        print('.----------------------------.')
        print('|    Welcome to hbnb CLI!    |')
        print('|   for help, input \'help\'   |')
        print('|   for quit, input \'quit\'   |')
        print('.----------------------------.')

    def postloop(self):
        """
            handles exit to command interpreter
        """
        print('.----------------------------.')
        print('|  Well, that sure was fun!  |')
        print('.----------------------------.')

    def default(self, line):
        """
            default response for unknown commands
        """
        pass

    def emptyline(self):
        """
            Called when an empty line is entered in response to the prompt.
        """
        pass

    def __class_err(self, arg):
        """
            private: checks for missing class or unknown class
        """
        error = 0
        if len(arg) == 0:
            print(HBNBCommand.ERR[0])
            error = 1

"""
-- INSERT --
-- INSERT --
-- INSERT --     

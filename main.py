#!/usr/bin/python3

import os
import argparse
from commands import Commands
import traceback
from config import *

folder = ""
root = TODO_STORE_DIR + "/"

#--parser conf
parser = argparse.ArgumentParser(prog = 'todo-tracker',
        description='Stores your work in a manageble list')

parser.add_argument('--store',
        '--dmb',
        nargs = '+',
        action = 'store',
        help = 'Stores an entry',
        )

parser.add_argument('--delete',
        action = 'store',
        type = int,
        help = 'Deletes an entry wrt its index'
        )

parser.add_argument('--show',
        action = 'store_true',
        help = 'Shows Entries'
        )

parser.add_argument('--purge',
        action = 'store_true',
        help = 'Deletes all entries'
        )

#--


#main function which reads the inputted commands
def run(command):
    if(command=="\\"):
        return 0
    
    args = command.split()

    command_handler = Commands(root, args[1:])
    commands = command_handler.get_dict()

    try:
        return commands[args[0]]()
    except KeyError:
        print("This command doesnt exist, try these : \n"+"\n".join(commands.keys()))
        return 1;



root+='debug'
if folder == 'todo':
    is_todo = 1
if not os.path.exists(root):
    os.makedirs(root)



args, leftovers = parser.parse_known_args()
command = ''
data = ''
if args.store is not None:
    command = 'store'
    data = " ".join(args.store)

elif args.delete is not None:
    command = 'delete'
    data = args.delete

elif args.purge:
    command = 'purge'

elif args.show:
    command = 'show'

print("%s %s"%(command, data))
run("%s %s"%(command, data))

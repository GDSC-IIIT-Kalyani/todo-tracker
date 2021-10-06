#!/usr/bin/python3

import os
from commands import Commands


folder = ""
root = os.environ['TODO_STORE_DIR']+"/"

#main function which reads the inputted commands
def run(command):
    if(command=="\\"):
        return 0
    
    args = command.split()

    print(root)
    command_handler = Commands(root, args[1:])
    commands = command_handler.get_dict()

    try:
        return commands[args[0]]()
    except KeyError:
        print("This command doesnt exist, try these : \n"+"\n".join(commands.keys()))
        return 1;

root+='todo'

if folder == 'todo':
    is_todo = 1

if not os.path.exists(root):
    os.makedirs(root)

while(True):
    command = input("#")
    if run(command)==0 :
        break

input("Press enter to continue...")

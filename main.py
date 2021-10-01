#!/usr/bin/python3

import os
from commands import Commands


folder = ""
root = "/home/tatan/.todo_tracker/"

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

print("Already existsing folders : \n"+"\n".join(os.listdir(root)))
folder = input("Folder : ")
root+=folder

if folder == 'todo':
    is_todo = 1

ans = "y"
if not os.path.exists(root):
    ans = input("This folder does not exist, are you sure you want to create a new folder?(y/n) : ")
    if(ans == "y"):
        os.makedirs(root)

while(True and ans == "y"):
    command = input("#")
    if run(command)==0 :
        break

input("Press enter to continue...")

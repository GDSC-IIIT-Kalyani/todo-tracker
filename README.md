# CUI program to easily add and schedule tasks on the go

This is some python code which is linked with a bash script which can be executed by just using a keystroke.

## **Requirements** :-
- Python 3.\*
- Ubuntu/Windows

## Setting up

- Please tell me you have an Operating System Installed
- Install Python from [Python](https://www.python.org)

## Instructions - For all

Run the code with `python main.py --command` where c`--command` is one of the available commands.
`python main.py -h` will show the list of available commands. 

## Instructions - For Windows

1. Go to the git-bash or command prompt.
2. Run the following command at the root directory of this application `./install.sh`.
3. Two new files called `open_terminal` and `config.py` will be generated.
4. Then run command `cmd "\C run_todo.bat"`. Now you can use todo-tracker.
5. To create keyboard bindings. Right click on batch_file.bat file Then click on create shortcut.
6. After shortcut created. Then Go to properties you can see shortcut keys. you can use like `alt + ctrl + n`. keyboard shortcut is created.

## Instructions - For Linux

1. Make install.sh executable with `chmod +x`<br>
Run the following line in the terminal of the root directory of install <br>
`chmod +x install.sh`
2. Run `./install.sh`
3. Two new files called `open_terminal` and `config.py` will be generated. Note the path of open_terminal.sh
4. Go to Settings > Keyboard Bindings
5. Add a new binding of you choice. I use `Alt+\` and put the path of the executable like `path/to/folder/./open_terminal.sh` . This will run the code when you press that binding


When the window opens, you have to write the commands as `<command> <arg1> <arg2>...`
Currently available commands are 

1. store
2. delete
3. purge
4. show

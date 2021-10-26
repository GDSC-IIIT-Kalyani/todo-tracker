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

For windows a batch file is needed, which has not yet been implemented. Please check Issues if you want to work on it.

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

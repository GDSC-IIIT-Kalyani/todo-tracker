# CUI program to easily add and schedule tasks on the go

This is some python code which is linked with a bash script which can be executed by just using a keystroke.

## **Requirements** :-
- Python 3.\*
- Ubuntu/Windows

## Setting up

- Please tell me you have an Operating System Installed
- Install Python from [Python](https://www.python.org)

## Instructions - For all

Run the code with `python main.py`.

## Instructions - For Windows

For windows a batch file is needed, which has not yet been implemented. Please check Issues if you want to work on it.

## Instructions - For Linux

1. Make run.sh executable with `chmod +x`<br>
Run the following line in the terminal of the root directory of install <br>
`chmod +x run.sh`
2. Go to Settings > Keyboard Bindings
3. Add a new binding of you choice. I use `Alt+/` and put the path of the executable like `path/to/folder/./run.sh` . This will run the code when you press that binding

When the window opens, you have to write the commands as `<command> <arg1> <arg2>...`
Currently available commands are 

1. store
2. delete
3. purge
4. show

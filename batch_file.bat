@echo off

:while
echo. 
echo Currently available commands in todo-tracker :
echo 1. store
echo 2. delete
echo 3. purge
echo 4. show
echo 5. quit


set /p command=Enter the command you want to use : 

if "%command%" == "quit" exit

python main.py --%command%

goto :while  

pause
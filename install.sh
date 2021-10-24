CURRDIR=$(pwd)
echo $CURRDIR

if [ ! -f "config.py" ]
then
    touch config.py
fi

if grep -Fxq "TODO_DIR='${CURRDIR}'" ./config.py
then
    echo "Env variable found"
else
    echo "Adding env variable to bash file"
    rm config.py
    touch config.py
    echo "TODO_DIR='${CURRDIR}'" >> ./config.py
fi

if grep -Fxq "TODO_STORE_DIR='/home/$(whoami)/.todo_tracker'" ./config.py
then
    echo "Env variable found"
else
    echo "Adding env variable to bash file"
    echo "TODO_STORE_DIR='/home/$(whoami)/.todo_tracker'" >> ./config.py
fi

echo "x-terminal-emulator --working-directory=$CURRDIR --geometry=50x20 -e 'bash -c \"./run.sh\"'" > open_terminal.sh
chmod +x open_terminal.sh
chmod +x run.sh

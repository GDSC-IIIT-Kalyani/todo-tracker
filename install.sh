CURRDIR=$(pwd)
echo $CURRDIR

if grep -Fxq "export TODO_DIR=${CURRDIR}" ~/.bashrc 
then
    echo "Env variable found"    
else
    echo "Adding env variable to bash file"
    echo "export TODO_DIR=${CURRDIR}" >> ~/.bashrc
fi

if grep -Fxq "export TODO_STORE_DIR=/home/$(whoami)/.todo_tracker" ~/.bashrc 
then
    echo "Env variable found"    
else
    echo "Adding env variable to bash file"
    echo "export TODO_STORE_DIR=/home/$(whoami)/.todo_tracker" >> ~/.bashrc
fi

echo "gnome-terminal --geometry=20x20 -- ${CURRDIR}/main.py" > run.sh
chmod +x run.sh

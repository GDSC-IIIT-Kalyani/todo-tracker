while IFS="" read -r -e -d $'\n' -p '>> ' line; do 
    if [ "$line" == "quit" -o "$line" == "\\" ]; then
        echo Exiting gracefully
        exit
    fi
    eval python3 main.py "--$line"
    history -s "$line"
done


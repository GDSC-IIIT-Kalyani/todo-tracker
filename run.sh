while IFS="" read -r -e -d $'\n' -p '>> ' line; do 
   eval python main.py "--$line"
   history -s "$line"
done


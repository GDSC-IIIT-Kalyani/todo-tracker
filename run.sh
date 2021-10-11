while IFS="" read -r -e -d $'\n' -p '>> ' line; do 
   ./main.py 
   history -s "$line"
done


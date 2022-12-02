#Funciona bien pero funcionaria mejor eliminando la aleatoriedad y usando una lista de palabras ordenada por frecuencia de uso. (lineas 9 y 98 del programa en caso de querer mejorarlo)
#Modulos que requieren instalacion mediante pip: pyautogui, Pillow (PIL)
#La lista de palabras fue descargada desde 'https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/0_palabras_todas.txt'
#Primero se eliminan las palabras con tildes usando el script llamado 'eliminar_elementos_con_acentos', ubicado en el directorio del proyecto
#Si hay algun error de codec con la ñ se puede buscar y reemplazar el caracter corrupto con la ñ en VSCODE o algun editor de texto similar (incluyendo el editor de texto por defecto de Windows)
#Posteriormente se agregan comillas al inicio de cada linea, y comillas con comas al final. Todo esto para eliminar los saltos de linea y tener todas las palabras en una linea. Para esto se puede usar el siguiente comando en bash/zsh: sed '$!s/^/"/' palabras.txt | sed '$!s/$/",/' | tr '\n' ' ' > t.txt
#Todas las palabras deben estar en mayuscula, para eso se puede usar esta herramienta: 'https://convertcase.net/'
#Se copian todas las lineas del archivo t.txt (CTRL + A, CTRL + C) y se pegan como un array en python.
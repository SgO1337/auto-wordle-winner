acentos = ['á','é','í','ó','ú']
palabras = [] #En este array van las palabras.
for item in palabras.copy():
    res = [ele for ele in acentos if(ele in item)]
    if res:
        palabras.remove(item)
#Esto crea un archivo llamado 'p.txt' en el directorio donde se ejecuta el programa, conteniendo la lista de palabras. 
with open('p.txt', 'w') as filehandle:
    for listitem in palabras:
        filehandle.write('%s\n' % listitem)
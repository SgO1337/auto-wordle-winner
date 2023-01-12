# ideas (ignorar): 
# - mejorar el algoritmo de eleccion de palabras basandolo en probabilidad (letras comunes) y no en aleatoriedad
import pyautogui
import time
from PIL import ImageGrab
import random
from palabras import espanol as palabras
letrasPermitidas = []
def conseguirColor(x, y, letra, pos):
    im = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    hex = ('{:X}{:X}{:X}').format(r, g, b)
    if(hex == 'E4A81D'):
        #amarillo, posible
        letrasAmarillas(letra, pos)
    elif(hex == '757575'):
        #gris, imposible
        letrasGrises(letra)
    elif(hex == '43A047'):
        #verde, segura y fixeada en la posicion
        #letrasVerdes(letra, pos)
        letrasVerdes(letra, pos)
    else:
        return 'Error de coordenadas (blanco)'
def enviarMensaje():
    #Los tiempos varian de computadora en computadora, tambien dependen de la velocidad de internet
    pyautogui.click(1050, 600)
    time.sleep(5)
    pyautogui.write('chanchis') #se debe reemplazar chanchis por el nombre del contacto
    time.sleep(1)
    pyautogui.click(1050, 675)
    time.sleep(1)
    pyautogui.click(1175, 335)
    time.sleep(1)
    pyautogui.click(1100, 885)
    time.sleep(1)
    pyautogui.press('enter')
def ingresarPalabra(palabra):
    letras_a_ingresar = separarPalabra(palabra)
    for i in letras_a_ingresar:
        coordenadas = abecedario.index(i)
        pyautogui.click(coordenadasLetrasX[coordenadas], coordenadasLetrasY[coordenadas])
        time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('backspace', presses=5)
    time.sleep(0.5)
    for item in palabras.copy():
        if item == palabra:
            palabras.remove(item)
    return letras_a_ingresar
def letrasAmarillas(letra, pos):
    letrasPermitidas.append(letra)
    #print('letra amarilla: '+letra)
    for item in palabras.copy():
        if letra not in item:
            palabras.remove(item)
    for item in palabras.copy():
        if item[pos] == letra:
            palabras.remove(item)
def letrasVerdes(letra, pos):
    letrasPermitidas.append(letra)
    for item in palabras.copy():
        if item[pos] != letra:
            palabras.remove(item)
def letrasGrises(letra):
    #print('letra gris: '+letra)
    for item in palabras.copy():
        if letra in item and letra not in letrasPermitidas:
            palabras.remove(item)
    for item in letrasPermitidas.copy():
        if letrasPermitidas == letra:
            letrasPermitidas.remove(item)
def separarPalabra(palabra):
    letras = list(palabra)
    return letras
def jugar(iteracion, palabra):
    ingresarPalabra(palabra)
    letras = separarPalabra(palabra)
    for i in range(0, 5):
        conseguirColor(coordenadasXcolores[i], coordenadasYcolores[iteracion], letras[i], i)
def elegirIdioma(idioma):
    global coordenadasXcolores, coordenadasYcolores, coordenadasLetrasX, coordenadasLetrasY, abecedario
    #1 = espanol, 2 = ingles
    #el ingles es WIP
    if(idioma == 1):
        #Todas las coordenadas estan definidas para un monitor 1920x1080 en modo ventana maximizada
        #Defino las coordenadas de las letras ingresadas para saber los colores de las letras
        coordenadasXcolores = [797, 872, 947, 1022, 1117]
        coordenadasYcolores = [245, 320, 395, 470, 555, 590]
        #Defino las coordenadas de las letras de la A a la Z contando la ñ (0, 26)
        coordenadasLetrasX = [725, 775, 825, 875, 925, 975, 1025, 1075, 1140, 1200, 725, 775, 825, 875, 925, 975, 1025, 1075, 1140, 1200, 820, 870, 920, 970, 1020, 1070, 1120]
        coordenadasLetrasY = [759, 759, 759, 759, 759, 759, 759, 759, 759, 759, 824, 824, 824, 824, 824, 824, 824, 824, 824, 824, 888, 888, 888, 888, 888, 888, 888]
        #Abecedario (para encontrar coordenadas con el index)
        abecedario = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    elif(idioma == 2):
        #Todas las coordenadas estan definidas para un monitor 1920x1080 en modo ventana maximizada
        #Defino las coordenadas de las letras ingresadas para saber los colores de las letras
        coordenadasXcolores = [797, 872, 947, 1022, 1117]
        coordenadasYcolores = [245, 320, 395, 470, 555, 590]
        #Defino las coordenadas de las letras de la A a la Z contando la ñ (0, 26)
        coordenadasLetrasX = [725, 775, 825, 875, 925, 975, 1025, 1075, 1140, 1200, 725, 775, 825, 875, 925, 975, 1025, 1075, 1140, 1200, 820, 870, 920, 970, 1020, 1070, 1120]
        coordenadasLetrasY = [759, 759, 759, 759, 759, 759, 759, 759, 759, 759, 824, 824, 824, 824, 824, 824, 824, 824, 824, 824, 888, 888, 888, 888, 888, 888, 888]
        #Abecedario (para encontrar coordenadas con el index)
        abecedario = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
def juegoInicial(idioma):
    elegirIdioma(idioma)
    for iteracion in range(0, 6):
        if(len(palabras) == 0):
            return 0
        print('Numero de palabras posibles: '+str(len(palabras)))
        palabra = random.choice(palabras)
        #print(palabras)
        print('palabra nueva: '+palabra)
        if(iteracion == 0):
            jugar(iteracion, 'AUDIO')
        else:
            jugar(iteracion, palabra)
juegoInicial(1)
#time.sleep(2)
#enviarMensaje()
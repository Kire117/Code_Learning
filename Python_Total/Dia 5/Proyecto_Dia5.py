from random import *
palabras = ['python',
            'java',
            'javascript',
            'ruby',
            'krypton']

letras_correctas = []
letras_incorrectas = []
vidas = 6
aciertos = 0
juego_terminado = False
def ask_user():
    letter = ''
    is_valid = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not is_valid:
        letter = input("Please write a letter(not numbers or more than 1 letter): ").lower()
        if letter in abecedario and len(letter) == 1:
            is_valid = True
        else:
            print("No has elegido una letra correcta")
    return letter
def chosen_word(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado esa letra, intenta con otra diferente")
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra era " + palabra)
    return True
def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades, has encontrado la palabra!")
    return True

palabra, letras_unicas = chosen_word(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f"Vidas: {vidas}")
    print('\n' + '*' * 20 + '\n')
    letra = ask_user()

    vidas, terminado, aciertos = chequear_letra(letra, palabra,vidas,aciertos)

    juego_terminado = terminado


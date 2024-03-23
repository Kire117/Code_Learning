import os
from os import system
from pathlib import *

path = Path("C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\PDF's\\Recetas")

def contar_recetas(path):
    contador = 0
    for txt in Path(path).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system('cls')
    print("*"*50)
    print('*' * 5 + "Bienvenido al administrador de recetas" + '*' * 5)
    print("*"*50)
    print('\n')
    print(f"Las recetas se encuentran en {path}")
    print(f"Total recetas: {contar_recetas(path)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print("\n[1]Leer receta"
              "\n[2]Crear receta"
              "\n[3]Crear categoria"
              "\n[4]Eliminar receta"
              "\n[5]Eliminar categoria"
              "\n[6]Finalizar programa")
        eleccion_menu = input()
    return eleccion_menu



inicio()

menu = 0
if menu == 1:
    leer_receta()
    pass
elif menu == 2:
    crear_receta()
    pass
elif menu == 3:
    crear_categoria()
    pass
elif menu == 4:
    eliminar_receta()
    pass
elif menu == 5:
    eliminar_categoria()
    pass
elif menu == 6:
    finalizar_programa()
    pass
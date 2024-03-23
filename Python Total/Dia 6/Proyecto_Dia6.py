import os
from os import system
from pathlib import *
import time

print("Hello user!")
carpeta = Path("C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\PDF's\\Recetas")
ruta_windows = PureWindowsPath(carpeta)
print("Tus recetas son:")
for txt in Path(carpeta).glob("**/*.txt"):
    print(txt.name)

print(f"Tu ruta del folder es: {ruta_windows}")

'''menu = 0

def contar_recetas(path):
    contador = 0
    for txt in Path(carpeta).glob("**/*.txt"):
        contador += 1'''


def show_menu():
    """
    opc = int(input("\n-----Menu-----"
                    "\n[1]Leer receta"
                    "\n[2]Crear receta"
                    "\n[3]Crear categoria"
                    "\n[4]Eliminar receta"
                    "\n[5]Eliminar categoria"
                    "\n[6]Finalizar programa"
                    "\nChoose an option: "))
    return opc
    """
    print('\n')
    print("\n-----Menu-----"
          "\n[1]Leer receta"
          "\n[2]Crear receta"
          "\n[3]Crear categoria"
          "\n[4]Eliminar receta"
          "\n[5]Eliminar categoria"
          "\n[6]Finalizar programa")


def leer_receta():
    global directory
    global guia
    print("Las categorias son: ")
    for directory in os.listdir(carpeta):
        print(directory)
    user_input = input("Por favor, escoge una categoria: ").lower()
    guia = Path(carpeta, user_input)

    print(f"Cual receta de la categoria {user_input}, deseas leer? ")
    for file in Path(guia).glob('*.txt'):
        print(file.stem.lower())
    user_input = input("Respuesta: ").lower()
    guia1 = Path(guia, user_input + '.txt')
    leer_archivos(guia1)
    time.sleep(5)
    limpiar_pantalla()


def leer_archivos(path):
    archivo = open(path)
    print(archivo.read())
    archivo.close()


def crear_archivo(path):
    archivo = open(path, 'w')
    user_input = input("Por favor dale un contenido: ")
    archivo.write(user_input)
    print("Receta creada exitosamente")
    archivo.close()


def crear_receta():
    print("Las categorias son: ")
    for directory in os.listdir(carpeta):
        print(directory)
    user_input = input("Por favor, escoge una categoria: ").lower()
    guia = Path(carpeta, user_input)

    user_input = input("Por favor dale un nombre a tu receta: ")
    guia1 = Path(guia, user_input + '.txt')
    crear_archivo(guia1)
    limpiar_pantalla()

def crear_categoria():
    print("Las categorias son: ")
    for directory in os.listdir(carpeta):
        print(directory)

    user_input = input("Por favor dale un nombre a la categoria: ")
    os.chdir(carpeta)
    os.makedirs(user_input)
    print("Genial, Has creado una nueva categoria")
    time.sleep(5)
    limpiar_pantalla()


def eliminar_receta():
    print("Las categorias son: ")
    for directory in os.listdir(carpeta):
        print(directory)
    user_input = input("Por favor, escoge una categoria: ").lower()
    guia = Path(carpeta, user_input)

    limpiar_pantalla()
    print(f"Cual receta de la categoria {user_input}, deseas eliminar? ")
    for file in Path(guia).glob('*.txt'):
        print(file.stem.lower())
    user_input = input("Respuesta: ").lower()
    guia1 = Path(guia, user_input + '.txt')
    if guia1.exists():
        os.remove(guia1)
        print("Esta receta ha sido eliminada")
    else:
        print("Esta receta no existe")
    time.sleep(5)
    limpiar_pantalla()


def eliminar_categoria():
    print("Las categorias son: ")
    for directory in os.listdir(carpeta):
        print(directory)
    user_input = input("Que categoria deseas eliminar?: ")
    guia = Path(carpeta, user_input)
    if guia.exists():
        os.rmdir(guia)
        print("Esta categoria ha sida eliminada")
    else:
        print("No existe esta categoria")
    time.sleep(5)
    limpiar_pantalla()

def limpiar_pantalla():
    system('cls')


def finalizar_programa():
    print("Gracias por usar el menu!")
    exit()


'''if menu == 1:
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
    pass'''

question = input("Would you like to display the menu?(Y/N): ").lower()

while question == 'yes' or question == 'y':
    show_menu()
    option = int(input("Choose an option: "))

    match option:
        case 1:
            leer_receta()

        case 2:
            crear_receta()

        case 3:
            crear_categoria()

        case 4:
            eliminar_receta()

        case 5:
            eliminar_categoria()

        case 6:
            finalizar_programa()
else:
    print("Pls select the given options")

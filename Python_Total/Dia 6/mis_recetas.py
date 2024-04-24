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
    print("*" * 50)
    print('*' * 5 + "Bienvenido al administrador de recetas" + '*' * 5)
    print("*" * 50)
    print('\n')
    print(f"Las recetas se encuentran en {path}")
    print(f"Total recetas: {contar_recetas(path)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opcion:")
        print("\n[1]Leer receta"
              "\n[2]Crear receta"
              "\n[3]Crear categoria"
              "\n[4]Eliminar receta"
              "\n[5]Eliminar categoria"
              "\n[6]Finalizar programa")
        eleccion_menu = input()
    return int(eleccion_menu)


def mostrar_categorias(path):
    print("Categorias:")
    ruta_categorias = Path(path)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_categorias(lista):
    eleccion_correcta = 'X'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElije una categoria: ')
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(path):
    print("Recetas:")
    ruta_recetas = Path(path)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_receta(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\n Elije una receta: ')
    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(path):
    existe = False

    while not existe:
        print("Escribre el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta")
        contenido_receta = input()
        ruta_nueva = Path(path, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_categoria(path):
    existe = False

    while not existe:
        print("Escribre el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(path, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esta categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresiove V para volver al menu: ')

finalizar_programa = False
while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(path)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(path)
        mi_categoria = elegir_categorias(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(path)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(path)
        mi_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(path)
        mi_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6:
        finalizar_programa = True
        print("Gracias por usar el menu!")

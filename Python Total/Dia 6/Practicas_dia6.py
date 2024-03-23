""" Práctica Abrir y Manipular Archivos 1
Abre el archivo texto.txt e imprime su contenido.
Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código"""
mi_archivo = open('texto.txt')
print(mi_archivo.read())
''' Práctica Abrir y Manipular Archivos 2
Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código'''

mi_archivo = open('texto.txt')
print(mi_archivo.readline())
mi_archivo.close()

''' Práctica Abrir y Manipular Archivos 3
Abre el archivo texto.txt e imprime únicamente la segunda línea.'''
mi_archivo = open('texto.txt')
todas = mi_archivo.readlines()
print(todas[1])

''' Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''
archivo = open('mi_archivo.txt', 'w')
archivo.write("Nuevo texto")
archivo.close()
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()

''' Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
Imprime el contenido completo de "mi_archivo.txt" al finalizar.
Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''
archivo = open('mi_archivo.txt', 'a')
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

'''Práctica Crear y Escribir Archivos 3 Utiliza el método writelines para escribir los valores de la siguiente lista 
al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en 
modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.'''
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open('registro.txt', 'a')

for p in registro_ultima_sesion:
    archivo.writelines(p + '\t')

archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())

''' Práctica Path 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()'''
from pathlib import Path
ruta_base = Path.home()

'''Práctica Path 2 Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir 
de la siguiente estructura de carpetas: Almacena el directorio obtenido en la variable ruta. No olvides importar 
Path.'''
from pathlib import Path

ruta = Path("Curso Python", "Día 6", "practicas_path.py")


'''Práctica Path 3 Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir 
de la siguiente estructura de carpetas: Almacena el directorio obtenido en la variable ruta. No olvides importar 
Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.'''

from pathlib import Path
base = Path.home()
ruta1 = Path(base, "Curso Python", "Día 6", "practicas_path.py")

'''Práctica Archivos y Funciones 1 Crea una función llamada abrir_leer() que abra (open) un archivo indicado como 
parámetro, y devuelva su contenido (read).'''
def abrir_leer(path):
    archivo = open(path, 'r')
    return archivo.read()
'''Práctica Archivos y Funciones 2 Crea una función llamada sobrescribir() que abra (open) un archivo indicado como 
parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"'''
def sobrescribir(path):
    archivo = open(path, 'w')
    archivo.write("contenido eliminado")
    archivo.close()

'''Práctica Archivos y Funciones 3 Crea una función llamada registro_error() que abra (open) un archivo indicado como 
parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.'''
def registro_error(path):
    archivo = open(path, 'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()

''' '''


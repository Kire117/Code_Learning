import shutil
import os
import datetime
import time
import re
import timeit
import math
from pathlib import Path


'''archivo_zip = "Proyecto+Dia+9.zip"
shutil.unpack_archive(archivo_zip, 'Proyecto_dia9', 'zip')  # importar archivo con shutil module
# para seguir con el proyecto del dia 9'''
inicio = time.time()
path = 'Proyecto_dia9/Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
fecha_hoy = datetime.datetime.today().strftime("%d/%m/%y")
num_encontrados = []
arch_encontrados = []

def buscar_numeros(archivo, patron):
    mi_archivo = open(archivo, 'r')
    texto = mi_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(path):
        for arch in archivo:
            resultado = buscar_numeros(Path(carpeta,arch), patron)
            if resultado != '':
                num_encontrados.append(resultado.group())
                arch_encontrados.append(arch.title())

def mostrar_todo():
    index = 0
    print('-'*50)
    print(f"Fecha de busqueda: {fecha_hoy}")
    print("\n")
    print("Archivo\t\t\tNRO. SERIE")
    print('-------\t\t\t----------')
    for item in arch_encontrados:
        print(f'{item}\t{num_encontrados[index]}')
        index += 1
    print('\n')
    print(f"Numeros encontrados : {len(num_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)} segundos!")

crear_listas()
mostrar_todo()







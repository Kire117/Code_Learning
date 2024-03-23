import os

''' get current working directory
ruta = os.getcwd() 
print(ruta) '''
''' remueve la carpeta o directorio dada en el path por las comillas simples'''
os.rmdir('C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\otra_carpeta')
''' change directory'''
ruta = os.chdir('C:\\Users\\Aleja\\OneDrive\\Escritorio\\Georgian College')
''' creates a new directory in the path'''
ruta1 = os.makedirs('C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\otra_carpeta')

archivo = open('otro_archivo.txt')
print(archivo.read())


ruta2 = 'C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\Prueba1.txt'
# refers to base name lit
elemento = os.path.basename(ruta2)
elemento2 = os.path.dirname(ruta2)
elemento3 = os.path.split(ruta2)
print(elemento)
print(elemento2)
print(elemento3) # lo que entregara como output sera una tuple where the first parameter is the directory name
# and the 2nd is the basename


otro_archivo = 'prueba1.txt'

from pathlib import Path

carpeta = Path('C:/Users/Aleja/OneDrive/Escritorio/Georgian College')
mi_archivo = carpeta / 'otro_archivo.txt'

mi2_archivo = open(mi_archivo)
print(mi2_archivo)



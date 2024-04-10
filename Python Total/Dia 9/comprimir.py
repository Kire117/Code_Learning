import zipfile

'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w') # .ZipFile() quiere decir archivo comprimido, que pide 2
# parametros, 1er parametro = archivo que queramos comprimir

mi_zip.write('mi_texto_A.txt') # nombre del archivo que voy a comprimir que al ejecutar lo que hara es agregarlo dentro
# del zip
mi_zip.write('mi_texto_B.txt')

mi_zip.close() # esta es una manera de comprimir archivos utilizando zipfile module'''

'''zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

zip_abierto.extractall()
zip_abierto.close() # esta es una manera de extraer todos los archivos utilizando zipfile module, sin embargo, 
# se pueden extraer un por uno con el metodo .extract() donde te pide como parametro el nombre del archivo comprimido
# y el archivo el cual quieres extraer'''

import shutil

'''carpeta_origen = "PDF'S"
archivo_destino = 'todo_comprimido'  # este es el nombre del archivo comprimido al que queremos guardar los cambios
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)'''
''' este codigo sirve para comprimir todos los archivos y/o 
carpetas dentro de una ruta en el formato zip como se muestra, donde los 3 parametros que te pide el metodo 
.make_archive(archivo(nombre), formato('zip', archivo(ruta a comprimir)) donde el formato en este caso estamos usando
 'zip' para crear un archivo zip'''

shutil.unpack_archive('todo_comprimido.zip', 'Extraccion Terminada',
                      'zip')  # donde el primer parametro es el archivo a descomprimir, el segundo
# parametro es el nombre de la carpeta el cual le quiere asignar donde se guardaran todos los archivos descomprimidos y
# finalmente el formato que estamos usando es ZIP

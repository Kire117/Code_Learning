import os

mi_archivo = open('Prueba.txt')

# mi_archivo.read() lee el archivo completo
# una_linea = mi_archivo.readline()
# print(mi_archivo.read())
# print(una_linea)

# una_linea = mi_archivo.readline()
# print(una_linea)

# una_linea = mi_archivo.readline()
#
# print(una_linea)

''' for l in mi_archivo:
    print("Aqui dice: " + l) '''

todas = mi_archivo.readlines()
''' el output saldra convertido en forma de lista, lo cual facilita la manera para trabajar con metodos de listas '''
print(todas)
mi_archivo.close()
todas = todas.pop()
print(todas)



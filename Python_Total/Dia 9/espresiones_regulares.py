import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

busqueda = re.search(patron, texto)

print(busqueda)
print(busqueda.start())
print(busqueda.end())
print(busqueda.span())

busqueda1 = re.findall(patron, texto)  # lo que retorna como resultado es la busqueda envuelto de una lista
print(type(busqueda1))
print(busqueda1)

print('\n')
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())

texto2 = "llama al 564-525-6588 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron_cantificadores = r'\d{3}-\d{3}-\d{4}'
patron2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron_cantificadores, texto2)
print(resultado.group())  # al utlizar el metodo .group(), nos dara como resultado la busqueda como tal en este caso
# el numero en el texto 2

resultado2 = re.search(patron2, texto2)
print(resultado2.group(2))  # al compilarlos usando el metodo .compile(r'expresion regular') estamos almacenando
# grupos entre los parentesis dentro de la expresion y podemos realizar la busqueda por grupos, en este caso,
# el segundo grupo en el texto2 vendria siendo 525 como output

''' ejemplos de casos de uso, que le pidas al usuario una clave que empiece con una letra y que en total tenga
8 caracteres'''
'''
clave = input("Clave: ")
patron_clave = r'\D{1}\w{7}'
chequear = re.search(patron_clave, clave)

print(chequear)'''

''' operadores especiales en expresiones regulares'''
texto3 = 'no atendemos los lunes por la tarde'
# | operador especial o

buscar = re.search(r'lunes|martes', texto3)
print(buscar)
buscar1 = re.search(r'....demos...', texto3)  # los puntos agregan lo que sea en el buscador
print(buscar1)
# ^ operador especial ascento circunflejo, sirve para verificar si un patron se encuentra al comienzo del string
buscar2 = re.search(r'^\D', texto3)
print(buscar2)
# operador especial $ moneda, sirve para checar si no hay digito al final del string
texto3_1 = 'no atendemos los lunes por la tarde'
texto3_2 = 'no atendemos los lunes por la tarde1'
buscar2_1 = re.search(r'\D$', texto3_1)
buscar2_2 = re.search(r'\D$', texto3_2)
print(buscar2_1)
print(buscar2_2)
# operadores especiales en conjunto son [^] llaves rectas con ascento circunflejo dentro, lo que pongamos dento de las
# llaves lo tendra que excluir dentro del patron
buscar3 = re.findall(r'[^\s]', texto3)
print(buscar3)  #el output nos dara como resultado todos los caracteres que no sean espacios vacios por que lo que
# buscamos precisamente es excluir estos espacios vacios dentro del texto
buscar4 = re.findall(r'[^\s]+', texto3)  # caracter especial + mas, sirve para decir 1 o mas veces
print(buscar4)  #el output nos dara como resultado todos las palabras que no contengan espacios vacios por que lo que
# buscamos precisamente es excluir y agrupar las palabras como tal en lugar de solo caracteres, por que cada vez que
# se encuentre un espacio vacio va acortar el grupo


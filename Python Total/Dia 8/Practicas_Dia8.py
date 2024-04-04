'''Práctica Manejo de Errores 1 Hemos visto en la lección de qué manera se implementa el manejo de errores
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma
ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario,
verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en
pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre
los dos números.'''

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""


def suma(num1,num2):
        try:
            print(num1+num2)
        except:
            print("Error inesperado")

'''Práctica Manejo de Errores 2 Hemos visto en la lección de qué manera se implementa el manejo de errores 
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma 
ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, 
verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.

Implementa para la siguiente función cociente(), un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo 
argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los dos 
números entregados como argumento.'''
def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
''' Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el 
mensaje: "El archivo no fue encontrado"
En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
En todos los casos, al finalizar, imprimir: "Finalizando ejecución"'''

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

'''Práctica Generadores 1 Crea un generador (almacenado en la variable generador) que sea capaz de devolver una 
secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea 
llamada mediante next.'''
def generador():
    for num in range(0, 1000):
        yield num

generador = generador()

print(next(generador))

'''Práctica Generadores 2 Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera 
indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo 
(7, 14, 21, 28...).'''

def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1

generador = multiplos_siete()

'''Práctica Generadores 3 Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva 
un mensaje cada vez que sea llamado:
"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
Almacena el generador en la variable perder_vida'''

"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"

def generador():
    personaje_vida = 3
    yield "Te quedan 3 vidas"

    personaje_vida = 2
    yield "Te quedan 2 vidas"

    personaje_vida = 1
    yield "Te queda 1 vida"

    personaje_vida = 0
    yield "Game Over"

perder_vida = generador()

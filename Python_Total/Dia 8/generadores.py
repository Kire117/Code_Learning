def mi_generador():
    yield 4


g = mi_generador()
print(next(g))


# ejemplo de generador utilizando una lista para pedir cada numero cuando se necesite

def mi_otro_generador():
    for num in range(1, 5):
        yield num * 10


og = mi_otro_generador()
print(next(og))
print(next(og))
print(next(og))
print(next(og))
'''print(next(og))  ojo a pesar de que en el rango esta el numero 5 solo se puede iterar 4 veces ya que
por conveniencia la iteracion empieza desde el numero 0, por lo tanto en la linea 19 dara un error, ya que
no tiene mas numeros por el cual iterar '''


def generador():
    x = 1
    yield x

    x += 2  # como el anterior num es 1 sumara 2 y dara como resultado 3
    yield x

    x += 4
    yield x


ge = generador()

print(next(ge))
print(next(ge))
print("hola mundo")  # cosa buena de los generadores es que si en medio de los call a la siguiente produccion
# hay otra tarea, funciones, etc, este seguira trabajando hasta que se pida el sig num como a continuacion
print(next(ge))

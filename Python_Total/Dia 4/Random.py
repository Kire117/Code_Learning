from random import *

aleatorio = randint(1,50)
aleatorio2 = round(uniform(1,5),1)
aleatorio3 = random() # valor entre 0 y 1 contando con decimales
print(aleatorio)
print(aleatorio2)
print(aleatorio3)

colores = ['rojo', 'azul', 'verde', 'amarillo']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

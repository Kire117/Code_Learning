mi_lista = [ 'a', 'b', 'c']
otra_lista = ["hola" , 55 , 6.1]
mi_lista2 = ['d', 'e', 'f']
resultado = len(otra_lista)
mi_lista4 = ['g', 'o', 'b', 'm', 'c']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
mi_lista3.append('g')
eliminado = mi_lista3.pop(1)

print(resultado)
print(mi_lista3)
print(type(mi_lista))
print(eliminado)
print(mi_lista4.sort())
print(mi_lista4.reverse())



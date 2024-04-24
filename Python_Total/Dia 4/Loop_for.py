lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"La letra es: {letra} en el indice {numero_letra}")

lista2 = ['pablo', 'laura', 'fede', 'luis', 'kire']
for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)

numeros = [1,2,3,4,5]

mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

palabra = 'Python'
print("\n")
for letra in palabra:
    print(letra)

print("\n")
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)

# palabra = 'python'
lista = [letra for letra in 'python']
print(lista)

lista2 = [n for n in range(0, 21, 2)]
print(lista2)

lista3 = [n ** 2 for n in range(0, 21, 2)]
print(lista3)

lista4 = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista4)

lista5 = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista5)

pies = [10, 20 ,30 ,40 ,50]
metros = [p / 3.281 for p in pies]
print(metros)





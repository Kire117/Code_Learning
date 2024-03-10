lista1 = [55, 99, 69]
lista2 = [555, 69, 600]

def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

# resultado = chequear_3_cifras(lista1)
# print(resultado)
resultado2 = chequear_3_cifras(lista2)
print(resultado2)
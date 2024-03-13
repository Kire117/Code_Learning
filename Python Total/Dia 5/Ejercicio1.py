def devolver_distintos(a,b,c):
    suma = a + b + c
    lista = [a,b,c]
    if suma > 15:
        max_num = max(lista)
        return max_num
    elif suma < 10:
        min_num = min(lista)
        return min_num
    else:
        lista.sort()
        return lista[1]

print(devolver_distintos(20, 5 , 7))
print(devolver_distintos(7, 2 , 4))
print(devolver_distintos(3, 2 , 7))
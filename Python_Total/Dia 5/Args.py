def suma(*args):
    total = 0
    for n in args:
        total+= n
    return total

print(suma(5,6,5,1,10,500))


def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

numeros_persona('Kire',1,2,3,4,5,6)
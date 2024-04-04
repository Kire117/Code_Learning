
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')

    return otra_funcion

# decorador = @
# @decorar_saludo
def mayusculas(texto):
    print(texto.upper())
# @decorar_saludo
def minusculas(texto):
    print(texto.lower())

#mayuscula_decorada = decorar_saludo(mayusculas)
#mayuscula_decorada("kire")
decorar_saludo('kire')
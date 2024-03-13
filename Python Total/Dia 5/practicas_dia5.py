# Práctica Métodos y Ayuda 1 Remueve los caracteres a la izquierda de nuestro texto principal: , : % _ Utiliza el
# método lstrip(). Imprime el resultado en pantalla: ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#" Busca en la
# documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables
# intermedias si las necesitas.

palabra = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
palabra = palabra.lstrip('#_,:_%')
print(palabra)

# Práctica Métodos y Ayuda 2 Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas",
# utilizando el método insert(): Busca en la documentación acerca del funcionamiento del método solicitado para saber
# cómo actúa y cómo es su funcionamiento.

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')

# Práctica Métodos y Ayuda 3 Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen
# elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:
# Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su
# funcionamiento.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)

''' Práctica Crear Funciones 1
Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

Solo debes definir la función, no debes invocarla luego.'''
def saludar():
    print("¡Hola mundo!")

'''Práctica Crear Funciones 2 Declara una función llamada bienvenida, que tome como argumento el nombre de una 
persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"

Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.

Solo debes definir la función y crear la variable, no debes invocar la función luego.'''
nombre_persona = ''
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
'''Práctica Crear Funciones 3 Declara una función llamada cuadrado, que tome como argumento un número cualquiera, 
y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).

El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.

Solo debes definir la función y crear la variable, no debes invocar la función luego.'''
un_numero = 10
def cuadrado(un_numero):
    print(un_numero ** 2)

'''Práctica Return 1 Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá 
devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como 
exponente:'''
def potencia(num1, num2):
    return num1 ** num2

'''Práctica Return 2 Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en 
dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, 
tomaremos la conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su 
resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para 
obtener el monto equivalente en euros.'''
dolares = 100
def usd_a_eur(dolares):
    return dolares * 0.90

'''Práctica Return 3 Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como 
argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como 
argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.'''
palabra = 'Curso'
def invertir_palabra(palabra):
    return palabra[::-1].upper()

'''Práctica Funciones Dinámicas 1 Crea una función (todos_positivos) que reciba una lista de números como parámetro, 
y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. 
Crea una lista llamada lista_numeros con valores positivos y negativos.
No invoques la función, solo es necesario definirla.'''

lista_numeros = [1, 25 , -35]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True

'''Práctica Funciones Dinámicas 2 Crea una función (suma_menores) que sume los números de una lista (almacenada en la 
variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.'''
lista_numeros = [1,50,500,750,-1]
def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(1,1000):
            suma += n
    return suma

'''Práctica Funciones Dinámicas 3 Crea una función (cantidad_pares) que cuente la cantidad de números pares que 
existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
def cantidad_pares(lista_numeros):
    cantidad_pares = 0
    for n in lista_numeros:
        if n % 2 == 0:
            cantidad_pares += 1
    return cantidad_pares

''' Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función 
debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:
"La suma de tus dados es {suma_dados}. Lamentable"
Si la suma es mayor a 6 y menor a 10:
"La suma de tus dados es {suma_dados}. Tienes buenas chances"
Si la suma es mayor o igual a 10:
"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.'''

from random import *
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

'''Práctica sobre Interacción entre Funciones 2 Crea una función llamada reducir_lista() que tome una lista como 
argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando 
uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo'''
lista_numeros = [1,2,15,7,2]

def reducir_lista(lista_numeros):
        lista_sin_duplicados = list(dict.fromkeys(lista_numeros))

        max_valor = max(lista_sin_duplicados)

        lista_sin_max = [num for num in lista_sin_duplicados if num != max_valor]

        return lista_sin_max

def promedio(lista_sin_max):
    return sum(lista_sin_max) / len(lista_sin_max)

'''Práctica sobre Interacción entre Funciones 3 Crea una función (llamada lanzar_moneda) que devuelva el resultado de 
lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir 
argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del 
lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con 
valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (
devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.'''
from random import *
def lanzar_moneda():
    moneda = ['Cara','Cruz']
    return choice(moneda)

lista_numeros = [1,2,3,4,5]
def probar_suerte(moneda, lista_numeros):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        lista_numeros.clear()
        return lista_numeros
    else:
        print("La lista fue salvada")
        return lista_numeros

'''Práctica sobre Argumentos Indefinidos (*args) 1 Crea una función llamada suma_cuadrados que tome una cantidad 
indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).'''
def suma_cuadrados(*args):
    suma = 0
    for n in args:
        suma += n ** 2
    return suma

'''Práctica sobre Argumentos Indefinidos (*args) 2 Crea una función llamada suma_absolutos, que tome un conjunto de 
argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin 
signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).'''

def suma_absolutos(*args):
    suma = 0
    suma = sum(abs(num) for num in args)
    return suma

''' Práctica sobre Argumentos Indefinidos (*args) 3
Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"'''

def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

'''Práctica sobre Argumentos Indefinidos (**kwargs) 1 Crea una función llamada cantidad_atributos que cuente la 
cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.'''

def cantidad_atributos(**kwargs):
    contar = 0
    for element in kwargs:
        contar+= 1
    return contar

'''Práctica sobre Argumentos Indefinidos (**kwargs) 2 Crea una función llamada lista_atributos que devuelva en forma 
de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer 
recibir cualquier cantidad de argumentos de este tipo.'''

def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista
'''Práctica sobre Argumentos Indefinidos (**kwargs) 3 Crea una función llamada describir_persona, que tome como 
parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:'''
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

''' '''

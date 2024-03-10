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



# Práctica con Variables 1
# Declara dos variables, llamadas nombre y edad.

# Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.

# ANSWER--------------------------------
nombre = "Tony Soprano"
edad = 51

# Práctica con Variables 2
# Crea tres variables:

# nombre
# apellido
# nombrecompleto

# A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente, construye la variable
# nombrecompleto concatenando las variables (recuerda sumar un espacio intermedio).

# ANSWER----------------------------------

nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido

# Práctica con Variables 3
# Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
# Estás tomando un curso de curso

# ANSWER-------------------------------------------
curso = "Python"
print("Estás tomando un curso de " + curso)

# Práctica con Integers
# Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.

# Imprime el tipo de dato de dicha variable.

num_entero = 13

print(type(num_entero))

# Práctica con Floats
# Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.

# Imprime el tipo de dato de dicha variable.

num_decimal = 1.17

print(type(num_decimal))

# Práctica con Tipos de Datos Numéricos
# ¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.

# Para ello, crea dos variables:

#num1 = 7.5

#num2 = 2.5

# A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))

# Práctica con Conversiones 1
# Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:

num1 = 7.5
num1 = int(num1)
print(type(num1))

# Práctica con Conversiones 2
# Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:

num2 = 10
num2 = float(num2)
print(type(num2))

# Práctica con Conversiones 3
# Suma los valores de num1 y num2.

# No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función
# print().

num1 = "7.5"
num2 = "10"
print(float(num1) + int(num2))

# Práctica Formatear Cadenas 1
# Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

# Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# Práctica Formatear Cadenas 2
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

# Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

# Práctica Formatear Cadenas 3
# Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

#Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

# En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_nuevos + puntos_anteriores
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

z = 7
y = 2
print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{z} modulo de  {y} es igual {z%y}")
print(f"{z} elevado a la {y} es igual a {z**y}")
print(f"La raiz cuadrad de {z} es {z**0.5}") # RAIZ CUADRADA FORMULA

# Práctica Operadores Matemáticos 1
# Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.
a = 874
b = 27
print(f"{874//27}")

# Práctica Operadores Matemáticos 2
# Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.
# Debes mostrar solo el valor numérico que resulta de esta operación.

a = 456
b = 33
print(f"{a%b}")

# Práctica Operadores Matemáticos 3
# Calcula y muestra en pantalla la raíz cuadrada de 783.
# Debes mostrar solo el valor numérico que resulta de esta operación.
c = 783
print(f"{c**0.5}")

# Práctica Redondeo 1
# Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.
resultado = 10/3
print(round(resultado, 2))

# Práctica Redondeo 2
# Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.
valor = 10.676767
print(round(valor))

# Práctica Redondeo 3
# Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.
num = round(5**0.5, 4)
print(num)





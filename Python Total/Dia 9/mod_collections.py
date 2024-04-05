from collections import Counter, defaultdict, namedtuple

numeros = [1, 3, 5, 3, 5, 6, 7, 5, 3, 2, 8, 54, 7, 9, 5, 0, 5]
frase = 'al pan pan y al vino vino'
print(Counter(numeros))
print(Counter("misisipi"))
print(Counter(frase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4])
print(list(serie))
print(serie.most_common(2))  # si se deja vacio por defecto mostrata todos los numeros repetidos del mas alto al
# mas bajo, pero si se pone un valor entre los parentesis puede demostrar solo los primeros numeros ejemplo seria 2
# que de esa lista que cuenta con 4 numeros solo mostrara los 2 primero mas altos
print(len(serie))  # solo mostrara cuantos numeros hay repetidos, aunque haya el mismo numero varias veces este
# solo se contara en si solo y en este caso tenemos 4 numeros en la lista repetida varias veces
print(serie.values())  # en este caso los valores seran cuantas veces se encuentra dicho numero dentro de la lista'
print(serie.total())  # en este caso contara cuantos numeros hay dentro de la lista, como tenemos 16 numeros
# repetidos el output sera de 16
print(serie.pop(3))  # en este caso tomara como valor el numero que le pongamos dentro y el numero de veces
# repetidos dentro de la lista, en este caso el 3 esta repetido 4 veces
print(serie.items())  # en este caso nos dara tanto el numero como los valores como un diccionario normal
# pero como sacamos el numero 3 atraves del metodo pop solo nos dara 3 items del diccionario\
print(serie.popitem())  # en este caso nos dara el ultimo item del diccionario
print(serie.keys())  # en este caso solo no dara los numeros sin sus repeticiones, aqui como sacamos el ultimo item
# a traves del metodo popitem() solo nos dara 2 numeros
# print(serie.copy()) # este metodo copiara el diccionario en su totalidad, haciendola que la podamos almacenar
# dentro de una variable cuando nos sea necesario
c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements())  # ejemplo de uso
print(serie.get(2))  # en este caso nos otorgara cuantos numeros esta repetido el argumento(numero) que le pongamos
# en este caso como el numero 2 esta repetido 5 veces nos dara 5
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)  # en este caso lo que hara es restar entre 2 counters
print(serie.clear())  # no recibe argumentos y lo que hace es borrar el counter entero

mi_dic = defaultdict(lambda: 'nada')  # le estamos diciendo que al valor que se pida y no se encuentre dentro del
# dic le asigne como valor 'nada'

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])  # lo que hay que saber es que se agregara otro item y por lo tanto tendra 2 items el dic
# donde 2 como error al no estar dentro del dic sera agregado y al imprimir el dic completo el valor de este
# sera 'nada' como a continuacion
print(mi_dic)  # output: defaultdict(<function <lambda> at 0x0000019FE77B9080>, {'uno': 'verde', 'dos': 'nada'})
''' tarea, investigar los attributes y metodos de defaultdic en la documentacion de python'''

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('ariel', 1.76, 79)
print(ariel.peso)
# tambien se puede accesar del modo simple que es atraves de los indices
print(ariel[1])
''' tarea: investigar en la documentacion de namedtuple para saber los metodos y attributes'''
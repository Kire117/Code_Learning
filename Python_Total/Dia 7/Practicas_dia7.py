""" Práctica Clases 1
Crea una clase llamada Personaje y a continuación, crea un objeto a partir de ella, por ejemplo: harry_potter"""


class Personaje():
    pass


harry_potter = Personaje()

'''Práctica Clases 2 Crea una clase llamada Dinosaurio, y tres instancias a partir de ella: velociraptor, 
tiranosaurio_rex y braquiosaurio .'''


class Dinosaurio():
    pass


velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()
'''Práctica Clases 3 Crea una clase llamada PlataformaStreaming y crea los siguientes objetos a partir de ella: 
netflix, hbo_max, amazon_prime_video'''


class PlataformaStreaming():
    pass


netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()

''' Práctica Atributos 1
Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.'''


class Casa():
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)

''' Práctica Atributos 2
Crea una clase llamada Cubo, y asígnale el atributo de clase:
caras = 6
y el atributo de instancia:
color
Crea una instancia cubo_rojo, de dicho color.'''


class Cubo():
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('rojo')

''' Práctica Atributos 3
Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:
real = False
Crea una instancia llamada harry_potter con los siguientes atributos de instancia:
especie = "Humano"
magico = True
edad = 17'''


class Personaje():
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', True, 17)

''' Práctica Métodos 1
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla 
"Guau!".'''


class Perro():
    def ladrar(self):
        print("Guau!")


mi_perro = Perro()
mi_perro.ladrar()

''' Práctica Métodos 2
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.'''


class Mago():
    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()
merlin.lanzar_hechizo()

'''Práctica Métodos 3 Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). 
El método debe imprimir en pantalla el mensaje
"La alarma ha sido pospuesta {cantidad_minutos} minutos"'''


class Alarma():

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


reloj = Alarma()
reloj.postergar(5)

'''Práctica Tipos de Métodos 1 Crea un método estático respirar() para la clase Mascota. Cuando se llame, 
debe imprimir en pantalla "Inhalar... Exhalar"'''


class Mascota():
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


'''Práctica Tipos de Métodos 2 Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la 
clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, 
debe ser False.'''
class Jugador():
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

'''Práctica Tipos de Métodos 3 Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que 
tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.'''
class Personaje():

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

'''Práctica Herencia 1 Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, 
edad. Crea otra clase, Alumno, que herede de la primera estos atributos.'''

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    pass

'''Práctica Herencia 2 Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, 
cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.'''
class Mascota():
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass
'''Práctica Herencia 3 Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar 
el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.'''
class Vehiculo():
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass
'''Práctica Herencia Extendida 1 Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la 
vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar 
correctamente de Padre y Madre.
Completa el código suministrado a continuación para lograrlo.'''
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass

'''Práctica Herencia Extendida 2 "El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, 
pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" 
un animal que tiene los siguientes métodos y atributos: 
- poner_huevos() - tiene_pico = True - vertebrado = True - 
venenoso = True - nadar() - caminar() - amamantar()'''

class Vertebrado:
    def __init__(self):
        self.vertebrado = True

class Pez:
    def nadar(self):
        print("El ornitorrinco nada")

class Reptil:
    def caminar(self):
        print("El ornitorrinco camina")

class Ave:
    def poner_huevos(self):
        print("El ornitorrinco pone huevos")
        self.tiene_pico = True

class Mamifero:
    def amamantar(self):
        print("El ornitorrinco amamanta a sus crías")
        self.venenoso = True

class Ornitorrinco(Vertebrado, Pez, Reptil, Ave, Mamifero):
    def __init__(self):
        super().__init__()

# Crear una instancia de Ornitorrinco
ornitorrinco = Ornitorrinco()

# Llamar a los métodos
ornitorrinco.poner_huevos()
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()

# Imprimir atributos
print(f"Tiene pico: {ornitorrinco.tiene_pico}")
print(f"Es venenoso: {ornitorrinco.venenoso}")

'''Práctica Herencia Extendida 3 Un hijo ha heredado de su padre todas sus características, sin embargo, 
tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, sobreescribiendo el 
método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre" [1]: asegúrate de utilizar return 
seguido de una cadena de texto'''
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

'''Práctica Polimorfismo 1 La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula 
el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items 
o caracteres que lo componen. Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en 
pantalla (print()) para cada uno de ellos su longitud con la función len(). Puedes recordar cómo implementar la 
función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html'''
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

def iterador(parametro):
    print(len(parametro))

iterador(palabra)
iterador(lista)
iterador(tupla)

''' Práctica Polimorfismo 2
Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.

Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método 
atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir 
un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.'''
class Mago():
    def atacar(self):
        print("Ataque mágico")
class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
class Samurai():
    def atacar(self):
        print("Ataque con katana")
personaje1 = Arquero()
personaje2 = Mago()
personaje3 = Samurai()

personajes = [personaje1, personaje2, personaje3]

for personaje in personajes:
    personaje.atacar()

''' Práctica Polimorfismo 3
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.
Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus 
personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.'''
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

personaje1 = Mago()
personaje2 = Arquero()
personaje3 = Samurai()

personaje_defender(personaje1)
personaje_defender(personaje2)
personaje_defender(personaje3)

'''Práctica Métodos Especiales 1 Dada la clase Libro, implementa el método especial __str__ para que cada vez que se 
imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas 
dobles).'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
'''Práctica Métodos Especiales 2 Dada la clase Libro, implementa el método especial __len__ para que cada vez que se 
ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
    def __len__(self):
        return self.cantidad_paginas

'''Práctica Métodos Especiales 3 Dada la clase Libro, implementa el método especial __del__ para que el usuario sea 
informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")


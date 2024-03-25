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



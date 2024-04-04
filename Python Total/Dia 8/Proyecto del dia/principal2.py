import numeros2


def preguntar():
    print("Bienvenido a Farmacias Kire")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos")
        try:
            mi_rubro = input("Elija su area: ").lower()
            ["p", "f", "c"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion validad")
        else:
            break

    numeros2.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno= input("Quieres sacar otro turno?: ").lower()
            ['s', 'n'].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == 'n':
                print("Gracias por su visita")
                break

inicio()

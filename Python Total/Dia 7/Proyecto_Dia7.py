from random import randint
import time
''' Este proyecto es una cuenta bancaria'''

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f'Hola {self.nombre} {self.apellido}.'
                f'\nNumero de cuenta: {self.numero_cuenta}'
                f'\nSaldo: {self.balance}')

    def depositar(self):
        print("Has elegido depositar")
        deposito = float(input("Cuanto deseas depositar? :"))
        nuevo_balance = self.balance + deposito
        self.balance = nuevo_balance
        print(f"Tu nuevo balance es: {self.balance}")


    def retirar(self):
        print("Has elegido retirar")
        print(f"Tu saldo es {self.balance}")
        retiro = float(input("Cuanto deseas retirar?: "))
        if retiro > self.balance:
            print("No puedes retirar esa cantidad, ya que no cuentas con ello")
        else:
            nuevo_balance = self.balance - retiro
            self.balance = nuevo_balance
            print(f"Tu nuevo balance es: {self.balance}")


def crear_cliente():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    numero_cuenta = randint(1, 200)
    balance = int(input("Escribe tu balance: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)


def inicio():
    cliente = crear_cliente()
    answer = input("Deseas continuar?(Y/N) ").lower()
    while answer == 'y' or answer == 'yes':
        print('*' * 5 + "Opciones" + '*' * 5)
        print('\n[1]Depositar'
              '\n[2]Retirar'
              '\n[3]Ver Balance'
              '\n[4]Salir')
        opcion = int(input("Escoge una opcion: "))

        if opcion == 1:
            cliente.depositar()
            time.sleep(5)
        elif opcion == 2:
            cliente.retirar()
            time.sleep(5)
        elif opcion == 3:
            print(cliente)
            time.sleep(5)
        elif opcion == 4:
            print("Gracias por usar el menu!")
            exit()

inicio()

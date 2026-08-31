from Scooter import Scooter

class Usuario:
    def __init__(self, nombre: str = "Ingrese nombre", saldo: float = 0.00): #usar float en lugar de double porke no existe
        self.__nombre = nombre
        self.__saldo = saldo

    def get_nombre(self) -> str:
        return self.__nombre

    def get_saldo(self) -> float:
        return self.__saldo

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_saldo(self, saldo: float):
        self.__saldo = saldo

    #métodos
    def agregarSaldo(self, monto: float):
        self.__saldo = (self.__saldo + monto)
        print ("Se agregó dinero a su saldo")

    def rentarScooter(self, scooter: Scooter, costo: float) -> bool: #recibir el scooter y el costo como parámetro
        if self.__saldo >= costo: #si se tiene suficiente dinero
            if scooter.desbloquear(): #si el scooter está desbloqueado
                self.__saldo = (self.__saldo - costo) #restar a la cuenta del usuario el costo
                print("Scooter rentado!")
                return True #devolver verdadero porque todo se cumplió
            else:
                print("Scooter no disponible...") #el scooter no está disponible o no tiene suficiente batería
                return False
        else:
            print("Vuestro saldo es insuficiente unu")
            return False
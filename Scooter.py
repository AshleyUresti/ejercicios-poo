class Scooter:
    def __init__(self, scooter_ID: str = "S-000", bateria: int = 50, estaDisponible: bool = True):
        self.__scooter_ID = scooter_ID
        self.__bateria = bateria
        self.__estaDisponible = estaDisponible

    def get_scooter_ID(self) -> str:
        return self.__scooter_ID

    def get_bateria(self) -> int:
        return self.__bateria

    def get_estaDisponible(self) -> bool:
        return self.__estaDisponible

    def set_scooter_ID(self, scooter_ID: str):
        self.__scooter_ID = scooter_ID

    def set_bateria(self, bateria: int):
        self.__bateria = bateria

    def set_estaDisponible(self, estaDisponible: bool):
        self.__estaDisponible = estaDisponible

    #métodos
    def desbloquear(self) -> bool:
        if self.__estaDisponible and self.__bateria > 0: #si el scooter está disponible y tiene bateria
            self.__estaDisponible = False #dejar como no disponible el scooter porque lo usará un usuario
            return True #devolver verdadero
        return False #si no se cumple el if, devuelve falso

    def finalizarViaje(self):
        self.__estaDisponible = True #dejar el scooter como disponible porque ya no se está usando
        print("\nviaje concluido, hasta pronto")

    def cargarBateria(self):
        self.__bateria = 100 #se llena la bateria al 100
        print ("\nbatería al 100%")
    
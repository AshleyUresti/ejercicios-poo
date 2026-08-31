class Carro:
    #constructor por default
    def __init__(self, color: str = "Negro", año: int = 0, matricula: str = "XX-XX"):
        #atributos privados
        self.__color = color
        self.__año = año
        self.__matricula = matricula

    #para ver el contenido del objeto
    def get_color(self) -> str:
        return self.__color

    def get_año(self) -> int:
        return self.__año

    def get_matricula(self) -> str:
        return self.__matricula

    #para reescribir el contenido del objeto
    def set_color(self, color: str):
        self.__color = color
    
    def set_año(self, año: int):
        self.__año = año

    def set_matricula(self, matricula: str):
        self.__matricula = matricula
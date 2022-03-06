class Carro:
    __id: int
    __modelo: str
    __categoria: str
    __valor: float

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: int):
        self.__modelo = modelo

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: int):
        self.__categoria = categoria

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)
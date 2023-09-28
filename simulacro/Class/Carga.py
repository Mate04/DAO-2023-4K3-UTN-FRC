from abc import ABC

class Carga(ABC):
    def __init__(self, contenido:str) -> None:
        self.contenido = contenido
    def __str__(self) -> str:
        return ('='*20+'\n')+f'{self.__class__.__name__}\ncontenido: {self.contenido}'
    def peso(self):
        pass
from Class.Carga import Carga
class Caja(Carga):
    def __init__(self,contendido:str,peso:float) -> None:
        super().__init__(contendido)
        self.peso_ = peso
    def __str__(self) -> str:
        return super().__str__()+f'\npeso: {self.peso}'
    def peso(self):
        return self.peso_
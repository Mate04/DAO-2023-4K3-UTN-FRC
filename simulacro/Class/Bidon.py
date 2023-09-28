from Class.Carga import Carga

class Bidon(Carga):
    def __init__(self, contenido: str,capacidad:float ,densidad:float) -> None:
        super().__init__(contenido)
        self.capacidad = capacidad
        self.densidad = densidad
    def __str__(self) -> str:
        return super().__str__()+f'\nCapacidad: {self.capacidad}\n'+f'Densidad: {self.densidad}\nPeso: {self.peso()}'
    def peso(self):
        return self.densidad * self.capacidad
    
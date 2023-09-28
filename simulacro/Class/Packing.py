from Class.Carga import Carga

class Packing(Carga):
    def __init__(self, contenido: str, peso_x_caja:float,cantidad:int,peso_estructura:float) -> None:
        super().__init__(contenido)
        self.peso_x_caja = peso_x_caja
        self.cantidad = cantidad
        self.peso_estructura = peso_estructura
    def peso(self):
        return (self.cantidad * self.peso_x_caja)+ self.peso_estructura
    def __str__(self) -> str:
        return super().__str__() + f'\nPeso de cada caja {self.peso_x_caja}\n'+f'Cantidad de cajas: {self.cantidad}\n'+f'Peso de la estructura {self.peso_estructura}\n'+f'Peso total: {self.peso()}'

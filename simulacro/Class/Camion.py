from Class.Carga import Carga

class Camion:
    def __init__(self,carga_max:int, patente:str) -> None:
        self.cargas = dict()
        self.estado = True #marca si se encuentra disponible
        self.patente = patente
        self.carga_max = carga_max
    def subirCargar(self,Object:Carga):
        try:
            if not isinstance(Object, Carga):
                raise TypeError("El objeto no pertenece a la clase Carga, ni sus Hijas")
            if self.carga_max < Object.peso() + self.pesoTotal():
                raise TypeError('Sobre Exceso de carga')
            id=len(self.cargas)+1
            self.cargas[id] = Object
        except TypeError as e:
            print(e)
    def bajarCarga(self,Object:Carga):
        try:
            flag = 0
            for key, value in self.cargas.items():
                if value == Object: flag = key
            if not flag:
                raise TypeError("No existia este elemeto")
            self.cargas.pop(flag)
        except TypeError as e:
            print(e)
    def pesoTotal(self):
        pesoTotal=0
        for key,value in self.cargas.items():
            pesoTotal += value.peso()
        return pesoTotal
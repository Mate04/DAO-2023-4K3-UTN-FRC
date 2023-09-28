from Class.Carga import Carga

class Camion:
    
    def __init__(self,carga_max:int, patente:str) -> None:
        self.cargas = dict()
        self.estado = True #marca si se encuentra disponible
        self.patente = patente
        self.carga_max = carga_max
    def subirCargar(self,Object:Carga) -> dict:
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
    def cantidadCargas(self): return len(self.cargas)
    def listaContenido(self):
        lista = []
        for key, values in self.cargas.items():
            lista.append(values.contenido)
        return lista
    def listo_para_salir(self): return (self.pesoTotal()*100)/self.carga_max > 75
    def partir(self):
        if self.listo_para_salir() and self.estado:
            self.estado = False
            self.cargas = dict()
    def llegar(self):
        if not self.estado:
            self.estado = True
    def estado(self):
        print('esta no esta de viaje') if self.estado else print('esta de viaje')
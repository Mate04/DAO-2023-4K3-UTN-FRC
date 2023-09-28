import json

class Pasarela:
    def __init__(self) -> None:
        self.empleados = dict()
        self.contador = self.lecturaJSON('contador.json')
    def agregar(self,Persona:object):
        self.empleados[Persona.legajo] = Persona
    def lecturaJSON(self,archivo:json):
        with open(archivo,'r') as JSON:
            datos= json.load(JSON)
        return datos
    def mostrarSueldoaPagar(self,legajo:int):
        return self.empleados[legajo].neto()
    def contadorTotal(self):
        for empleado in self.empleados:
            self.contador[(type(self.empleados[empleado]).__name__).lower()]+=1
        with open('contador.json', 'w') as archivo_json:
            json.dump(self.contador, archivo_json)
    def sumadorTotal(self):
        return sum(self.empleados.values().neto())

class Persona:
    def __init__(self,legajo:str,nombre:str, apellido:str,sueldoBasico:int) -> None:
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldoBasico = sueldoBasico
    def __str__(self) -> str:
        return '='*20+'\n'+f'legajo: {self.legajo}\nnombre Completo: {self.nombre} {self.apellido}\nsueldo base {self.sueldoBasico}'
    def neto(self):
        pass
    def __add__(self,Clase):
        return self.neto + Clase.neto

class Obrero(Persona):
    def __init__(self, legajo: str, nombre: str, apellido: str, sueldoBasico: int,diasTrabajado:int) -> None:
        super().__init__(legajo, nombre, apellido, sueldoBasico)
        self.diasTrabajado = diasTrabajado
    def neto(self):
        return (self.diasTrabajado * self.sueldoBasico) / 20
    

class Administrador(Persona):
    def __init__(self, legajo: str, nombre: str, apellido: str, sueldoBasico: int,presentismo:bool) -> None:
        super().__init__(legajo, nombre, apellido, sueldoBasico)
        self.presentismo = presentismo
    def neto(self):
        return self.sueldoBasico if not self.presentismo else self.sueldoBasico * 1.13
class Venta(Persona):
    def __init__(self, legajo: str, nombre: str, apellido: str, sueldoBasico: int, importeTotal:int) -> None:
        super().__init__(legajo, nombre, apellido, sueldoBasico)
        self.importeTotal = importeTotal
    def neto(self):
        return self.sueldoBasico + (self.importeTotal * 0.01)
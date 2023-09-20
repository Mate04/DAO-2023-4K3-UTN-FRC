class Pasarela:
    def __init__(self) -> None:
        self.empleados = dict()
    def agregar(self,Persona:object):
        self.empleados[Persona.legajo] = Persona

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
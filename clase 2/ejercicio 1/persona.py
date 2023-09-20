from datetime import datetime
class Persona:
    def __init__(self, dni:int, nombre:str,apellido:str, fecha:datetime) -> None:
        self.dni = dni
        self.nombre= nombre
        self.apellido = apellido
        self.nombreCompleto = f'{nombre} {apellido}'
        self.fecha = fecha
    def __str__(self) -> str:
        return f'{self.nombreCompleto} dni: {self.dni} años: {self.calcularanios()}'
    def calcularanios(self):
        fecha_actual = datetime.now()
        return fecha_actual.year - self.fecha.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha.month, self.fecha.day))
    def __gt__(self, otherPerson:object):
        return 
from Class.Persona import Persona, Obrero, Administrador, Venta,Pasarela
import csv
def main():
    listaTrabajadores = Pasarela
    clase = [Obrero,Administrador,Venta]
    with open('empleados.csv') as empleados:
        reader = csv.reader(empleados,delimiter=';')
        for empleado in reader:
            ob1 = clase[int(empleado[0])-1](int(empleado[1]),str(empleado[2]),str(empleado[3]),int(empleado[4]),int(empleado[5]) if int(empleado[0]) != 2 else bool(empleado[5]))
            listaTrabajadores.agregar(listaTrabajadores,ob1)
main()
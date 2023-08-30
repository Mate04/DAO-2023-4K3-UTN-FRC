import os, csv,json
def main():
    data = lecturaArchivo(os.path.dirname(__file__)+'/'+'personas.csv')
    busquepordocumpento(data,input('archivo que deseas buscar?\n'))
    createJSON(data,os.path.dirname(__file__)+'/'+'personas.json')
def lecturaArchivo(archivo):
    data = {}
    with open(archivo,'r') as archivo:
        archivo = csv.reader(archivo)
        for linea in archivo:
            documento, nombre, apellido, edad = linea
            data.update({documento:{'nombre':nombre,'apellido':apellido,'edad':edad}})
    return data
def busquepordocumpento(data,documento):
    print(data[documento]) if documento in data else print('no se encontro')
def createJSON(data,nombreArchivo='fichero.json'):
    with open(nombreArchivo,'r') as JSON:
        json.dump(data,JSON)
main()
import time,os
import csv
import json
def leer_codigos(nombre_archivo):
    data = {}
    with open(os.path.dirname(__file__)+'/'+nombre_archivo,'r') as archivo:
        reader = csv.reader(archivo,delimiter=';')
        for linea in reader:
            ISO, code,nombre=linea
            data.update({f"{nombre}":{"codigo postal":f"{code}","Codigo ISO":f'{ISO}'}})
    return data

data = leer_codigos('cp.csv')
nombre = input('que deseas buscar: ').upper()
print(data[nombre]) if nombre.upper() in data else print('no se encontro')
with open(os.path.dirname(__file__)+'/'+'fichero.json','w') as JSON:
    json.dump(data,JSON)
'''
Cree un programa que lea de un archivo con dicho JSON e:

1 Imprima los nombres completos (nombre y apellidos) de las personas
que practican el deporte ingresado por el usuario.

2 Imprima los nombres completos (nombre y apellidos) de las personas
que est ́en en un rango de edades dado por el usuario.

3 Cree un JSON de deportes como el siguiente:
  {
    "Ajedrez":["jadiazcoronado",...,"dmlunasol"],
    "Futbol":["jadiazcoronado",...],
    "Gimnasia":["jadiazcoronado,...,"dmlunasol"],
    ...
    "Baloncesto":[...,"dmlunasol"]
  }
'''

import json

def filtrarPorDeporte(deporte):
  with open('personas.json', 'r') as file:
    data = json.load(file)
    for persona in data:
      deportes = data[persona]['deportes']
      if deporte in deportes:
        print(f"{data[persona]['nombres']} {data[persona]['apellidos']}")
  file.close()
    
filtrarPorDeporte('Ajedrez')

def filtrarPorRangoEdades(min, max):
  with open('personas.json', 'r') as file:
    data = json.load(file)
    for persona in data:
      edad = data[persona]['edad']
      if min <= edad <= max:
        print(f"{data[persona]['nombres']} {data[persona]['apellidos']}")
  file.close()

filtrarPorRangoEdades(18, 21)

def deportesPracticados ():
  deportes = {} 
  with open('personas.json', 'r') as file:
    data = json.load(file)
    for persona in data:
      for deporte in data[persona]['deportes']: 
        if deporte not in deportes: 
          deportes[deporte] = []
          deportes[deporte].append(persona)
        else: 
          deportes[deporte].append(persona)
  file.close()
  return deportes

print(deportesPracticados())

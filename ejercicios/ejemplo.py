import json

def filtrarPorRangoEdades(min, max):
  with open('personas.json', 'r') as file:
    data = json.load(file)
    for persona in data:
      edad = data[persona]['edad']
      if min <= edad <= max:
        print(f"{data[persona]['nombres']} {data[persona]['apellidos']}")
  file.close()

filtrarPorRangoEdades(18, 21)

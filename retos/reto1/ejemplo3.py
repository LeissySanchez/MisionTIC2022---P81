# Creado por Leissy Sanchez

prendas = int(input())
Preparacion = (prendas * 1)
Lavado = ((2 * prendas) + 4)
Secado = int(((Preparacion + Lavado)/ 5))

if Secado <= 20:
  valor = "uno"
elif 21 <= Secado <= 30:
  valor = "dos"
elif 31 <= Secado <= 50:
  valor = "tres"
else: 
  valor = "cuatro"
  
print(Preparacion, Lavado, Secado)
print(valor)

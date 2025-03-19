import os
os.system('cls')
### TUPLAS ###
"""
Conjunto de valores constantes
No se pueden modificar los valores, es inmutable
Si se pueden concatenar
"""

mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (22, 1.74, "Nico", "piñera", "Nico")
mi_otra_tupla = (30, 45, 60)
print("Mi tupla:",mi_tupla)
print("Tipo tupla:",type(mi_tupla))

print("Elemento 0:",mi_tupla[0])
print("Elemento -1:",mi_tupla[-1])

nombre = "Nico"
print(f"Cuantas veces aparece: {nombre}: ",mi_tupla.count(nombre))

edad = 22
print(f"Cual es el indice de {edad}:",mi_tupla.index(edad))

mi_tupla_total = mi_tupla+ mi_otra_tupla
print("Suma de tuplas:",mi_tupla_total)

mi_tupla = list(mi_tupla)
print("Cambio a lista:", type(mi_tupla))
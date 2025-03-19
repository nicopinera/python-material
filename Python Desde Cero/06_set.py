import os
os.system('cls')
### Sets ###
"""
Tiene operaciones de conjuntos
"""
mi_set = set()
mi_set = {"c++", "java", "python"}
mi_otro_set = {}

#tipo
print("Tipo set:", type(mi_set))

#definir
mi_otro_set = {"Nico", "Piñera", 22}

#Longitud
print(len(mi_otro_set))

#Agregar elementos
mi_otro_set.add("nicoP") #no es ordenado, se agrega en cualquier lado
print(mi_otro_set)

mi_otro_set.add("nicoP")
print(mi_otro_set) #No admite repetido

#Realizar busqueda
print("Nico" in mi_otro_set)
print("nico" in mi_otro_set)

#remover
mi_otro_set.remove("Nico")
print(mi_otro_set)

#Union
mi_set_total = mi_set.union(mi_otro_set)
print(mi_set_total)

#Limpiar
mi_otro_set.clear()
print(mi_otro_set)

#Diferencia, elimino los elementos
print(mi_set_total.difference(mi_set))


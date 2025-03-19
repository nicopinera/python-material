import os
os.system('cls')
### Diccionarios ###

mi_diccionario = dict()
mi_otro_dicc = {}

print(type(mi_diccionario))

#Definicion
mi_otro_dicc = {"Nombre":"nico", "Apellido":"Piñera","Edad":22}
"Mapa con relacion Clave:Valor para poder buscarlo"

mi_diccionario ={
    "Nombre":"Nico",
    "Apellido" : "Piñera",
    "Edad":22,
    "Lenguaje":{"Python", "C++", "Java"}, #set
    1:1.74
}

print(mi_otro_dicc)
print(mi_diccionario)

#Longitud
print(len(mi_diccionario))
print(len(mi_otro_dicc))

#Acceso por claves a los datos
mi_diccionario["Nombre"] = "NicoP"
print(mi_diccionario["Nombre"])
print(mi_diccionario["Lenguaje"])

#Agregar Valores
mi_diccionario["Apodo"] = "Piñe"
print(mi_diccionario)

#Eliminar un solo elemento
del mi_diccionario["Apodo"]
print(mi_diccionario)

print("Nico" in mi_diccionario) # No busca datos
print("Apellido" in mi_diccionario) # Busca claves

print("\nItems del Diccionario:",mi_diccionario.items()) #Diccionario de items

print("\nLLaves del diccionario",mi_diccionario.keys()) #Llaves en formato lista
claves = mi_diccionario.keys()

print("\nSolo los valores del diccionario:",mi_diccionario.values()) # valores

mi_nuevo_dicc2 = dict.fromkeys(claves,"Sin valores")
mi_nuevo_dicc = dict.fromkeys(("Piso","Altura")) #crea un dicc nuevo sin valores pero con esas claves/llaves
print(mi_nuevo_dicc)
print(mi_nuevo_dicc2)
#5:25:50
    
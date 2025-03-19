import os
os.system('cls')
### Listas ###
"""
Lista de datos u objetos
Tipos de datos compuestos
"""
mi_lista = list()
mi_otra_lista = []
lista_numeros = [3,5,7,9,1,2,5,7,8]

#forma de agrupar datos en forma ordenada
mi_lista = [22, 23, 25, 62, 52, 30 , 30, 17]
mi_otra_lista = [22, 1.74, "Nico", "Piñera"]

print("Mi lista: ",mi_lista)
print("Mi otra lista:", mi_otra_lista)

#Longitud de la lista
print("Longitud de mi lista: ",len(mi_lista))
print("Longitud de mi otra lista: ",len(mi_otra_lista))

print("Tipo lista: ",type(mi_otra_lista))

#Acceso a un valor especifico
print("Posicion 0:",mi_lista[0])
print("Posicion 1:",mi_lista[1])
print("Posicion -1:",mi_lista[-1]) #Recorre la lista de atras hacia adelante
print("Posicion -3:",mi_lista[-3])

#COUNT: Numero de ocurrencia de un valor
print("COUNT(30):",mi_lista.count(30))

#Concatenacion de listas
mi_lista_total = mi_lista + mi_otra_lista
print("Mi lista total: ", mi_lista_total)

#Trabajo con lista
mi_lista.append("Nicolas") #agregar
print(mi_lista)

mi_lista.insert(1,"Azul") #Posicion en donde queres meter un dato
print(mi_lista)

mi_lista.remove(22) #Remover un objeto especifico
print(mi_lista)

elemento_desapilado = mi_lista.pop(2) #saca el dato de esa posicion
print(elemento_desapilado)

mi_lista.reverse()
print("Lista invertida: ", mi_lista)

lista_numeros.sort() # orden por defecto par anumeros
print("Lista ordenada: ", lista_numeros)

mi_nueva_lista = mi_lista.copy()
print(mi_nueva_lista)

del mi_lista[1] # elimina por indice
print(mi_lista)

mi_lista.clear() # borra la lista
print(mi_lista)


import os
os.system('cls')

### Bucles ###
"Bucles - ciclos - loops"
i = 0

#while
while (i<100):
    print(i)
    i += 1
    if(i==15):
        break
else: print("Mi Condicion es >= 10")
"Solo se tiene en python"   

#For: itera segun la cant de elementos de un arreglo
lista_numeros = [3,5,7,9,1,2,5,7,8]
mi_tupla = (22, 1.74, "Nico", "piñera", "Nico")
mi_otro_set = {"Nico", "Piñera", 22}
mi_diccionario ={
    "Nombre":"Nico",
    "Apellido" : "Piñera",
    "Edad":22,
    "Lenguaje":{"Python", "C++", "Java"}, #set
    1:1.74
}
print("\nIteramos los elementos de una lista:")
for elementos in lista_numeros:
    print(elementos)

print("\nIteramos los elementos de una tupla")
for elementos in mi_tupla:
    print(elementos)

print("\nIteramos los elementos de un set")
for elementos in mi_otro_set:
    print(elementos)

print("\nIteramos los elementos de un diccionario")
for elementos in mi_diccionario: #itera en las claves
    print(elementos)
    
for elementos in list(mi_diccionario.values()): #itera en las claves
    print(elementos)
for elementos in mi_diccionario.values(): #itera en las claves
    print(elementos)
    
print("\nTerminado")


import os
os.system('cls') #Limpiar consola
### Condicionales ###
"establece flujo de ejecucion"

mi_condicion = 2*9

    
if(mi_condicion>10 and mi_condicion <20):
    print("Es mayor que 10 y menor que 20")
    
elif(mi_condicion>50):
    print("Es mayor a 50")
    
elif(mi_condicion==0):
    exit
    
else:
    print("Es menor o igual que 10 o mayor que 20")
    
nombre = "" #false
nombre2 = "Nicolas" #true

if not nombre:
    print("Nombre esta vacio")
    
if nombre2:
    print("Mi cadena no es vacia")
    
if(nombre2 == "Nicolas"):
    print("tu Nombre es Nico")

print("La ejecucion termino")
    
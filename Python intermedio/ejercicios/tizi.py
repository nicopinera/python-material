## Librerias
import numpy as np
import random
import os
os.system('cls')

#Numero de muestras
muestras = 20000

#Setteo de Semilla
random.seed(49)

#Variables auxiliares
multiplo_5 = 0 #Multiplos de 5
multiplo_7 = 0 #Multiplos de 7
multiplo_9 = 0 #Multiplos de 9
numeros_pares_men_1500 = 0 
numero_mayor = 0

for i in range(muestras):
    
    numero = random.randint(1,45000)
    ultimo_digito = numero % 10

    #Numero par menor a 15000
    if numero % 2 == 0 and numero < 15000:
        numeros_pares_men_1500 +=1
    
    # Numero Mayor cuyo ultimo digito esta entre 5 y 8
    if numero_mayor < numero and ultimo_digito>=5 and ultimo_digito<8:
        numero_mayor = numero
    
    #Multiplo de 5
    if numero % 5 == 0:
        multiplo_5 +=1
    
    # Multiplo de 7
    if numero % 7 == 0:
        multiplo_7 +=1
    
    #Multiplo de 9
    if numero % 9 == 0:
        multiplo_9 +=1

print("---"*10)
print("EJERCICIO 1:")
print(f"Cantidad de Multiplos de 5: {multiplo_5}")
print(f"Cantidad de Multiplos de 7: {multiplo_7}")
print(f"Cantidad de Multiplos de 9: {multiplo_9}")
print(f"Numero mayor cuyo utlimo digito esta entre 5 y 8 {numero_mayor}")

#Porcentaje de numeros pares mayores a 15000
por_par_15000 =100 * (numeros_pares_men_1500/muestras)
print(f"Porcentaje de Numeros Pares mayores a 15000: {por_par_15000}%")

print("---"*10)
## EJERCICIO 2
print("EJERCICIO 2:")

muestra2 = 25000
random.seed(20220512)

# Variables


for i in range(muestra2):
    num = random.randint(1,4500)




print("---"*10)
print("Terminado")
import os
os.system('cls')
### Operadores ###

print("Suma: 3+4=",3 + 4)
print("Resta: 3-4=",3 - 4)
print("Producto: 3*4=",3 * 4)
print("Divicion: 3/4=",3 / 4)
print("Modulo: 10%2=", 10 % 2) #Modulo = resto de la divicion, para saber si son multiplos
print("Flor Divicion (Aproximacion entera): 10//3=",10 // 3) # flor divicion: se aproxima a un numero entero
print("Exponente: 2**3 o 2^3=",2 ** 3) # Exponente 2^3


print("\n","Hola" + " Python")
print("Hola " * 3)

### Operadores comparativos ###
print("Mayor que: 3>4=",3 > 4)
print("Menor que: 3<4=",3 < 4)
print("Menor o Igual que: 3 <= 4", 3 <= 4 )
print("Mayor o igual que: 3 >= 4", 3 >= 4)
print ("Igual que: 3==4:",3 == 4)
print("Distinto que: 3!=4:",3 != 4)

### Operadores Logicos ###

print((not 3 > 4) and 3 < 4) #Operador logico and
print(3 > 4 or 3 < 4) #Operador logico or
print(not 3 > 4 ) # Operador logico not

#Operadores de pertenencia (in / not in)
# Para saber si algo esta o no
mensaje = "Hola como estas"
print("Hola" in mensaje)
print("o" not in mensaje)
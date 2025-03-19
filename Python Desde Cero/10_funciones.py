import os
os.system('cls')

### Funciones ### 
"Encapsulamos la logica de una funcion especifica"

def primer_funcion():
    i = 0
    while(i < 10):
        print(f"{i+1}: mi primera funcion")
        i += 1

def suma_dos_valores1(valor_uno, valor_dos):
    print(valor_dos+valor_uno)

def suma_dos_valores2(valor_uno, valor_dos):
    c = valor_uno + valor_dos
    return c

def print_nombre(nombre, apellido):
    print(f"Tu nombre es {nombre} y tu apellido es {apellido}")

#Establecer un valor por defecto si no pasan por parametros
def print_nombre_default(nombre, apellido,alias="Sin alias"):
    print(f"Tu nombre es {nombre} y tu apellido es {apellido} y tu alias {alias}")

#Le puedo pasar inf valores por parametros
def print_texts(*text):
    for texts in text:
        print(texts.upper())

primer_funcion()

suma_dos_valores1(12,2)
suma_dos_valores1(33,12)

print(suma_dos_valores2(12,2))
print(suma_dos_valores2(33,12))

#Forma de poner el orden que queiras de los argumentos/parametros
print_nombre(apellido="Piñera",nombre="Nico")

print_nombre_default("nico","Piñera")
print_nombre_default("nico","Piñera","Piñe")

print_texts("Hola")
print_texts("Hola", "Nico", "python", "Funciones")
print("Programa terminado")
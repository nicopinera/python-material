import os
os.system('cls')
### Strings ###

mi_string = "Mi string"
mi_otro_string = "Mi otro string"
print(len(mi_string)) #Longitud de la cadena

salto_de_linea = "Salto\nDe linea"
print(salto_de_linea)

tabulacion= "\tEste es un string con tabulacion"
print(tabulacion)

# Formateo o reemplazo de datos de variables
name = "Nico"
apellido = "Piñera"
edad = 22

#opcion con format
print("Mi nombre es {} {} y mi edad {}".format(name,apellido,edad))

#opcion con %
print("Mi nombre es %s %s y mi edad %d" %(name,apellido,edad))

"""
%s : el primer texto que le pase formateado me lo va a reemplazar ahi
%d : idem pero con enteros
%f : idem pero con float
"""
#Otra opcion mas facil, inferencia de datos
saludo = f"Mi nombre es {name} {apellido} y mi edad {edad}"
print(f"Mi nombre es {name} {apellido} y mi edad {edad}")
print(saludo)

# Desempaquetado de caracteres
lenguaje = "python"
a, b, c, d, e, f= lenguaje
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division
lenguaje_slice = lenguaje[0:3]
print(lenguaje_slice)

lenguaje_slice = lenguaje[0:]
print(lenguaje_slice)

lenguaje_slice = lenguaje[-2]
print(lenguaje_slice)

#Reverse
lenguaje_invertido = lenguaje[::-1]
print(lenguaje_invertido)

#Funciones del sistema
print(lenguaje.capitalize()) #primera letra en mayuscula
print(lenguaje.upper()) #Todo en mayuscula 
print(lenguaje.count("t")) #Cuenta las "t"
print(lenguaje.isnumeric()) # Es un numero?
print(lenguaje.lower()) #Todo minuscula
print(lenguaje.upper().isupper()) #es mayuscula? 

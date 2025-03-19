import os
os.system('cls')
#Variables de python

#Variable string
mi_variable_string = "Mi string variable"
print("Variable de Texto:",mi_variable_string,"\n")

#Variable entera
mi_int_variable = 52
mi_int_variable += 1 #Le sumo uno
print("Variable entera:",mi_int_variable,"\n")

#Variable booleana
mi_bool_variable = False
print("Variable bool:",mi_bool_variable,"\n")

"""
CONCATENACION DE VARIABLES EN PRINT
Print puede recibir 
varios parametros separados por ,
Lo convierte en una sola cadena de texto
"""
print(mi_bool_variable, mi_int_variable, mi_variable_string)
print("Este es el valor de:", mi_bool_variable, "\n")

#Variables en una sola linea
nombre, apellido, alias, edad = "Nico", "Pinera", "Piñe", 22
print("Me llamo:",nombre,". Mi edad es:",edad,". Mi apellido es:", apellido,". Mi alias es:", alias, "\n")

# Funciones del sistema
# STR convierte a string una variable
print("FUNCION STR")
mi_int_a_str = str(mi_int_variable)
print(mi_int_a_str, type(mi_int_a_str), "\n")


#LEN: cuenta la longitud de una cadena de texto
print("FUNCION LEN", "\n", "Longitud de la cadena",len(mi_variable_string))

#INPUT: Ingresa el valor de una variable por consola
nombre_usuario = input("Cual es el nombre de usuaro: ")
contraseña_usuario = input("Ingrese la contraseña: ")
print("Usuario:",nombre_usuario,"\n", "Contraseña: ", contraseña_usuario, "\n")


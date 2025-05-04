import os
os.system('cls')

print("***"*12)
### List Comprehension - Listas comprimidas ###
mi_lista_original = [35,24,62,52,30,30,17]

mi_lista = [i for i in mi_lista_original]
print(mi_lista)
print("***"*12)

mi_lista = [i for i in range(8)]
print(mi_lista)
print("***"*12)

mi_lista = [i+i for i in range(8)]
print(mi_lista)
print("***"*12)


import os
os.system('cls')

### Excepciones ### 

numero1 = 5
numero2 = "1"

#try except
try:
    print(numero1 + numero2)
    print("No hay error")
except:
    print("Error al sumar")
    
# try except else
try:
    print(numero1 + numero2)
    print("No hay error")
except:
    print("Error al sumar")
else: # no se ejecuta si se produce la excepcion
    print("La ejecucion continua correctamente")

#try except else finally
try:
    print(numero1 + numero2)
    print("No hay error")
except:
    print("Error al sumar")
else: # no se ejecuta si se produce la excepcion
    print("La ejecucion continua correctamente")
finally: # se ejecuta siempre
    print("Fin")
    
#excepciones por tipo
try:
    print(numero1 + numero2)
    print("No hay error")
except TypeError: #se ejecuta si el error es de typeError
    print("Error al sumar")

#Capturar la info del error
try:
    print(numero1 + numero2)
    print("No hay error")
except ValueError as error: #Exception: excepcion generica
    print(error)
except Exception as error:
    print(error)
print("Programa terminado")
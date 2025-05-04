"""
Crear una aplicación de consola que permita al usuario realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) entre dos números.
Requisitos:
El programa debe mostrar un menú con las operaciones disponibles:
Sumar
Restar
Multiplicar
Dividir
Salir

El usuario debe elegir una opción del menú ingresando el número correspondiente.
Si elige una operación (1-4), debe:
Ingresar dos números
Ver el resultado de la operación

Si elige la opción 5, el programa debe terminar con un mensaje de despedida.
Validar:
Que la opción del menú sea válida. Que el divisor no sea cero en el caso de la división
"""

def menu():
    print("Bienvenido a la calculadora")
    print("Seleccione una operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b == 0:
        return "Division por cero"
    else:
        return a/b


ejecutar = True
while ejecutar:
    menu()
    opcion = int(input("Operacion a realizar: "))
    if opcion == 1:
        a = int(input("Numero 1:"))
        b = int(input("Numero 2:"))
        resultado = suma(a,b)
        print(f"Resultado de la suma: {resultado}")
        print("-------------------------------------")
    elif opcion == 2:
        a = int(input("Numero 1:"))
        b = int(input("Numero 2:"))
        resultado = resta(a,b)
        print(f"Resultado de la resta: {resultado}")
        print("-------------------------------------")
    elif opcion == 3:
        a = int(input("Numero 1:"))
        b = int(input("Numero 2:"))
        resultado = multiplicar(a,b)
        print(f"Resultado de la multiplicacion: {resultado}")
        print("-------------------------------------")
    elif opcion == 4:
        a = int(input("Numero 1:"))
        b = int(input("Numero 2:"))
        print("Resultado de la division:" , dividir(a,b))
        print("-------------------------------------")
    else:
        ejecutar = False


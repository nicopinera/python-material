import os
os.system('cls')

### Fechas ###

#import datetime #obj y operaciones con fechas
from datetime import datetime

## Funcion para imprimir datos de fechas
def print_date(date):
    print("Año: ",date.year)
    print("Mes: ",date.month)
    print("Dia: ",date.day)
    print("Hora: ",date.hour)
    print("Minuto: ",date.minute)
    print("Segundo: ",date.second)

## Definimos la hora actual
ahora = datetime.now() #tipo date con la info actual
print_date(ahora)
# print("Milisegundos: ",ahora.microsecond)

##  Represenacion unica de un tiempo
print("--"*10)
timestamp = ahora.timestamp() 
print(f"Timestamp: {timestamp}")
print("--"*10)

## Definicion de una fecha puntual
ano_2026 = datetime(2026,1,1)
"Se necesita como minimo año, mes y dia"
#print(f"Fecha Pre establecida: {ano_2026}")
print_date(ano_2026)
print("--"*10)

## Libreria Time
""" 
Nos da funcionalidades sobre el tiempo
Empieza todo en cero
"""
from datetime import time
current_time = time(hour=21, minute=6,second=0)

print("Hora: ", current_time.hour)
print("Minuto: ", current_time.minute)
print("Segundo: ", current_time.second)

print("--"*10)

## Libreria Date
""" 
Fecha, sin tiempo
"""
from datetime import date

current_date = date.today()
print("Año: ", current_date.year)
print("Mes: ", current_date.month)
print("Dia: ", current_date.day)

current_date = date(2030,10,5)
print("Año: ", current_date.year)
print("Mes: ", current_date.month)
print("Dia: ", current_date.day)
print("--"*10)

## Operaciones con fechas


print("--"*10)
print("Programa terminado")
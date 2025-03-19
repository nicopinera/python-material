import os
os.system('cls')

### Fechas ###
import datetime #obj y operaciones con fechas
from datetime import datetime

ahora = datetime.now() #tipo date con la info actual
print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)
print(ahora.microsecond)

timestamp = ahora.timestamp() #represenacion unica de un tiempo
print(timestamp)



print("Programa terminado")
import os
os.system('cls')

### Modulos ### 
"librerias"

import my_module
from my_module import sum # exportar una sola funcion

my_module.mostrar("Hola")
my_module.sum(1,2,3)

sum(3,4) # no hace falta usar  my_module

import math
from math import pi as PI_VALOR
print(math.sqrt(25))
print(math.log(35,2))
print(PI_VALOR)
math.e
import random
print(int(random.random()*100))

print("Programa terminado")
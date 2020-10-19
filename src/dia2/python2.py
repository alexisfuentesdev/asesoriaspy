'''
Palabras reservadas
and 
continue 
else 
for 
import 
not 
raise
assert 
def 
except 
from 
in 
or 
return
break 
del 
exec 
global 
is 
pass 
try
class 
elif 
finally 
if 
lambda 
print 
while
'''

# print("*" * 60)

f = "89h" #Asignación de valor
# int  Podemos convertir cadenas de texto a enteros
# float Para convertir cadenas de texto a flotantes o decimales
# str Para convertir enteros o flotantes a cadenas de texto

# int("4545") -> Entero

# float("34.6") -> Flotante o decimal

# str(3243) -> Cadena de texto


# Bloque IF en Python
if f.isnumeric(): # Validación de si la cadena es un número
    d = int(f) # Cast a número
    print(d * 10) # multiplicar 10
else: # Si no se cumple la validación
    print("\'f\' no es un número")

print("*"*80)    


entero = 60
print(type(entero)) # imprimir el tipo de la variable
print("-"*50)
res = str(entero) # Cast a string o cadena
print(res*10)
print(type(res))

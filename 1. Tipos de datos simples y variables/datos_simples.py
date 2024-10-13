# ---Python reconoce los siguientes tipos de datos---
int
float
str
bool
# ------

# Variables de tipo int
uno = 1
dos = 2
tres = uno + dos
print(tres)

cuatro = int(4)
print(cuatro)
# ------

# Variables de tipo float
num = 4.5 # Se usa el punto para indicar la parte decimal
otro_num = 6.3333
sumatorio = num + uno # float + int = float
print(sumatorio)
otro_sumatorio = num + otro_num
print(otro_sumatorio)

significative_num = float(2.39849284912949812481)
print(significative_num)
# ------

# Variables de tipo str
"Esto es una string que no se ha asignado a ninguna variable"
'Usualmente se usan para la documentación y/o organización del código'

"""
Gracias a las triples comillas puedo escribir en más de una línea.
Esta es la segunda línea
"""

'El salto de carrete sirve para indicar que hay que saltar a la siguiente línea y se define como "\n".'

cadena = "El primer resultado es el 1"
print(cadena)
cadena_dos = f"El primer resultado es el {dos}"
print(cadena_dos)
cadena_tres = f"El primer resultado es el {1 + 2}"
print(cadena_tres)

otra_cadena = str("Hola que tal")
print(otra_cadena)
# ------

# Variables de tipo bool
falso = False # La keyword asociada está capitalizada
verdadero = True

print(verdadero)

booleano = bool(0)
print(booleano)
otro_bool = bool(1)
print(otro_bool)
# ------

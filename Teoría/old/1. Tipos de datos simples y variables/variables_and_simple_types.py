# Declarando algunas variables
a = 15
b = 4
c = a + b

print(c) # La función print muestra por pantalla una evaluación de código y/o valores de variables
print(a + c) # 34
print(1 + 100)

nombre = "Paco"
print("nombre") # Error de principiante
print(nombre)

# Redefiniendo la variable nombre
nombre = "Pedro" # Ahora nombre se reconoce como "Pedro"
print(nombre)

# Python reconoce los siguientes tipos de datos
int   # enteros
float # flotantes
str   # cadenas de texto
bool  # booleanos

# integers (int)
uno = 1
dos = 2
tres = uno + dos
print(tres) # 3

# Otra forma de crear enteros
cuatro = int(4)
print(cuatro) # 4

# floating point numbers (float)
num = 4.5 # Se usa el punto para indicar la parte decimal
otro_num = 6.3333
sumatorio = num + uno # float + int = float
print(sumatorio) # 5.5

otro_sumatorio = num + otro_num
print(otro_sumatorio) # 10.8333

significative_num = float(2.39849284912949812481)
print(significative_num) # No se pierde la precisión

# strings (str)
"Esto es una string que no se ha asignado a ninguna variable"
'Usualmente se usan para la documentación y/o organización del código'

"""
Gracias a las triples comillas puedo escribir en más de una línea.
Esta es la segunda línea
"""

'El salto de carrete sirve para indicar que hay que saltar a la siguiente línea y se define como "\n".'

cadena = "El primer resultado es el 1"
print(cadena)

# f-strings (format strings)
cadena_dos = f"El primer resultado es el {}".format(dos)
print(cadena_dos)

cadena_tres = f"El primer resultado es el {1 + 2}"
print(cadena_tres)

otra_cadena = str("Hola que tal")
print(otra_cadena)

# Variables de tipo bool
falso = False # La keyword asociada está capitalizada
verdadero = True

print(verdadero)

booleano = bool(0)
print(booleano) # False
otro_bool = bool(1)
print(otro_bool) # True

# Concatenación
nombre = "Lucas"
bienvenida = "Hola" + nombre + ", ¿Como estas?"
print(bienvenida)

# Redefiniendo las variables usando f-string
nombre = "Mario"
bienvenida = f"Hola {nombre} ¿Como estas?"
print(bienvenida)

# Ejemplo de uso para el operador del
nombre = "Mario"
del nombre
# print(nombre) # Ya no se reconoce nombre. Se ha liberado la memoria que ocupaba

# Concatenando strings y eliminando datos concatenados
nombre = "Mario" # Definimos una variable nombre
bienvenida = f"Hola {nombre}, ¿Como estas?" # Concatenamos nombre en la variable bienvenida
del nombre # Eliminamos la variable nombre
print(bienvenida) # Ya que bienvenida ya se había definido con la variable nombre sigue el valor dentro de esta.

# Separadores
sinUso = 0 # camelCase
mi_variable = 0 # snake_case
MiClase = 0 # PascalCase
MI_CONSTANTE = 0 # snake_case (mayusc)


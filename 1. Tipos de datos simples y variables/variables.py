# Declarando algunas variables
a = 15
b = 4
c = a + b
# ------

# --- * ---
print(c) # La función print muestra por pantalla una evaluación o valores de variables
print(a + c)
# ---------

# Otro ejemplo
nombre = "Uriel"
print(nombre)
print("nombre") # Error de principiante
# ------

# Redefiniendo la variable nombre
nombre = "Pedro" # Ahora nombre se reconoce como "Pedro"
print(nombre)
# ------

# Uso de números enteros para variables
numero = 10
numero = 10 + 1
print(numero)
# ------

# Caso de uso -> sumar valores a una variable
num = 10
num += 1 # El operador se añade antes del igual para indicar que se sume el valor tras el igual
print(num)
# ------

# Concatenación
nombre = "Lucas"
bienvenida = "Hola" + nombre + "¿Como estas?"
print(bienvenida)
# ------

# Redefiniendo las variables usando f-string
nombre = "Mario"
bienvenida = f"Hola {nombre} ¿Como estas?"
print(bienvenida)
# ------

# Ejemplo de uso para el operador del
nombre = "Mario"
del nombre
# print(nombre) # Ya no se reconoce nombre. Se ha liberado la memoria que ocupaba
# ------

# Concatenando strings y eliminando datos concatenados
nombre = "Mario" # Definimos una variable nombre
bienvenida = f"Hola {nombre} ¿Como estas?" # Concatenamos nombre en la variable bienvenida
del nombre # Eliminamos la variable nombre
print(bienvenida) # Ya que bienvenida ya se había definido con la variable nombre sigue el valor dentro de esta.
# ------

# Almacenando un valor booleano en una variable
condicion = False
# ------

# Separadores
sinUso = 0 # camelCase
mi_variable = 0 # snake_case
MiClase = 0 # PascalCase
MI_CONSTANTE = 0 # snake_case (mayusc)
# ------
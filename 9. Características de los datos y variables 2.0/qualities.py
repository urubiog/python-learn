# --- Datos que reconoce Pytohn ---
str
int
float
list
tuple
set
dict
# ------

# Mutabilidad
lista = [1, 2, 3] # Creación de la lista
print(lista)
lista.append(5) # Mutando lista
print(lista)

diccionario = {
    "name": "Bob",
    "location-x": 4.23423,
    "location-y": 1.32324
}
print(diccionario)
diccionario["time"] = 12.24
print(diccionario)

# Capacidad de anidamiento
list, tuple, dict, set, frozenset # Datos compuestos

# Acceso a elementos
str # str[x]
list # list[x]
set # set[x]
tuple # tuple[x]
dict # dict["key"]

# Inmutabilidad
tupla = (255, 255, 255) # No puede cambiar
tupla_variable = [255, 255, 255],
print(tupla_variable)
tupla_variable[0][1] = 0
print(tupla_variable)

conjunto_congelado = frozenset([1,2,3,4])
conjunto_congelado.append() # No existe el método append para conjuntos congelados

# Iterabilidad
mi_lista = [1, 2, 3, 4, 5]

# Iterar sobre los elementos de la lista utilizando un bucle for
print("Iterando sobre los elementos de la lista:")
for elemento in mi_lista:
    print(elemento)
    
num = 1233123
for digit in num: # No se puede iterar un integer
    print(num)
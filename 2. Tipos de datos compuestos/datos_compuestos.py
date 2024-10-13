# ---Python reconoce los siguientes tipos de datos---
list
tuple
set
dict
# ------

# Tipo de dato lista
lista = ["Manzana", "Pera", "Platano", "Banana"] # Uso de "," como separador
print(lista)
print(lista[0]) # [x] Se usa para acceder a un elemento a partir de su índice o valor dentro de una lista

matriz = [[1, 1], [2, 2]] # matriz es una lista de listas
print(matriz)

print(list("Manzana")) # El resultado es una lista con los caracteres ya que recoge un iterable como argumento

# Redefiniendo el valor de un elemento de la lista
lista[0] = "Naranja" # Accediendo al valor de orden 0
print(lista)
# ------

# Tipo de dato tupla
tupla = ("Manzana" , "Pera" , "Platano" , "Banana") # No mutan

print(tupla[-1]) # Accediendo a valores desde el final

# tupla[2] = "Coco" # Intento de cambiar un valor de una tupla

# Error de principiante
tupla = (25) # No se reconoce como tupla ya que no se ha declarado con ","
print(type(tupla))

tupla = (25, )
tupla = 25,

# ------

# Tipo de dato set
conjunto = {"Manzana" , "Pera" , "Platano" , "Banana"} # Uso de llaves "{}"
print(conjunto)
# ------

# Tipo de dato diccionario
diccionario = {
    "nombre" : "Mario", # llave: valor
    "canal" : "Villegas", # key: value
    "altura" : 1.76,
    "vivo" : True
}

print(diccionario["nombre"]) # Accediendo al valor de la llave nombre

diccionario = dict(uno=1, dos=2, tres=3)
print(diccionario)

diccionario = dict([("uno", 1), ("dos", 2)])
print(diccionario)
# ------

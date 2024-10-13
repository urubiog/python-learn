# Repaso

# Datos compuestos

list # Lista, objeto iterable
["monos", "gorilas", "peces"]

tuple # Tupla, objeto no iterable
("tu padre", "tu madre", "tu abuela")

dict # Diccionario, interable (llaves y valores)
{
    "key": "value",
    "anotherkey": 1
}

set # Conjunto, iterable
{1, 2, 3, 4, 5, 6, ...}

# Iteraciones

lista = list("monos") # creamos la lista con los caracteres de monos
print(lista) # la imprimimos
lista[0] # Iteramos por índice la lista

lista.append("/") # le añadimos elementos
lista.reverse() # La invertimos
lista.sort() # La ordenamos alfabéticamente
lista.remove(lista[0]) # Eliminamos valores
print(lista)

tupla = tuple("hola")
print(tupla)
print(tupla.index("a")) # Buscamos el index de un elemento
print(tupla.count("a")) # Devuelve si existe en la tupla o no

diccionario = {
    "nombre": "Uriel",
    "edad": 16,
    "población": "Barcelona"
}
print(diccionario)
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())

for key, value in diccionario.items():
    print(f"{key}: {value}")
    
print(diccionario.get("nombre")) # Devuelve el valor de una llave
# Si no hay clave, inserta None
print(diccionario.get("edad")) # Devuelve el valor de una llave
# Si no hay clave, inserta la clave None
diccionario.setdefault("curso")
diccionario.get("curso")
print(diccionario)
print(diccionario.pop("edad")) # Remueve la llave y su valor y devuelve el valor
print(diccionario.popitem()) # Remueve todos los items menos el primero y devuelve su key y valor

conjunto = set([1,2,3,4]) # Creamos un conjunto con el objeto lista

print(conjunto)
pares = {2,4,6,8,10}

conjunto.clear() # Vacia el conjunto
conjunto.add(2) # Podemos añadir items
conjunto.remove(2) # Podemos remover items
conjunto.discard(11) # Remueve items, y si no existe no lanza error
print(conjunto)

conjunto = {1,2,3,4,5,6}
print(conjunto.intersection(pares)) # Crea intersecciones entre conjuntos
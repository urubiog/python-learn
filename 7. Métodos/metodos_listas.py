# Métodos de listas
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Crear una nueva lista
lista = [1, 2, 3]

# Añadir un elemento al final de la lista
lista.append(4)

# Copiar una lista
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()

# Contar el número de veces que aparece un elemento en la lista
lista = [1, 2, 2, 3, 3, 3]
contador = lista.count(2) # Contar cuántas veces aparece el elemento 2
contador # Devuelve 2

# Extender la lista agregando los elementos de otra lista al final
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
lista1 # Devuelve [1, 2, 3, 4, 5, 6]

# Encontrar el índice de la primera aparición de un elemento en la lista
indice = lista.index(3) # Índice de la primera aparición del elemento 3
indice # Devuelve 3

# Insertar un elemento en una posición específica de la lista
lista.insert(1, 10)  # Insertar el elemento 10 en el índice 1
lista # Devuelve [1, 10, 2, 2, 3, 3, 3]

# Eliminar y devolver el último elemento de la lista
elemento_eliminado = lista.pop()
elemento_eliminado # Devuelve 3
lista # Devuelve [1, 10, 2, 2, 3, 3]

# Eliminar la primera aparición de un elemento en la lista
lista.remove(2)  # Eliminar la primera aparición del elemento 2
lista # Devuelve [1, 10, 2, 3, 3]

# Invertir el orden de los elementos en la lista
lista.reverse()
lista # Devuelve [3, 3, 2, 10, 1]

# Ordenar los elementos de la lista
lista.sort()
lista # Devuelve [1, 2, 3, 3, 10]

# Eliminar todos los elementos de la lista
lista.clear()
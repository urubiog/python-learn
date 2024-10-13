# Métodos para sets
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

# Crear un conjunto
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}

# Agregar un elemento al conjunto
conjunto1.add(4) # Devuelve {1, 2, 3, 4}

# Eliminar todos los elementos del conjunto
conjunto1.clear() # Devuelve set()

# Copiar un conjunto
conjunto_copia = conjunto2.copy() # Devuelve {2, 3, 4}

# Calcular la diferencia entre dos conjuntos
diferencia = conjunto2.difference(conjunto1) # Devuelve {2, 3, 4}

# Descartar un elemento del conjunto
conjunto2.discard(3) # Devuelve {2, 4}

# Calcular la intersección entre dos conjuntos
interseccion = conjunto1.intersection(conjunto2) # Devuelve {}

# Verificar si un conjunto es disjunto de otro
disyunto = conjunto1.isdisjoint(conjunto2) # Devuelve True

# Verificar si un conjunto es un subconjunto de otro
subconjunto = conjunto1.issubset(conjunto2) # Devuelve False

# Verificar si un conjunto es un superconjunto de otro
superconjunto = conjunto1.issuperset(conjunto2) # Devuelve False

# Eliminar y devolver un elemento arbitrario del conjunto
elemento_eliminado = conjunto2.pop() # Devuelve un elemento arbitrario del conjunto

# Eliminar un elemento específico del conjunto
conjunto2.remove(2) # Devuelve {4}

# Calcular la diferencia simétrica entre dos conjuntos
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2) # Devuelve {1, 4}

# Unir dos conjuntos
union = conjunto1.union(conjunto2) # Devuelve {1, 4}

# Actualizar un conjunto con la unión de sí mismo y otro conjunto
conjunto1.update(conjunto2) # Devuelve {1, 4}
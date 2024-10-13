# Teoría de conjuntos y operaciones
impares = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Comprobando si conjunto2 es un subconjunto de impares
print(conjunto2.issubset(impares))  # Devuelve True

# También se puede comprobar utilizando el operador <
print(conjunto2 < impares)  # Devuelve True

# Para comprobar si impares es un superconjunto de conjunto2
print(impares >= conjunto2)  # Devuelve True

# También se puede utilizar el método issuperset
print(impares.issuperset(conjunto2))  # Devuelve True

# Verificando si hay algún valor en común entre los conjuntos
print(conjunto2.isdisjoint(impares))  # Devuelve False, ya que hay elementos en común

# Intersección
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)

# Unión
A = {1, 2, 3}
B = {4, 5, 6}

print(A.union(B))
print(A | B)

# Uso de frozensets
ingredientes_receta_tortitas = frozenset(["harina", "azúcar", "huevos", "leche"])
ingrediente_receta_tortitas_platano = frozenset(["harina", "azúcar", "huevos", "leche", "platano"])

print(ingredientes_receta_tortitas.issubset(ingrediente_receta_tortitas_platano))

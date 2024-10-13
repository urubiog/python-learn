# Métodos de trabajo para diccionario
['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

diccionario = {
    "nombre" : "Uriel",
    "apellido" : "Rubio",
    "edad" : 16,
    "elemento" : "Hola"
}

# Obtener una lista de todas las claves
diccionario.keys() # Devuelve dict_keys(['nombre', 'apellido', 'edad', 'elemento'])

# Obtener una lista de todos los valores
diccionario.values()

# Obtener una lista de tuplas (clave, valor)
diccionario.items()

# Devuelve el valor de una clave
diccionario.get("elemento")

# Elimina un elemento y obtener su valor a la vez
sixteen = diccionario.pop("edad")

# Actualizar un diccionario con otro diccionario o una lista de pares clave-valor
diccionario.update({"clave1": "valor1", "clave2": "valor2"})
diccionario.update(clave6="valor6")

# Obtener valor
diccionario = {"a": 1, "b": 2, "c": 3}

# Obtener el valor asociado a la clave "a"
valor_a = diccionario.setdefault("a") # Devuelve 1
valor_d = diccionario.setdefault("d", 4) # La clave "d" que no existe así que se añade con el segundo argumento como valor

# Método copy() - Copiar un diccionario
diccionario = {"a": 1, "b": 2, "c": 3}

diccionario_copia = diccionario.copy() # Devuelve {'a': 1, 'b': 2, 'c': 3}

# Método fromkeys() - Crear un diccionario con claves y un valor por defecto
claves = ["a", "b", "c"]
valor_por_defecto = 0
diccionario = dict.fromkeys(claves, valor_por_defecto) # Devuelve {'a': 0, 'b': 0, 'c': 0}

# Método popitem() - Eliminar y devolver un par clave-valor arbitrario
diccionario = {"a": 1, "b": 2, "c": 3}
par_arbitrario = diccionario.popitem()
par_arbitrario  # Devuelve un par clave-valor arbitrario, por ejemplo, ('c', 3)
diccionario  # Devuelve {'a': 1, 'b': 2}, el par clave-valor arbitrario ha sido eliminado del diccionario

# Elimina todos los elementos
diccionario.clear()
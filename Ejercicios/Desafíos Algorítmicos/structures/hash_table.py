# structures/hash_table.py


class HashTable:
    def __init__(self, size: int = 10) -> None:
        """
        Inicializa una tabla hash con un tamaño específico.

        Parámetros:
        - size: El tamaño de la tabla hash (número de buckets).
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        """
        Función hash que convierte una clave en un índice de la tabla.

        Parámetros:
        - key: La clave a la que se le va a aplicar la función hash.

        Retorna:
        - El índice en la tabla donde se almacenará la clave.
        """
        return key % self.size

    def insert(self, key: int, value: any) -> None:
        """
        Inserta una clave y su valor asociado en la tabla hash.

        Parámetros:
        - key: La clave de la entrada.
        - value: El valor asociado a la clave.
        """
        index = self._hash(key)
        # Revisamos si la clave ya está presente, y si es así, actualizamos el valor
        for idx, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][idx] = (key, value)
                return
        # Si no encontramos la clave, agregamos una nueva entrada
        self.table[index].append((key, value))

    def search(self, key: int) -> any:
        """
        Busca un valor asociado a una clave en la tabla hash.

        Parámetros:
        - key: La clave a buscar.

        Retorna:
        - El valor asociado a la clave, o None si no se encuentra.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key: int) -> None:
        """
        Elimina la clave y su valor asociado de la tabla hash.

        Parámetros:
        - key: La clave a eliminar.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self) -> None:
        """
        Imprime la tabla hash completa.
        """
        for i, bucket in enumerate(self.table):
            print(f"Índice {i}: {bucket}")


# Ejercicio 1: Crear una tabla hash e insertar elementos
def crear_tabla_hash(keys: list[int], values: list[any], size: int = 10) -> HashTable:
    """
    Crea una tabla hash e inserta una lista de claves y valores en ella.

    Parámetros:
    - keys: Lista de claves para insertar.
    - values: Lista de valores asociados a las claves.
    - size: El tamaño de la tabla hash (número de buckets).

    Retorna:
    - La tabla hash con los elementos insertados.
    """
    pass


# Ejercicio 2: Buscar un valor en la tabla hash
def buscar_en_tabla_hash(tabla: HashTable, key: int) -> any:
    """
    Busca un valor asociado a una clave en la tabla hash.

    Parámetros:
    - tabla: La tabla hash donde realizar la búsqueda.
    - key: La clave a buscar.

    Retorna:
    - El valor asociado a la clave, o None si no se encuentra.
    """
    pass


# Ejercicio 3: Eliminar un valor de la tabla hash
def eliminar_de_tabla_hash(tabla: HashTable, key: int) -> None:
    """
    Elimina una clave y su valor asociado de la tabla hash.

    Parámetros:
    - tabla: La tabla hash donde eliminar la clave.
    - key: La clave a eliminar.
    """
    pass


# Ejercicio 4: Mostrar el contenido de la tabla hash
def mostrar_tabla_hash(tabla: HashTable) -> None:
    """
    Imprime todo el contenido de la tabla hash.

    Parámetros:
    - tabla: La tabla hash a mostrar.
    """
    pass


# Ejercicio 5: Comprobar si una clave existe en la tabla hash
def existe_en_tabla_hash(tabla: HashTable, key: int) -> bool:
    """
    Verifica si una clave existe en la tabla hash.

    Parámetros:
    - tabla: La tabla hash donde buscar la clave.
    - key: La clave a verificar.

    Retorna:
    - True si la clave existe, de lo contrario False.
    """
    pass

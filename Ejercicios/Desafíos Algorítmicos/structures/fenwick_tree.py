# structures/fenwick_tree.py

class FenwickTree:
    def __init__(self, size: int) -> None:
        """
        Inicializa un Fenwick Tree (Binary Indexed Tree) de tamaño 'size'.
        
        Parámetros:
        - size: Tamaño de la estructura Fenwick Tree.
        """
        self.size = size
        self.tree = [0] * (size + 1)  # Usamos un índice 1 basado para comodidad

    def update(self, index: int, delta: int) -> None:
        """
        Actualiza el valor en el índice 'index' sumando el valor 'delta'.
        
        Parámetros:
        - index: Índice donde se realizará la actualización (1 basado).
        - delta: El valor a agregar en el índice especificado.
        """
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  # Mover al siguiente índice relevante

    def query(self, index: int) -> int:
        """
        Retorna la suma de los valores desde el inicio (índice 1) hasta el índice 'index'.
        
        Parámetros:
        - index: Índice hasta donde se calculará la suma (1 basado).
        
        Retorna:
        - La suma acumulada de los valores desde el índice 1 hasta el índice 'index'.
        """
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  # Mover al padre
        return result

    def range_query(self, left: int, right: int) -> int:
        """
        Retorna la suma de los valores entre los índices 'left' y 'right'.
        
        Parámetros:
        - left: Índice de inicio del rango (1 basado).
        - right: Índice final del rango (1 basado).
        
        Retorna:
        - La suma de los valores entre 'left' y 'right'.
        """
        return self.query(right) - self.query(left - 1)


# Ejercicio 1: Crear un Fenwick Tree desde un arreglo
def crear_fenwick_tree_desde_arreglo(arreglo: list[int]) -> FenwickTree:
    """
    Crea un Fenwick Tree a partir de un arreglo de enteros.
    """
    pass


# Ejercicio 2: Actualizar un valor en el Fenwick Tree
def actualizar_valor(fenwick_tree: FenwickTree, index: int, valor: int) -> None:
    """
    Actualiza el valor en el índice 'index' del Fenwick Tree.
    """
    pass


# Ejercicio 3: Consultar la suma acumulada hasta un índice
def consultar_suma(fenwick_tree: FenwickTree, index: int) -> int:
    """
    Retorna la suma acumulada de los valores desde el índice 1 hasta 'index' en el Fenwick Tree.
    """
    pass


# Ejercicio 4: Consultar la suma en un rango
def consultar_rango(fenwick_tree: FenwickTree, left: int, right: int) -> int:
    """
    Retorna la suma de los valores entre los índices 'left' y 'right' en el Fenwick Tree.
    """
    pass


# Ejercicio 5: Encontrar el valor en el índice específico del Fenwick Tree
def obtener_valor_en_indice(fenwick_tree: FenwickTree, index: int) -> int:
    """
    Encuentra y devuelve el valor almacenado en el índice 'index' del Fenwick Tree.
    """
    pass


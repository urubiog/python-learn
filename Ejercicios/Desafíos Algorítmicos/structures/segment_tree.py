# structures/segment_tree.py

class SegmentTree:
    def __init__(self, data: list[int]) -> None:
        """
        Inicializa el Segment Tree utilizando una lista de datos.
        
        Parámetros:
        - data: Una lista de enteros sobre la cual construir el árbol de segmentos.
        """
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data: list[int]) -> None:
        """
        Construye el Segment Tree basado en los datos proporcionados.
        
        Parámetros:
        - data: La lista de enteros sobre la cual construir el árbol.
        """
        # Insertamos los datos en la mitad del arreglo de segmentos
        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        # Construimos el árbol hacia arriba
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, idx: int, value: int) -> None:
        """
        Actualiza el valor en el índice 'idx' del segmento con un nuevo valor.
        
        Parámetros:
        - idx: El índice del dato a actualizar.
        - value: El nuevo valor para ese índice.
        """
        idx += self.n
        self.tree[idx] = value

        # Actualizamos los valores hacia arriba
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, left: int, right: int) -> int:
        """
        Consulta la suma de los elementos entre los índices 'left' y 'right' (inclusive).
        
        Parámetros:
        - left: El índice izquierdo (inclusive) de la consulta.
        - right: El índice derecho (inclusive) de la consulta.
        
        Retorna:
        - La suma de los elementos en el rango [left, right].
        """
        left += self.n
        right += self.n
        result = 0

        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return result

    def display(self) -> None:
        """
        Muestra el árbol de segmentos (el arreglo de segmentos).
        """
        print(self.tree)

# Ejercicio 1: Construir un Segment Tree a partir de una lista
def construir_segment_tree(data: list[int]) -> SegmentTree:
    """
    Construye un Segment Tree a partir de los datos proporcionados.
    
    Parámetros:
    - data: La lista de enteros sobre la cual construir el árbol.
    
    Retorna:
    - El árbol de segmentos construido.
    """
    pass

# Ejercicio 2: Actualizar un valor en el Segment Tree
def actualizar_segment_tree(segment_tree: SegmentTree, idx: int, value: int) -> None:
    """
    Actualiza el valor en el índice dado del árbol de segmentos con un nuevo valor.
    
    Parámetros:
    - segment_tree: El Segment Tree sobre el cual hacer la actualización.
    - idx: El índice que se debe actualizar.
    - value: El nuevo valor para ese índice.
    """
    pass

# Ejercicio 3: Consultar el rango de un Segment Tree
def consultar_segment_tree(segment_tree: SegmentTree, left: int, right: int) -> int:
    """
    Consulta la suma de los valores en el rango [left, right] del Segment Tree.
    
    Parámetros:
    - segment_tree: El Segment Tree sobre el cual hacer la consulta.
    - left: El índice izquierdo (inclusive) de la consulta.
    - right: El índice derecho (inclusive) de la consulta.
    
    Retorna:
    - La suma de los valores en el rango [left, right].
    """
    pass

# Ejercicio 4: Mostrar el Segment Tree
def mostrar_segment_tree(segment_tree: SegmentTree) -> None:
    """
    Muestra el contenido del Segment Tree.
    
    Parámetros:
    - segment_tree: El Segment Tree a mostrar.
    """
    pass


# structures/heap.py


class Heap:
    def __init__(self, is_min_heap: bool = True) -> None:
        """
        Inicializa un heap (montículo).

        Parámetros:
        - is_min_heap: Si True, el heap será un min-heap (el valor más pequeño está en la raíz).
                        Si False, será un max-heap (el valor más grande está en la raíz).
        """
        self.heap = []
        self.is_min_heap = is_min_heap

    def _parent(self, index: int) -> int:
        """
        Retorna el índice del padre de un nodo.

        Parámetros:
        - index: El índice del nodo actual.

        Retorna:
        - El índice del padre.
        """
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        """
        Retorna el índice del hijo izquierdo de un nodo.

        Parámetros:
        - index: El índice del nodo actual.

        Retorna:
        - El índice del hijo izquierdo.
        """
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        """
        Retorna el índice del hijo derecho de un nodo.

        Parámetros:
        - index: El índice del nodo actual.

        Retorna:
        - El índice del hijo derecho.
        """
        return 2 * index + 2

    def _heapify_up(self, index: int) -> None:
        """
        Mantiene la propiedad del heap subiendo el elemento en el índice adecuado.

        Parámetros:
        - index: El índice del nodo actual.
        """
        while index > 0:
            parent_index = self._parent(index)
            if (self.is_min_heap and self.heap[index] < self.heap[parent_index]) or (
                not self.is_min_heap and self.heap[index] > self.heap[parent_index]
            ):
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def _heapify_down(self, index: int) -> None:
        """
        Mantiene la propiedad del heap bajando el elemento en el índice adecuado.

        Parámetros:
        - index: El índice del nodo actual.
        """
        size = len(self.heap)
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            smallest_or_largest = index

            if left < size and (
                (self.is_min_heap and self.heap[left] < self.heap[smallest_or_largest])
                or (
                    not self.is_min_heap
                    and self.heap[left] > self.heap[smallest_or_largest]
                )
            ):
                smallest_or_largest = left
            if right < size and (
                (self.is_min_heap and self.heap[right] < self.heap[smallest_or_largest])
                or (
                    not self.is_min_heap
                    and self.heap[right] > self.heap[smallest_or_largest]
                )
            ):
                smallest_or_largest = right

            if smallest_or_largest != index:
                self.heap[index], self.heap[smallest_or_largest] = (
                    self.heap[smallest_or_largest],
                    self.heap[index],
                )
                index = smallest_or_largest
            else:
                break

    def insert(self, value: int) -> None:
        """
        Inserta un valor en el heap.

        Parámetros:
        - value: El valor a insertar en el heap.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) -> int:
        """
        Elimina y retorna el valor raíz del heap (el más pequeño en un min-heap o el más grande en un max-heap).

        Retorna:
        - El valor raíz (el valor más pequeño o más grande dependiendo del tipo de heap).
        """
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")

        root_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)

        return root_value

    def peek(self) -> int:
        """
        Retorna el valor raíz sin eliminarlo.

        Retorna:
        - El valor raíz del heap (el valor más pequeño o más grande dependiendo del tipo de heap).
        """
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")

        return self.heap[0]

    def display(self) -> None:
        """
        Imprime el contenido del heap.
        """
        print(self.heap)


# Ejercicio 1: Crear un heap desde una lista
def crear_heap_desde_lista(lista: list[int], is_min_heap: bool = True) -> Heap:
    """
    Crea un heap desde una lista de números.

    Parámetros:
    - lista: Lista de números a insertar en el heap.
    - is_min_heap: Si True, crea un min-heap, si False, crea un max-heap.

    Retorna:
    - Un objeto Heap con los elementos de la lista.
    """
    pass


# Ejercicio 2: Obtener el valor mínimo o máximo
def obtener_minimo_o_maximo(heap: Heap) -> int:
    """
    Obtiene el valor mínimo en un min-heap o el valor máximo en un max-heap sin eliminarlo.

    Parámetros:
    - heap: El heap del cual obtener el valor mínimo o máximo.

    Retorna:
    - El valor mínimo o máximo del heap.
    """
    pass


# Ejercicio 3: Extraer el valor mínimo o máximo
def extraer_minimo_o_maximo(heap: Heap) -> int:
    """
    Extrae el valor mínimo de un min-heap o el valor máximo de un max-heap.

    Parámetros:
    - heap: El heap del cual extraer el valor.

    Retorna:
    - El valor mínimo o máximo extraído del heap.
    """
    pass


# Ejercicio 4: Insertar un valor en el heap
def insertar_en_heap(heap: Heap, value: int) -> None:
    """
    Inserta un valor en el heap.

    Parámetros:
    - heap: El heap donde insertar el valor.
    - value: El valor a insertar.
    """
    pass


# Ejercicio 5: Mostrar el heap
def mostrar_heap(heap: Heap) -> None:
    """
    Muestra el contenido del heap.

    Parámetros:
    - heap: El heap a mostrar.
    """
    pass

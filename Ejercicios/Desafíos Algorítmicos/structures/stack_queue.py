# structures/stack_queue.py

class Stack:
    def __init__(self) -> None:
        """
        Inicializa una pila vacía.
        La pila se implementa usando una lista interna.
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Verifica si la pila está vacía.
        
        Retorna:
        - True si la pila está vacía, False si no lo está.
        """
        return len(self.items) == 0

    def push(self, item: int | float) -> None:
        """
        Agrega un elemento a la parte superior de la pila.
        
        Parámetros:
        - item: El elemento a agregar.
        """
        self.items.append(item)

    def pop(self) -> int | float | None:
        """
        Elimina y devuelve el elemento en la parte superior de la pila.
        
        Retorna:
        - El elemento eliminado si la pila no está vacía, None si lo está.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> int | float | None:
        """
        Devuelve el elemento en la parte superior de la pila sin eliminarlo.
        
        Retorna:
        - El elemento en la parte superior si la pila no está vacía, None si lo está.
        """
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self) -> int:
        """
        Devuelve el número de elementos en la pila.
        
        Retorna:
        - El tamaño de la pila.
        """
        return len(self.items)


class Queue:
    def __init__(self) -> None:
        """
        Inicializa una cola vacía.
        La cola se implementa usando una lista interna.
        """
        self.items = []

    def is_empty(self) -> bool:
        """
        Verifica si la cola está vacía.
        
        Retorna:
        - True si la cola está vacía, False si no lo está.
        """
        return len(self.items) == 0

    def enqueue(self, item: int | float) -> None:
        """
        Agrega un elemento al final de la cola.
        
        Parámetros:
        - item: El elemento a agregar.
        """
        self.items.append(item)

    def dequeue(self) -> int | float | None:
        """
        Elimina y devuelve el primer elemento de la cola.
        
        Retorna:
        - El primer elemento si la cola no está vacía, None si lo está.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self) -> int | float | None:
        """
        Devuelve el primer elemento de la cola sin eliminarlo.
        
        Retorna:
        - El primer elemento si la cola no está vacía, None si lo está.
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self) -> int:
        """
        Devuelve el número de elementos en la cola.
        
        Retorna:
        - El tamaño de la cola.
        """
        return len(self.items)

# Ejercicio 1: Implementar una pila
def implementar_pila() -> Stack:
    """
    Crea una pila vacía e implementa las operaciones básicas (push, pop, peek, is_empty, size).
    
    Retorna:
    - La pila creada.
    """
    pass

# Ejercicio 2: Implementar una cola
def implementar_cola() -> Queue:
    """
    Crea una cola vacía e implementa las operaciones básicas (enqueue, dequeue, peek, is_empty, size).
    
    Retorna:
    - La cola creada.
    """
    pass

# Ejercicio 3: Verificar si una secuencia de paréntesis es válida
def verificar_parentesis(expresion: str) -> bool:
    """
    Verifica si una secuencia de paréntesis está balanceada.
    
    Parámetros:
    - expresion: Una cadena que contiene solo paréntesis ().
    
    Retorna:
    - True si los paréntesis están balanceados, False si no lo están.
    """
    pass

# Ejercicio 4: Implementar cola usando dos pilas
def cola_con_pilas() -> Queue:
    """
    Implementa una cola utilizando dos pilas.
    
    Retorna:
    - La cola implementada usando dos pilas.
    """
    pass

# Ejercicio 5: Invertir una lista usando una pila
def invertir_lista(lista: list[int | float]) -> list[int | float]:
    """
    Invierte el orden de los elementos en una lista usando una pila.
    
    Parámetros:
    - lista: Una lista de enteros o flotantes a invertir.
    
    Retorna:
    - La lista invertida.
    """
    pass


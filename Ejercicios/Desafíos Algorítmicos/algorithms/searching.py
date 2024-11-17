# algorithms/searching.py

def linear_search(arr, target):
    """
    Realiza una búsqueda lineal en una lista. 
    Este algoritmo recorre cada elemento de la lista de manera secuencial 
    para encontrar el valor objetivo.

    Complejidad temporal: O(n), donde n es el número de elementos en la lista.
    Esto se debe a que, en el peor de los casos, el algoritmo tiene que recorrer toda la lista.
    
    Parámetros:
    - arr: Lista de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def binary_search(arr, target):
    """
    Realiza una búsqueda binaria en una lista ordenada. 
    El algoritmo divide repetidamente el espacio de búsqueda a la mitad, 
    comparando el valor objetivo con el elemento del medio.

    Complejidad temporal: O(log n), donde n es el número de elementos en la lista.
    Esto se debe a que el tamaño del espacio de búsqueda se reduce a la mitad en cada paso.
    
    Parámetros:
    - arr: Lista ordenada de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def fibonacci_search(arr, target):
    """
    Realiza una búsqueda de Fibonacci en una lista ordenada. 
    El algoritmo utiliza los números de Fibonacci para dividir la lista y 
    encontrar el valor objetivo.

    Complejidad temporal: O(log n), donde n es el número de elementos en la lista.
    Es útil cuando se tiene una lista ordenada y el algoritmo binario no es aplicable.

    Parámetros:
    - arr: Lista ordenada de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def interpolation_search(arr, target):
    """
    Realiza una búsqueda de interpolación, que es una versión mejorada de la búsqueda binaria.
    Utiliza la fórmula de interpolación para hacer una estimación del índice del valor objetivo 
    en función de su valor y el rango de los valores en la lista.

    Complejidad temporal: O(log log n), en el mejor de los casos. 
    Sin embargo, en el peor de los casos, puede llegar a O(n) si los datos están distribuidos de forma no uniforme.
    
    Parámetros:
    - arr: Lista ordenada de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def exponential_search(arr, target):
    """
    Realiza una búsqueda exponencial en una lista ordenada. 
    El algoritmo primero encuentra el rango en el que se podría encontrar el objetivo 
    mediante una expansión exponencial, y luego realiza una búsqueda binaria en ese rango.

    Complejidad temporal: O(log n), donde n es el número de elementos en la lista.
    Es eficiente para listas muy grandes.
    
    Parámetros:
    - arr: Lista ordenada de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def bst_search(root, target):
    """
    Realiza una búsqueda en un Árbol de Búsqueda Binaria (BST).
    El algoritmo compara el valor objetivo con el nodo actual y decide si se debe 
    continuar en el subárbol izquierdo o derecho basado en la comparación.

    Complejidad temporal: O(log n) en promedio, pero O(n) en el peor de los casos si el árbol es desequilibrado.
    
    Parámetros:
    - root: El nodo raíz del árbol de búsqueda binaria.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El nodo que contiene el valor objetivo si se encuentra, o None si no se encuentra.
    """
    pass

def bfs(graph, start, target):
    """
    Realiza una búsqueda en anchura (BFS) en un grafo.
    El algoritmo explora los nodos vecinos primero antes de moverse a los nodos de nivel más profundo.

    Complejidad temporal: O(V + E), donde V es el número de vértices y E es el número de aristas.
    
    Parámetros:
    - graph: El grafo representado como un diccionario de listas de adyacencia.
    - start: El nodo inicial para comenzar la búsqueda.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El nodo objetivo si se encuentra, o None si no se encuentra.
    """
    pass

def dfs(graph, start, target):
    """
    Realiza una búsqueda en profundidad (DFS) en un grafo.
    El algoritmo explora un camino desde el nodo inicial hasta que encuentra el objetivo o se queda sin caminos.

    Complejidad temporal: O(V + E), donde V es el número de vértices y E es el número de aristas.
    
    Parámetros:
    - graph: El grafo representado como un diccionario de listas de adyacencia.
    - start: El nodo inicial para comenzar la búsqueda.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El nodo objetivo si se encuentra, o None si no se encuentra.
    """
    pass

def hash_search(hash_table, key):
    """
    Realiza una búsqueda en una tabla hash.
    El algoritmo utiliza la función hash para mapear la clave y buscar rápidamente el valor asociado.

    Complejidad temporal: O(1) en promedio, O(n) en el peor de los casos si hay colisiones.
    
    Parámetros:
    - hash_table: La tabla hash representada como un diccionario.
    - key: La clave cuyo valor asociado se desea encontrar.
    
    Retorna:
    - El valor asociado a la clave si se encuentra, o None si no se encuentra.
    """
    pass

def jump_search(arr, target):
    """
    Realiza una búsqueda saltada en una lista ordenada. 
    El algoritmo salta a intervalos fijos y luego realiza una búsqueda lineal dentro 
    del bloque encontrado.

    Complejidad temporal: O(√n), donde n es el número de elementos en la lista.
    El algoritmo tiene un comportamiento mejorado sobre la búsqueda lineal en listas grandes.
    
    Parámetros:
    - arr: Lista ordenada de elementos en los que se buscará.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El índice del valor objetivo si se encuentra, o -1 si no se encuentra.
    """
    pass

def avl_search(root, target):
    """
    Realiza una búsqueda en un Árbol AVL (Árbol de Búsqueda Balanceado).
    Similar a la búsqueda en un árbol binario, pero garantizando un equilibrio en el árbol para mantener la eficiencia.

    Complejidad temporal: O(log n) en el mejor de los casos debido al equilibrio del árbol.
    
    Parámetros:
    - root: El nodo raíz del árbol AVL.
    - target: El valor que se desea encontrar.
    
    Retorna:
    - El nodo que contiene el valor objetivo si se encuentra, o None si no se encuentra.
    """
    pass


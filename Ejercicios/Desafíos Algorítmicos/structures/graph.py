# structures/graph.py

from collections import deque


class Graph:
    def __init__(self, directed: bool = False) -> None:
        """
        Inicializa un grafo, que puede ser dirigido o no dirigido.

        Parámetros:
        - directed: Si es True, el grafo será dirigido, si es False será no dirigido.
        """
        self.directed = directed
        self.graph = {}

    def add_vertex(self, vertex: int) -> None:
        """
        Añade un vértice al grafo.

        Parámetros:
        - vertex: El vértice a añadir al grafo.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u: int, v: int) -> None:
        """
        Añade una arista entre los vértices u y v. Si el grafo es no dirigido, se añade en ambos sentidos.

        Parámetros:
        - u: El primer vértice de la arista.
        - v: El segundo vértice de la arista.
        """
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)

        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def bfs(self, start: int) -> list[int]:
        """
        Realiza una búsqueda en anchura (BFS) en el grafo a partir del vértice 'start'.

        Parámetros:
        - start: El vértice desde donde comienza la búsqueda.

        Retorna:
        - Una lista con el orden en que se visitaron los vértices.
        """
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order

    def dfs(self, start: int) -> list[int]:
        """
        Realiza una búsqueda en profundidad (DFS) en el grafo a partir del vértice 'start'.

        Parámetros:
        - start: El vértice desde donde comienza la búsqueda.

        Retorna:
        - Una lista con el orden en que se visitaron los vértices.
        """
        visited = set()
        order = []

        def dfs_recursive(v):
            visited.add(v)
            order.append(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return order

    def has_path(self, start: int, end: int) -> bool:
        """
        Determina si existe un camino entre los vértices 'start' y 'end' utilizando BFS.

        Parámetros:
        - start: El vértice de inicio.
        - end: El vértice de destino.

        Retorna:
        - True si hay un camino entre 'start' y 'end', de lo contrario False.
        """
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex == end:
                return True
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return False


# Ejercicio 1: Crear un grafo a partir de una lista de aristas
def crear_grafo(aristas: list[tuple[int, int]], directed: bool = False) -> Graph:
    """
    Crea un grafo a partir de una lista de aristas.

    Parámetros:
    - aristas: Lista de tuplas donde cada tupla contiene dos vértices (u, v) representando una arista entre u y v.
    - directed: Si el grafo es dirigido o no dirigido.

    Retorna:
    - El grafo creado con las aristas proporcionadas.
    """
    pass


# Ejercicio 2: Imprimir los vértices y las aristas del grafo
def imprimir_grafo(grafo: Graph) -> None:
    """
    Imprime los vértices y sus aristas en el grafo.

    Parámetros:
    - grafo: El grafo a imprimir.
    """
    pass


# Ejercicio 3: Verificar si existe un camino entre dos vértices
def verificar_camino(grafo: Graph, start: int, end: int) -> bool:
    """
    Verifica si existe un camino entre los vértices 'start' y 'end' usando BFS.

    Parámetros:
    - grafo: El grafo en el que buscar el camino.
    - start: El vértice de inicio.
    - end: El vértice de destino.

    Retorna:
    - True si existe un camino entre 'start' y 'end', de lo contrario False.
    """
    pass


# Ejercicio 4: Encontrar el recorrido BFS de un grafo
def recorrido_bfs(grafo: Graph, start: int) -> list[int]:
    """
    Encuentra el recorrido en anchura (BFS) de un grafo desde el vértice 'start'.

    Parámetros:
    - grafo: El grafo en el que realizar la búsqueda.
    - start: El vértice desde el cual iniciar la búsqueda.

    Retorna:
    - Una lista con los vértices visitados en el recorrido BFS.
    """
    pass


# Ejercicio 5: Encontrar el recorrido DFS de un grafo
def recorrido_dfs(grafo: Graph, start: int) -> list[int]:
    """
    Encuentra el recorrido en profundidad (DFS) de un grafo desde el vértice 'start'.

    Parámetros:
    - grafo: El grafo en el que realizar la búsqueda.
    - start: El vértice desde el cual iniciar la búsqueda.

    Retorna:
    - Una lista con los vértices visitados en el recorrido DFS.
    """
    pass

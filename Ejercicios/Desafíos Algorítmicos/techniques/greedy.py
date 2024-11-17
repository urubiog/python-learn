# techniques/greedy.py


# Ejercicio 1: Problema del cambio de monedas (Coin Change Problem - Greedy)
def cambio_monedas_greedy(monedas: list[int], cantidad: int) -> int:
    """
    Resuelve el problema del cambio de monedas utilizando la estrategia codiciosa.
    Dado un conjunto de monedas con denominaciones, encuentra el número mínimo de monedas necesarias
    para hacer un cambio a una cantidad dada. La estrategia codiciosa elige las monedas más grandes posibles
    primero.

    Parámetros:
    - monedas: Una lista de denominaciones de monedas disponibles (ordenadas de mayor a menor).
    - cantidad: El valor objetivo que debe alcanzarse con las monedas.

    Retorna:
    - El número mínimo de monedas necesarias para alcanzar la cantidad, o -1 si no es posible.
    """
    pass


# Ejercicio 2: Actividades (Activity Selection Problem)
def seleccion_actividades(actividades: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Resuelve el problema de selección de actividades utilizando la estrategia codiciosa.
    Dado un conjunto de actividades con horarios de inicio y fin, selecciona el número máximo de actividades
    que se pueden realizar sin que se solapen.

    Parámetros:
    - actividades: Una lista de tuplas (inicio, fin) que representan el horario de cada actividad.

    Retorna:
    - Una lista de tuplas (inicio, fin) representando las actividades seleccionadas.
    """
    pass


# Ejercicio 3: Kruskal (Árbol de expansión mínima - Minimum Spanning Tree)
def kruskal(
    vertices: int, aristas: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    """
    Resuelve el problema de encontrar el árbol de expansión mínima de un grafo no dirigido utilizando el algoritmo de Kruskal.
    El algoritmo codicioso selecciona las aristas de menor peso, asegurando que no se formen ciclos.

    Parámetros:
    - vertices: El número de vértices del grafo.
    - aristas: Una lista de aristas, cada una representada como una tupla (peso, u, v) donde u y v son los vértices
               conectados por la arista y peso es su valor.

    Retorna:
    - Una lista de aristas que forman el árbol de expansión mínima.
    """
    pass


# Ejercicio 4: Dijkstra (Camino más corto - Shortest Path)
def dijkstra(grafo: list[list[int]], inicio: int) -> list[int]:
    """
    Resuelve el problema del camino más corto en un grafo ponderado utilizando el algoritmo de Dijkstra.
    El algoritmo codicioso selecciona el vértice con la distancia más corta que aún no ha sido procesado
    y actualiza las distancias a los vértices vecinos.

    Parámetros:
    - grafo: Una matriz de adyacencia que representa el grafo ponderado.
    - inicio: El vértice de inicio desde el cual se calculan los caminos más cortos.

    Retorna:
    - Una lista de distancias mínimas desde el vértice de inicio a todos los demás vértices.
    """
    pass


# Ejercicio 5: Huffman Coding (Codificación de Huffman)
def codificacion_huffman(simbolos: list[tuple[str, int]]) -> dict[str, str]:
    """
    Resuelve el problema de la codificación de Huffman utilizando el algoritmo codicioso.
    Dado un conjunto de símbolos con sus frecuencias, construye un árbol de Huffman y asigna a cada símbolo
    una secuencia binaria de longitud variable para la compresión de datos.

    Parámetros:
    - simbolos: Una lista de tuplas (símbolo, frecuencia), donde símbolo es el caracter a codificar y frecuencia es su frecuencia.

    Retorna:
    - Un diccionario que mapea cada símbolo a su código Huffman.
    """
    pass


# Ejercicio 6: Problema de la Franja (Fractional Knapsack Problem)
def mochila_fraccionada(capacidad: int, objetos: list[tuple[int, int]]) -> float:
    """
    Resuelve el problema de la mochila fraccionada utilizando el algoritmo codicioso.
    Dado un conjunto de objetos con un peso y un valor, y una mochila con una capacidad limitada,
    determina el valor máximo que se puede obtener al tomar fracciones de los objetos.

    Parámetros:
    - capacidad: La capacidad máxima de la mochila.
    - objetos: Una lista de tuplas (peso, valor) de cada objeto.

    Retorna:
    - El valor máximo que se puede obtener sin exceder la capacidad de la mochila.
    """
    pass


# Ejercicio 7: Selección de actividad con el máximo beneficio (Job Sequencing Problem)
def secuenciacion_trabajos(
    trabajos: list[tuple[int, int, int]], n: int
) -> list[tuple[int, int]]:
    """
    Resuelve el problema de secuenciación de trabajos con el máximo beneficio utilizando la estrategia codiciosa.
    Dado un conjunto de trabajos, cada uno con un beneficio y una fecha de vencimiento, selecciona los trabajos
    que maximicen el beneficio total sin que se solapen.

    Parámetros:
    - trabajos: Una lista de tuplas (beneficio, duración, vencimiento) que representan cada trabajo.
    - n: El número total de trabajos.

    Retorna:
    - Una lista de trabajos seleccionados (beneficio, duración, vencimiento) que maximicen el beneficio.
    """
    pass


# Ejercicio 8: Algoritmo de selección de intervalo (Interval Scheduling Maximization)
def seleccion_intervalos(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Resuelve el problema de la selección de intervalos con el objetivo de maximizar el número de intervalos no solapados
    utilizando la estrategia codiciosa. El algoritmo selecciona los intervalos de manera que no se solapen.

    Parámetros:
    - intervalos: Una lista de tuplas (inicio, fin) que representan los intervalos.

    Retorna:
    - Una lista de tuplas (inicio, fin) representando los intervalos seleccionados.
    """
    pass

# techniques/monotonic_stack.py


# Ejercicio 1: La siguiente mayor temperatura (Next Greater Element)
def siguiente_mayor_temperatura(temperaturas: list[int]) -> list[int]:
    """
    Resuelve el problema de encontrar la siguiente mayor temperatura para cada día utilizando una pila monótona.
    Dado un conjunto de temperaturas, para cada día, se debe encontrar la próxima fecha en la que se alcanzará una temperatura más alta.

    Parámetros:
    - temperaturas: Una lista de temperaturas diarias.

    Retorna:
    - Una lista de enteros, donde cada elemento es el número de días hasta la próxima temperatura mayor,
      o -1 si no existe una temperatura mayor en el futuro.
    """
    pass


# Ejercicio 2: La siguiente menor temperatura (Next Smaller Element)
def siguiente_menor_temperatura(temperaturas: list[int]) -> list[int]:
    """
    Resuelve el problema de encontrar la siguiente menor temperatura para cada día utilizando una pila monótona.
    Dado un conjunto de temperaturas, para cada día, se debe encontrar la próxima fecha en la que se alcanzará una temperatura más baja.

    Parámetros:
    - temperaturas: Una lista de temperaturas diarias.

    Retorna:
    - Una lista de enteros, donde cada elemento es el número de días hasta la próxima temperatura menor,
      o -1 si no existe una temperatura menor en el futuro.
    """
    pass


# Ejercicio 3: El menor elemento a la izquierda (Previous Smaller Element)
def menor_elemento_izquierda(arr: list[int]) -> list[int]:
    """
    Resuelve el problema de encontrar el menor elemento a la izquierda de cada elemento en una lista utilizando una pila monótona.
    Para cada elemento en la lista, se debe encontrar el primer número que sea menor al elemento y esté a la izquierda.

    Parámetros:
    - arr: Una lista de números enteros.

    Retorna:
    - Una lista de enteros, donde cada elemento es el menor número a la izquierda del número en la misma posición en arr,
      o -1 si no existe un número menor a la izquierda.
    """
    pass


# Ejercicio 4: Longitud de la subsecuencia más larga de paréntesis balanceados
def subsecuencia_balanceada_parentesis(s: str) -> int:
    """
    Resuelve el problema de encontrar la longitud de la subsecuencia más larga de paréntesis balanceados utilizando una pila monótona.
    Se debe encontrar la subsecuencia de paréntesis que sea válida y tenga la mayor longitud posible en una cadena dada.

    Parámetros:
    - s: Una cadena de paréntesis (solo contiene '(' y ')').

    Retorna:
    - Un entero que representa la longitud de la subsecuencia más larga de paréntesis balanceados.
    """
    pass


# Ejercicio 5: Problema de los elementos máximos en una ventana deslizante (Sliding Window Maximum)
def maximo_en_ventana_deslizante(arr: list[int], k: int) -> list[int]:
    """
    Resuelve el problema de encontrar el valor máximo en cada ventana de tamaño k en una lista utilizando una pila monótona.
    Dado un arreglo y un tamaño de ventana k, encuentra el valor máximo dentro de cada ventana deslizante.

    Parámetros:
    - arr: Una lista de números enteros.
    - k: El tamaño de la ventana deslizante.

    Retorna:
    - Una lista de enteros, donde cada elemento es el valor máximo dentro de la ventana deslizante correspondiente.
    """
    pass


# Ejercicio 6: El problema de las áreas de barras más grandes (Largest Rectangle in Histogram)
def area_maxima_histograma(heights: list[int]) -> int:
    """
    Resuelve el problema de encontrar el área del rectángulo más grande que se puede formar en un histograma utilizando una pila monótona.
    Dado un histograma representado por alturas de barras, encuentra el área máxima del rectángulo que se puede formar con las barras.

    Parámetros:
    - heights: Una lista de enteros que representa las alturas de las barras del histograma.

    Retorna:
    - El área máxima del rectángulo que se puede formar en el histograma.
    """
    pass


# Ejercicio 7: El problema de los índices más cercanos
def indices_mas_cercanos(arr: list[int]) -> list[int]:
    """
    Resuelve el problema de encontrar el índice más cercano de un número mayor para cada elemento en la lista utilizando una pila monótona.
    Para cada elemento, se debe encontrar el índice del siguiente número mayor que se encuentre a la derecha del elemento.

    Parámetros:
    - arr: Una lista de números enteros.

    Retorna:
    - Una lista de enteros, donde cada elemento es el índice del siguiente número mayor en la lista,
      o -1 si no existe tal número mayor.
    """
    pass


# Ejercicio 8: Resolver el problema de la validación de paréntesis
def validar_parentesis(s: str) -> bool:
    """
    Resuelve el problema de validar si una secuencia de paréntesis es válida utilizando una pila.
    Una secuencia de paréntesis es válida si los paréntesis están correctamente balanceados y cerrados.

    Parámetros:
    - s: Una cadena de paréntesis (solo contiene '(', ')', '{', '}', '[' y ']').

    Retorna:
    - True si la secuencia de paréntesis es válida, de lo contrario False.
    """
    pass

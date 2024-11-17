# techniques/recursion.py

# Ejercicio 1: Factorial de un número
def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo utilizando recursión.
    
    Parámetros:
    - n: Un número entero no negativo.
    
    Retorna:
    - El factorial de n (n!).
    """
    pass


# Ejercicio 2: Serie de Fibonacci
def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número en la secuencia de Fibonacci utilizando recursión.
    La secuencia de Fibonacci está definida como:
    - fib(0) = 0
    - fib(1) = 1
    - fib(n) = fib(n-1) + fib(n-2) para n > 1.
    
    Parámetros:
    - n: El índice de la secuencia de Fibonacci.
    
    Retorna:
    - El n-ésimo número en la secuencia de Fibonacci.
    """
    pass


# Ejercicio 3: Potencia de un número
def potencia(base: int, exponente: int) -> int:
    """
    Calcula la potencia de un número (base^exponente) utilizando recursión.
    
    Parámetros:
    - base: El número base.
    - exponente: El exponente al que se va a elevar la base.
    
    Retorna:
    - El resultado de base^exponente.
    """
    pass


# Ejercicio 4: Búsqueda binaria recursiva
def busqueda_binaria(arr: list[int], objetivo: int, inicio: int = 0, fin: int = None) -> int:
    """
    Realiza una búsqueda binaria recursiva para encontrar el índice de un valor en un arreglo ordenado.
    
    Parámetros:
    - arr: Un arreglo de números enteros ordenados de menor a mayor.
    - objetivo: El valor que se busca en el arreglo.
    - inicio: El índice de inicio del subarreglo a buscar.
    - fin: El índice final del subarreglo a buscar.
    
    Retorna:
    - El índice de objetivo en arr si se encuentra, de lo contrario -1.
    """
    pass


# Ejercicio 5: Suma de los elementos de una lista
def suma_lista(arr: list[int]) -> int:
    """
    Calcula la suma de los elementos de una lista utilizando recursión.
    
    Parámetros:
    - arr: Una lista de números enteros.
    
    Retorna:
    - La suma de los elementos de la lista.
    """
    pass


# Ejercicio 6: Combinaciones de un conjunto
def combinaciones(arr: list[int], r: int) -> list[list[int]]:
    """
    Genera todas las combinaciones posibles de tamaño r de un conjunto utilizando recursión.
    
    Parámetros:
    - arr: Un conjunto de elementos (lista de números enteros).
    - r: El tamaño de las combinaciones a generar.
    
    Retorna:
    - Una lista de listas, cada una representando una combinación de tamaño r.
    """
    pass


# Ejercicio 7: Torres de Hanoi
def torres_hanoi(n: int, origen: str, destino: str, auxiliar: str) -> list[str]:
    """
    Resuelve el problema de las Torres de Hanoi utilizando recursión.
    
    Parámetros:
    - n: El número de discos.
    - origen: El nombre de la torre de origen.
    - destino: El nombre de la torre de destino.
    - auxiliar: El nombre de la torre auxiliar.
    
    Retorna:
    - Una lista de movimientos (cada movimiento es una cadena que indica qué disco se mueve de una torre a otra).
    """
    pass


# Ejercicio 8: Camino más corto en una matriz (Suma de caminos)
def camino_mas_corto(matriz: list[list[int]], fila: int = 0, col: int = 0) -> int:
    """
    Encuentra el camino más corto desde la esquina superior izquierda de una matriz hasta la esquina inferior derecha.
    Se puede mover hacia la derecha o hacia abajo en cada paso.
    
    Parámetros:
    - matriz: Una matriz de enteros, donde cada número representa el costo de ese paso.
    - fila: La fila actual en la matriz.
    - col: La columna actual en la matriz.
    
    Retorna:
    - El costo total mínimo para llegar a la esquina inferior derecha.
    """
    pass


# Ejercicio 9: Subconjuntos de un conjunto
def subconjuntos(arr: list[int]) -> list[list[int]]:
    """
    Genera todos los subconjuntos posibles de un conjunto dado utilizando recursión.
    
    Parámetros:
    - arr: Un conjunto de elementos (lista de números enteros).
    
    Retorna:
    - Una lista de listas, cada una representando un subconjunto del conjunto original.
    """
    pass


# Ejercicio 10: Permutaciones de un conjunto
def permutaciones(arr: list[int]) -> list[list[int]]:
    """
    Genera todas las permutaciones posibles de un conjunto dado utilizando recursión.
    
    Parámetros:
    - arr: Un conjunto de elementos (lista de números enteros).
    
    Retorna:
    - Una lista de listas, cada una representando una permutación del conjunto original.
    """
    pass


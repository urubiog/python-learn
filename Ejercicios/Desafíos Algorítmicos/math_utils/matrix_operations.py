# math_utils/matrix_operations.py
import math


# Ejercicio 1: Sumar dos matrices
def sumar_matrices(
    matriz_a: list[list[float]], matriz_b: list[list[float]]
) -> list[list[float]]:
    """
    Suma dos matrices de las mismas dimensiones.

    Parámetros:
    - matriz_a: La primera matriz.
    - matriz_b: La segunda matriz.

    Retorna:
    - La matriz resultante de sumar las dos matrices.
    """
    pass


# Ejercicio 2: Restar dos matrices
def restar_matrices(
    matriz_a: list[list[float]], matriz_b: list[list[float]]
) -> list[list[float]]:
    """
    Resta dos matrices de las mismas dimensiones.

    Parámetros:
    - matriz_a: La primera matriz.
    - matriz_b: La segunda matriz.

    Retorna:
    - La matriz resultante de restar las dos matrices.
    """
    pass


# Ejercicio 3: Multiplicar dos matrices
def multiplicar_matrices(
    matriz_a: list[list[float]], matriz_b: list[list[float]]
) -> list[list[float]]:
    """
    Multiplica dos matrices, siempre que el número de columnas de la primera matriz
    sea igual al número de filas de la segunda matriz.

    Parámetros:
    - matriz_a: La primera matriz.
    - matriz_b: La segunda matriz.

    Retorna:
    - La matriz resultante de multiplicar las dos matrices.
    """
    pass


# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz: list[list[float]]) -> list[list[float]]:
    """
    Transpone una matriz, intercambiando filas por columnas.

    Parámetros:
    - matriz: La matriz a transponer.

    Retorna:
    - La matriz transpuesta.
    """
    pass


# Ejercicio 5: Determinante de una matriz 2x2
def determinante_2x2(matriz: list[list[float]]) -> float:
    """
    Calcula el determinante de una matriz 2x2.

    Parámetros:
    - matriz: Una matriz 2x2.

    Retorna:
    - El determinante de la matriz 2x2.
    """
    pass


# Ejercicio 6: Determinante de una matriz NxN
def determinante(matriz: list[list[float]]) -> float:
    """
    Calcula el determinante de una matriz de cualquier tamaño NxN utilizando la regla de cofactores.

    Parámetros:
    - matriz: Una matriz cuadrada de tamaño NxN.

    Retorna:
    - El determinante de la matriz.
    """
    pass


# Ejercicio 7: Inversa de una matriz 2x2
def inversa_2x2(matriz: list[list[float]]) -> list[list[float]]:
    """
    Calcula la inversa de una matriz 2x2, si existe.

    Parámetros:
    - matriz: Una matriz 2x2.

    Retorna:
    - La matriz inversa de 2x2.
    """
    pass


# Ejercicio 8: Inversa de una matriz NxN
def inversa(matriz: list[list[float]]) -> list[list[float]]:
    """
    Calcula la inversa de una matriz cuadrada NxN utilizando el método de la matriz adjunta.

    Parámetros:
    - matriz: Una matriz cuadrada de tamaño NxN.

    Retorna:
    - La matriz inversa.
    """
    pass


# Ejercicio 9: Multiplicar una matriz por un escalar
def multiplicar_por_escalar(
    matriz: list[list[float]], escalar: float
) -> list[list[float]]:
    """
    Multiplica una matriz por un escalar.

    Parámetros:
    - matriz: La matriz a multiplicar.
    - escalar: El valor escalar con el cual multiplicar la matriz.

    Retorna:
    - La matriz resultante de la multiplicación.
    """
    pass


# Ejercicio 10: Calcular el rastro (trace) de una matriz
def rastro_matriz(matriz: list[list[float]]) -> float:
    """
    Calcula el rastro de una matriz cuadrada, que es la suma de los elementos de la diagonal principal.

    Parámetros:
    - matriz: La matriz cuadrada.

    Retorna:
    - El rastro de la matriz.
    """
    pass


# Ejercicio 11: Verificar si una matriz es simétrica
def es_simetrica(matriz: list[list[float]]) -> bool:
    """
    Verifica si una matriz es simétrica, es decir, si es igual a su transpuesta.

    Parámetros:
    - matriz: La matriz a verificar.

    Retorna:
    - True si la matriz es simétrica, False en caso contrario.
    """
    pass


# Ejercicio 12: Producto punto entre dos vectores
def producto_punto(v1: list[float], v2: list[float]) -> float:
    """
    Calcula el producto punto entre dos vectores de la misma longitud.

    Parámetros:
    - v1: El primer vector.
    - v2: El segundo vector.

    Retorna:
    - El producto punto entre los dos vectores.
    """
    pass


# Ejercicio 13: Multiplicar una matriz por un vector
def multiplicar_matriz_por_vector(
    matriz: list[list[float]], vector: list[float]
) -> list[float]:
    """
    Multiplica una matriz por un vector, resultando un nuevo vector.

    Parámetros:
    - matriz: La matriz a multiplicar.
    - vector: El vector a multiplicar.

    Retorna:
    - El vector resultante de la multiplicación.
    """
    pass


# Ejercicio 14: Resolver un sistema de ecuaciones lineales usando la eliminación de Gauss
def resolver_sistema_gauss(
    matriz: list[list[float]], resultados: list[float]
) -> list[float]:
    """
    Resuelve un sistema de ecuaciones lineales utilizando el método de eliminación de Gauss.

    Parámetros:
    - matriz: La matriz de coeficientes del sistema de ecuaciones.
    - resultados: El vector de resultados del sistema.

    Retorna:
    - El vector de soluciones al sistema de ecuaciones.
    """
    pass

# math_utils/polynomial_operations.py

# Ejercicio 1: Sumar dos polinomios
def sumar_polinomios(p1: list[int], p2: list[int]) -> list[int]:
    """
    Suma dos polinomios representados como listas de coeficientes.
    El coeficiente de grado n está en el índice n de la lista.
    
    Parámetros:
    - p1: El primer polinomio representado como una lista de coeficientes.
    - p2: El segundo polinomio representado como una lista de coeficientes.
    
    Retorna:
    - Un nuevo polinomio (lista de coeficientes) que es la suma de p1 y p2.
    """
    pass

# Ejercicio 2: Restar dos polinomios
def restar_polinomios(p1: list[int], p2: list[int]) -> list[int]:
    """
    Resta dos polinomios representados como listas de coeficientes.
    El coeficiente de grado n está en el índice n de la lista.
    
    Parámetros:
    - p1: El primer polinomio representado como una lista de coeficientes.
    - p2: El segundo polinomio representado como una lista de coeficientes.
    
    Retorna:
    - Un nuevo polinomio (lista de coeficientes) que es la resta de p1 y p2.
    """
    pass

# Ejercicio 3: Multiplicar dos polinomios
def multiplicar_polinomios(p1: list[int], p2: list[int]) -> list[int]:
    """
    Multiplica dos polinomios representados como listas de coeficientes.
    
    Parámetros:
    - p1: El primer polinomio representado como una lista de coeficientes.
    - p2: El segundo polinomio representado como una lista de coeficientes.
    
    Retorna:
    - Un nuevo polinomio (lista de coeficientes) que es el producto de p1 y p2.
    """
    pass

# Ejercicio 4: Evaluar un polinomio en un valor dado
def evaluar_polinomio(p: list[int], x: int) -> int:
    """
    Evalúa un polinomio en un valor dado utilizando la fórmula de Horner.
    
    Parámetros:
    - p: El polinomio representado como una lista de coeficientes.
    - x: El valor en el que evaluar el polinomio.
    
    Retorna:
    - El valor del polinomio evaluado en x.
    """
    pass

# Ejercicio 5: Encontrar las raíces de un polinomio cuadrático
def raices_polinomio_cuadratico(a: int, b: int, c: int) -> list[float]:
    """
    Encuentra las raíces de un polinomio cuadrático de la forma ax^2 + bx + c.
    
    Parámetros:
    - a: El coeficiente de x^2.
    - b: El coeficiente de x.
    - c: El término independiente.
    
    Retorna:
    - Una lista con las raíces del polinomio. Si no existen raíces reales, se devuelve una lista vacía.
    """
    pass

# Ejercicio 6: Dividir dos polinomios
def dividir_polinomios(dividendo: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    """
    Divide dos polinomios y devuelve el cociente y el residuo.
    El algoritmo de división es similar a la división larga de números.
    
    Parámetros:
    - dividendo: El polinomio dividendo representado como una lista de coeficientes.
    - divisor: El polinomio divisor representado como una lista de coeficientes.
    
    Retorna:
    - Una tupla con dos listas de coeficientes: el cociente y el residuo de la división.
    """
    pass

# Ejercicio 7: Encontrar el máximo común divisor (MCD) de dos polinomios
def mcd_polinomios(p1: list[int], p2: list[int]) -> list[int]:
    """
    Encuentra el máximo común divisor (MCD) de dos polinomios utilizando el algoritmo
    de Euclides para polinomios.
    
    Parámetros:
    - p1: El primer polinomio representado como una lista de coeficientes.
    - p2: El segundo polinomio representado como una lista de coeficientes.
    
    Retorna:
    - El MCD de los dos polinomios.
    """
    pass

# Ejercicio 8: Hacer la derivada de un polinomio
def derivada_polinomio(p: list[int]) -> list[int]:
    """
    Calcula la derivada de un polinomio representado como una lista de coeficientes.
    
    Parámetros:
    - p: El polinomio representado como una lista de coeficientes.
    
    Retorna:
    - La derivada del polinomio representada como una lista de coeficientes.
    """
    pass

# Ejercicio 9: Hacer la integral de un polinomio
def integral_polinomio(p: list[int]) -> list[int]:
    """
    Calcula la integral indefinida de un polinomio representado como una lista de coeficientes.
    
    Parámetros:
    - p: El polinomio representado como una lista de coeficientes.
    
    Retorna:
    - La integral indefinida del polinomio representada como una lista de coeficientes.
    """
    pass

# Ejercicio 10: Simplificar un polinomio
def simplificar_polinomio(p: list[int]) -> list[int]:
    """
    Simplifica un polinomio eliminando los términos nulos (coeficientes cero) de la lista.
    
    Parámetros:
    - p: El polinomio representado como una lista de coeficientes.
    
    Retorna:
    - El polinomio simplificado, es decir, sin los coeficientes cero.
    """
    pass

# Ejercicio 11: Comprobar si dos polinomios son iguales
def son_polinomios_iguales(p1: list[int], p2: list[int]) -> bool:
    """
    Compara dos polinomios para ver si son iguales. Dos polinomios son iguales si
    tienen los mismos coeficientes en los mismos grados.
    
    Parámetros:
    - p1: El primer polinomio representado como una lista de coeficientes.
    - p2: El segundo polinomio representado como una lista de coeficientes.
    
    Retorna:
    - True si los polinomios son iguales, False en caso contrario.
    """
    pass

# Ejercicio 12: Factorizar un polinomio cuadrático
def factorizar_polinomio_cuadratico(a: int, b: int, c: int) -> str:
    """
    Factoriza un polinomio cuadrático de la forma ax^2 + bx + c.
    
    Parámetros:
    - a: El coeficiente de x^2.
    - b: El coeficiente de x.
    - c: El término independiente.
    
    Retorna:
    - La factorización en forma de una cadena, por ejemplo, "(x - 1)(x + 2)".
    """
    pass


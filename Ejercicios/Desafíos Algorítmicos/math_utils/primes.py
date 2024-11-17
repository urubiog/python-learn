# math_utils/primes.py

# Ejercicio 1: Comprobar si un número es primo
def es_primo(n: int) -> bool:
    """
    Verifica si un número es primo. Un número es primo si es mayor que 1 y solo tiene
    dos divisores: 1 y sí mismo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es primo, False en caso contrario.
    """
    pass

# Ejercicio 2: Generar una lista de números primos hasta un límite dado
def primos_hasta(limite: int) -> list[int]:
    """
    Genera una lista de números primos hasta un límite dado utilizando la Criba de Eratóstenes.
    
    Parámetros:
    - limite: El número hasta el cual generar los primos.
    
    Retorna:
    - Una lista de números primos hasta el límite dado.
    """
    pass

# Ejercicio 3: Verificar si un número es un número primo de Mersenne
def es_primo_mersenne(n: int) -> bool:
    """
    Verifica si un número es un primo de Mersenne. Un primo de Mersenne tiene la forma 2^p - 1,
    donde p también es un número primo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es un primo de Mersenne, False en caso contrario.
    """
    pass

# Ejercicio 4: Calcular los primeros N números primos
def primeros_n_primos(n: int) -> list[int]:
    """
    Genera una lista con los primeros N números primos.
    
    Parámetros:
    - n: El número de primos a generar.
    
    Retorna:
    - Una lista con los primeros N números primos.
    """
    pass

# Ejercicio 5: Comprobar si un número es un número primo de Fermat
def es_primo_fermat(n: int) -> bool:
    """
    Verifica si un número es un primo de Fermat. Un número primo de Fermat es de la forma
    2^(2^k) + 1, donde k es un número entero no negativo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es un primo de Fermat, False en caso contrario.
    """
    pass

# Ejercicio 6: Encontrar todos los divisores primos de un número
def divisores_primos(n: int) -> list[int]:
    """
    Encuentra todos los divisores primos de un número.
    
    Parámetros:
    - n: El número para el cual encontrar los divisores primos.
    
    Retorna:
    - Una lista con los divisores primos de n.
    """
    pass

# Ejercicio 7: Generar números primos en un rango dado
def primos_en_rango(inicio: int, fin: int) -> list[int]:
    """
    Genera una lista de números primos dentro de un rango dado [inicio, fin].
    
    Parámetros:
    - inicio: El inicio del rango.
    - fin: El fin del rango.
    
    Retorna:
    - Una lista de números primos dentro del rango [inicio, fin].
    """
    pass

# Ejercicio 8: Calcular la suma de los primeros N números primos
def suma_primos_hasta_n(n: int) -> int:
    """
    Calcula la suma de los primeros N números primos.
    
    Parámetros:
    - n: El número de primos cuya suma se quiere calcular.
    
    Retorna:
    - La suma de los primeros N números primos.
    """
    pass

# Ejercicio 9: Verificar si dos números son primos relativos
def son_primos_relativos(a: int, b: int) -> bool:
    """
    Verifica si dos números son primos relativos, es decir, si su MCD (máximo común divisor)
    es 1.
    
    Parámetros:
    - a: El primer número.
    - b: El segundo número.
    
    Retorna:
    - True si los números son primos relativos, False en caso contrario.
    """
    pass

# Ejercicio 10: Calcular la fórmula de Wilson para un número primo
def formula_wilson(p: int) -> bool:
    """
    Verifica si un número p cumple la fórmula de Wilson para números primos. La fórmula dice que:
    (p - 1)! ≡ -1 (mod p), para todo número primo p.
    
    Parámetros:
    - p: El número a verificar.
    
    Retorna:
    - True si p cumple la fórmula de Wilson, False en caso contrario.
    """
    pass

# Ejercicio 11: Verificar si un número es primo de Sophie Germain
def es_primo_sophie_germain(n: int) -> bool:
    """
    Verifica si un número es un primo de Sophie Germain. Un primo de Sophie Germain es un número
    primo p tal que 2p + 1 también es un número primo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si n es un primo de Sophie Germain, False en caso contrario.
    """
    pass

# Ejercicio 12: Encontrar los números primos gemelos
def primos_gemelos(limite: int) -> list[tuple[int, int]]:
    """
    Encuentra todos los pares de números primos gemelos hasta un límite dado. Dos números primos
    son gemelos si la diferencia entre ellos es 2.
    
    Parámetros:
    - limite: El límite hasta el cual buscar pares de primos gemelos.
    
    Retorna:
    - Una lista de tuplas con pares de primos gemelos.
    """
    pass

# Ejercicio 13: Comprobar si un número es un número primo fuerte
def es_primo_fuerte(n: int) -> bool:
    """
    Verifica si un número es un número primo fuerte. Un número primo fuerte es aquel que es mayor que 3
    y su doble menos 1 también es un número primo.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es un primo fuerte, False en caso contrario.
    """
    pass


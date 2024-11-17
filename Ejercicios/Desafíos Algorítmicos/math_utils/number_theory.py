# math_utils/number_theory.py
import math

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

# Ejercicio 2: Calcular el máximo común divisor (MCD) de dos números
def mcd(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    
    Parámetros:
    - a: El primer número.
    - b: El segundo número.
    
    Retorna:
    - El MCD de los dos números.
    """
    pass

# Ejercicio 3: Calcular el mínimo común múltiplo (MCM) de dos números
def mcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo (MCM) de dos números utilizando la relación:
    MCM(a, b) = abs(a * b) // MCD(a, b)
    
    Parámetros:
    - a: El primer número.
    - b: El segundo número.
    
    Retorna:
    - El MCM de los dos números.
    """
    pass

# Ejercicio 4: Encontrar todos los divisores de un número
def divisores(n: int) -> list[int]:
    """
    Encuentra todos los divisores de un número.
    
    Parámetros:
    - n: El número del cual encontrar los divisores.
    
    Retorna:
    - Una lista con todos los divisores de n.
    """
    pass

# Ejercicio 5: Calcular la factorización prima de un número
def factorizacion_prima(n: int) -> list[int]:
    """
    Devuelve la factorización prima de un número. Es decir, descompone el número en
    factores primos.
    
    Parámetros:
    - n: El número a factorizar.
    
    Retorna:
    - Una lista con los factores primos del número.
    """
    pass

# Ejercicio 6: Calcular la potencia modular
def potencia_modular(base: int, exponente: int, modulo: int) -> int:
    """
    Calcula la potencia de un número en módulo de forma eficiente utilizando
    exponenciación rápida.
    
    Parámetros:
    - base: El número base.
    - exponente: El exponente al que elevar la base.
    - modulo: El módulo en el que calcular la potencia.
    
    Retorna:
    - El resultado de (base ^ exponente) % modulo.
    """
    pass

# Ejercicio 7: Algoritmo de Criba de Eratóstenes
def criba_eratostenes(limite: int) -> list[int]:
    """
    Encuentra todos los números primos hasta un límite dado utilizando el algoritmo
    de la Criba de Eratóstenes.
    
    Parámetros:
    - limite: El número hasta el cual encontrar los primos.
    
    Retorna:
    - Una lista de números primos menores o iguales al límite.
    """
    pass

# Ejercicio 8: Comprobar si un número es un número perfecto
def es_numero_perfecto(n: int) -> bool:
    """
    Verifica si un número es perfecto. Un número perfecto es aquel que es igual
    a la suma de sus divisores propios (excluyendo el mismo número).
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es perfecto, False en caso contrario.
    """
    pass

# Ejercicio 9: Calcular el teorema de Fermat para el último teorema de Fermat
def fermat_ultimo_teorema(a: int, b: int, c: int, n: int) -> bool:
    """
    Verifica si los números dados cumplen con la ecuación de Fermat para el último
    teorema de Fermat: a^n + b^n = c^n.
    
    Parámetros:
    - a: El primer número.
    - b: El segundo número.
    - c: El tercer número.
    - n: El exponente.
    
    Retorna:
    - True si la ecuación se cumple, False en caso contrario.
    """
    pass

# Ejercicio 10: Resolver la congruencia lineal
def resolver_congruencia(a: int, b: int, m: int) -> int:
    """
    Resuelve una congruencia lineal de la forma a * x ≡ b (mod m) utilizando el algoritmo
    extendido de Euclides.
    
    Parámetros:
    - a: El coeficiente de la congruencia.
    - b: El término constante de la congruencia.
    - m: El módulo.
    
    Retorna:
    - El valor de x que satisface la congruencia o None si no tiene solución.
    """
    pass

# Ejercicio 11: Comprobar si un número es un número de Fibonacci
def es_numero_fibonacci(n: int) -> bool:
    """
    Verifica si un número es parte de la secuencia de Fibonacci.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es de Fibonacci, False en caso contrario.
    """
    pass

# Ejercicio 12: Calcular el número de Euler (phi) de un número
def phi(n: int) -> int:
    """
    Calcula el número de Euler (función phi) de un número n. La función phi de n
    cuenta cuántos números enteros menores que n son coprimos con n.
    
    Parámetros:
    - n: El número para el cual calcular la función phi.
    
    Retorna:
    - El valor de phi(n).
    """
    pass

# Ejercicio 13: Comprobar si un número es un cuadrado perfecto
def es_cuadrado_perfecto(n: int) -> bool:
    """
    Verifica si un número es un cuadrado perfecto, es decir, si tiene una raíz
    cuadrada entera.
    
    Parámetros:
    - n: El número a verificar.
    
    Retorna:
    - True si el número es un cuadrado perfecto, False en caso contrario.
    """
    pass

# Ejercicio 14: Generar números primos dentro de un rango
def primos_en_rango(inicio: int, fin: int) -> list[int]:
    """
    Genera una lista de números primos dentro de un rango dado.
    
    Parámetros:
    - inicio: El inicio del rango.
    - fin: El fin del rango.
    
    Retorna:
    - Una lista de números primos dentro del rango [inicio, fin].
    """
    pass


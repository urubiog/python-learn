# math_utils/probability.py

# Ejercicio 1: Calcular la probabilidad de un evento
def calcular_probabilidad(eventos_favorables: int, eventos_posibles: int) -> float:
    """
    Calcula la probabilidad de un evento. La probabilidad de un evento es el número de eventos favorables
    dividido por el número total de eventos posibles.
    
    Parámetros:
    - eventos_favorables: El número de eventos favorables.
    - eventos_posibles: El número total de eventos posibles.
    
    Retorna:
    - La probabilidad de que ocurra el evento.
    """
    pass

# Ejercicio 2: Probabilidad de la unión de dos eventos (A ∪ B)
def probabilidad_union(p_a: float, p_b: float, p_a_y_b: float) -> float:
    """
    Calcula la probabilidad de la unión de dos eventos, es decir, la probabilidad de que ocurra A o B.
    La fórmula es: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
    
    Parámetros:
    - p_a: La probabilidad del evento A.
    - p_b: La probabilidad del evento B.
    - p_a_y_b: La probabilidad de que ambos eventos A y B ocurran.
    
    Retorna:
    - La probabilidad de que ocurra A o B.
    """
    pass

# Ejercicio 3: Probabilidad de la intersección de dos eventos (A ∩ B)
def probabilidad_interseccion(p_a: float, p_b: float, p_a_o_b: float) -> float:
    """
    Calcula la probabilidad de la intersección de dos eventos, es decir, la probabilidad de que ocurran
    ambos eventos A y B.
    La fórmula es: P(A ∩ B) = P(A) + P(B) - P(A ∪ B)
    
    Parámetros:
    - p_a: La probabilidad del evento A.
    - p_b: La probabilidad del evento B.
    - p_a_o_b: La probabilidad de que ocurra A o B.
    
    Retorna:
    - La probabilidad de que ocurran ambos eventos A y B.
    """
    pass

# Ejercicio 4: Calcular la probabilidad condicional
def probabilidad_condicional(p_a_y_b: float, p_b: float) -> float:
    """
    Calcula la probabilidad condicional de A dado B. La fórmula es: P(A|B) = P(A ∩ B) / P(B)
    
    Parámetros:
    - p_a_y_b: La probabilidad de que ocurran ambos eventos A y B.
    - p_b: La probabilidad de que ocurra el evento B.
    
    Retorna:
    - La probabilidad de que ocurra A dado que ha ocurrido B.
    """
    pass

# Ejercicio 5: Distribución binomial
def distribucion_binomial(n: int, k: int, p: float) -> float:
    """
    Calcula la probabilidad de obtener exactamente k éxitos en n intentos, usando la distribución binomial.
    La fórmula es: P(X = k) = (n C k) * p^k * (1-p)^(n-k)
    
    Parámetros:
    - n: El número de intentos.
    - k: El número de éxitos deseados.
    - p: La probabilidad de éxito en un intento.
    
    Retorna:
    - La probabilidad de obtener exactamente k éxitos.
    """
    pass

# Ejercicio 6: Distribución normal (valor Z)
def distribucion_normal(z: float) -> float:
    """
    Calcula la probabilidad de que una variable aleatoria con distribución normal tenga un valor menor o igual
    a un valor dado z (valor Z).
    
    Parámetros:
    - z: El valor Z, que es el número de desviaciones estándar que se aleja de la media.
    
    Retorna:
    - La probabilidad acumulada hasta el valor Z en una distribución normal estándar.
    """
    pass

# Ejercicio 7: Calcular el número esperado de éxitos
def numero_esperado_exitos(n: int, p: float) -> float:
    """
    Calcula el número esperado de éxitos en n intentos con una probabilidad p de éxito en cada intento.
    La fórmula es: E(X) = n * p
    
    Parámetros:
    - n: El número de intentos.
    - p: La probabilidad de éxito en un intento.
    
    Retorna:
    - El número esperado de éxitos.
    """
    pass

# Ejercicio 8: Calcular la varianza de una distribución binomial
def varianza_binomial(n: int, p: float) -> float:
    """
    Calcula la varianza de una distribución binomial. La fórmula es: Var(X) = n * p * (1 - p)
    
    Parámetros:
    - n: El número de intentos.
    - p: La probabilidad de éxito en un intento.
    
    Retorna:
    - La varianza de la distribución binomial.
    """
    pass

# Ejercicio 9: Teorema de Bayes
def teorema_bayes(p_a: float, p_b: float, p_b_dado_a: float) -> float:
    """
    Aplica el teorema de Bayes para calcular la probabilidad de un evento A dado que B ha ocurrido.
    La fórmula es: P(A|B) = (P(B|A) * P(A)) / P(B)
    
    Parámetros:
    - p_a: La probabilidad del evento A.
    - p_b: La probabilidad del evento B.
    - p_b_dado_a: La probabilidad de que B ocurra dado que A ha ocurrido.
    
    Retorna:
    - La probabilidad de A dado B.
    """
    pass

# Ejercicio 10: Distribución de Poisson
def distribucion_poisson(k: int, lambda_: float) -> float:
    """
    Calcula la probabilidad de observar exactamente k eventos en un intervalo dado, usando la distribución de Poisson.
    La fórmula es: P(X = k) = (lambda^k * e^(-lambda)) / k!
    
    Parámetros:
    - k: El número de eventos observados.
    - lambda_: La tasa promedio de ocurrencia de eventos en el intervalo.
    
    Retorna:
    - La probabilidad de observar exactamente k eventos.
    """
    pass

# Ejercicio 11: Experimento de Monte Carlo
def monte_carlo(una_funcion, num_simulaciones: int) -> float:
    """
    Realiza una simulación de Monte Carlo para estimar el valor esperado de una función.
    
    Parámetros:
    - una_funcion: La función que se desea simular.
    - num_simulaciones: El número de simulaciones a realizar.
    
    Retorna:
    - El valor estimado de la función basado en el número de simulaciones.
    """
    pass

# Ejercicio 12: Simulación de lanzamientos de dados
def simulacion_lanzamientos_dado(num_lanzamientos: int) -> list[int]:
    """
    Simula el lanzamiento de un dado (números del 1 al 6) durante un número dado de lanzamientos.
    
    Parámetros:
    - num_lanzamientos: El número de veces que se lanzará el dado.
    
    Retorna:
    - Una lista con los resultados de cada lanzamiento del dado.
    """
    pass


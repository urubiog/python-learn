import random as rd

# Inicializa el generador de números aleatorios con una semilla específica
rd.seed(42)

# Obtiene el estado interno del generador de números aleatorios
state = rd.getstate()

# Restaura el estado interno del generador de números aleatorios al estado previo
rd.setstate(state)

# Genera un número flotante aleatorio en el rango [0.0, 1.0)
random_number = rd.random()

# Genera un número flotante aleatorio entre 10 y 20
random_uniform = rd.uniform(10, 20)

# Genera un número flotante aleatorio con distribución triangular
random_triangular = rd.triangular(0, 10, 5)

# Genera un número entero aleatorio en el rango [1, 10]
random_integer = rd.randint(1, 10)

# Retorna un número aleatorio de la secuencia (lista) dada
random_choice = rd.choice(['a', 'b', 'c'])

# Retorna una lista de 3 elementos elegidos aleatoriamente de una población con pesos
random_choices = rd.choices(['a', 'b', 'c'], weights=[1, 1, 2], k=3)

# Retorna una muestra de 2 elementos únicos seleccionados aleatoriamente de una población
random_sample = rd.sample(range(1, 100), 2)

# Mezcla una lista de elementos en su lugar
x = [1, 2, 3, 4, 5]
rd.shuffle(x)

# Retorna un número flotante aleatorio de la distribución beta
random_betavariate = rd.betavariate(2, 5)

# Retorna un número flotante aleatorio de la distribución exponencial
random_expovariate = rd.expovariate(0.5)

# Retorna un número flotante aleatorio de la distribución gamma
random_gammavariate = rd.gammavariate(2, 2)

# Retorna un número flotante aleatorio de la distribución gaussiana (normal)
random_gauss = rd.gauss(0, 1)

# Retorna un número flotante aleatorio de la distribución log-normal
random_lognormvariate = rd.lognormvariate(0, 1)

# Retorna un número flotante aleatorio de la distribución normal
random_normalvariate = rd.normalvariate(0, 1)

# Retorna un número flotante aleatorio de la distribución de von Mises
random_vonmisesvariate = rd.vonmisesvariate(0, 1)

# Retorna un número flotante aleatorio de la distribución de Pareto
random_paretovariate = rd.paretovariate(3)

# Retorna un número flotante aleatorio de la distribución de Weibull
random_weibullvariate = rd.weibullvariate(2, 3)
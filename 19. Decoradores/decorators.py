# Decorador @property: Permite definir métodos que se comportan como atributos.
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

# Decorador @classmethod: Permite definir métodos que operan en la clase en lugar de en instancias individuales.
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_string(cls, cadena_fecha):
        dia, mes, año = map(int, cadena_fecha.split('-'))
        return cls(dia, mes, año)

# Decorador @staticmethod: Permite definir métodos que no toman la instancia o la clase como argumento.
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

# Decorador @classmethod vs @staticmethod: Diferencia entre @classmethod y @staticmethod.
class Ejemplo:
    valor = 10

    @classmethod
    def metodo_de_clase(cls):
        return cls.valor

    @staticmethod
    def metodo_estatico():
        return Ejemplo.valor

# Decorador @classmethod como Constructor Alternativo: Utilizando @classmethod como un constructor alternativo.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_diccionario(cls, diccionario):
        return cls(diccionario['nombre'], diccionario['edad'])

# Decorador @property setter: Permite definir un método setter para un atributo.
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

# Decorador @property deleter: Permite definir un método deleter para un atributo.
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre

# Decoradores Personalizados: Creación de decoradores personalizados.
def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Ejecutando antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Ejecutando después de la función")
        return resultado
    return wrapper

@mi_decorador
def mi_funcion():
    print("Dentro de la función")

# Decorador para Caché LRU: Este decorador permite cachear el resultado de una función utilizando el algoritmo LRU (Least Recently Used).
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Decorador para Medir el Tiempo de Ejecución: Este decorador mide el tiempo de ejecución de una función y muestra el tiempo transcurrido.
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time} segundos")
        return result
    return wrapper

@timer
def ejemplo():
    time.sleep(2)
    print("Función ejecutada")

ejemplo()
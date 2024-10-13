# --- * ---
# Para tipar se usa ":" y "->"
# ---------

# Indicando el tipo de dato para las variables
a: int = 15
b: float = 13.5
print(b)
# ------

# Para los tipos de datos compuestos se puede especificar de que se componen
c: list[int] = [1, 2, 3]
d: set[int] = {1, 2, 3, 4}
e: dict[str, any] = dict(name="Uriel", age=14) # any es un comodín
f: list[int, str] = [1, "2"]
# ------

# Tipado de argumentos para funciones
def sumar(a: int, b: int) -> int: # "-> int" indica que la función retorna un dato de tipo int
    return a + b

# Otro ejemplo
def concatenar(cadena1: str, cadena2: str) -> str:
    return cadena1 + cadena2
# ------

# El tipado se puede presentar en muchos elementos
class Punto:
    def __init__(self, x: float, y: float) -> None:
        self.x = x  # Coordenada x del punto
        self.y = y  # Coordenada y del punto

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"  # Representación en forma de cadena del punto

    # Método para calcular la distancia entre dos puntos
    def distancia(self, otro_punto: 'Punto') -> float:
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5
# ------
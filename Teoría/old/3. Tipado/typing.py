# Para tipar se usa ":" y "->"

# Indicando el tipo de dato para las variables
a: int = 15
b: float = 13.5
print(b)

# Aún que esté mal tipado, Python lo ejecuta
c: int = 5.5

# Para los tipos de datos compuestos se puede especificar de que se componen
c: list[int] = [1, 2, 3]
d: set[int] = {1, 2, 3, 4}
e: dict[str, any] = dict(name="Uriel", age=14) # any es un comodín
f: list[int, str] = [1, "2"]

# Tipado de argumentos para funciones
def sumar(a: int, b: int) -> int: # "-> int" indica que la función retorna un dato de tipo int
    return a + b

# Otro ejemplo
def concatenar(cadena1: str, cadena2: str) -> str:
    return cadena1 + cadena2

# Incluso podemos tipar diferentes posibilidades
a: str = input("Introduce un número: ")

b: int | float

if "." in a:
    b = float(a)
else:
    b = int(a)

print(type(b))

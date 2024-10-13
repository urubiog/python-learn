# Funciones

# Devuelve el valor absoluto de un número.
print(abs(-31532))

# Devuelve True si todos los elementos de un iterable son verdaderos, False en caso contrario.
lista = ["mono", "gato", "perro", None]
print(all(lista))

# Devuelve True si al menos un elemento de un iterable es verdadero, False en caso contrario.
print(any(lista))

# Devuelve una cadena que representa el objeto especificado, pero con caracteres no ASCII reemplazados por secuencias de escape.
cadena = "á à é è í ì ó ò ú ù"
print(ascii(cadena))

# Convierte un número entero en una cadena binaria.
print(bin(10))

# Convierte un valor en True o False.
print(bool(None))

# Devuelve True si el objeto especificado es "llamable" (es decir, puede ser llamado como una función), False en caso contrario.
print(callable(bin))

# Devuelve el carácter Unicode correspondiente al número entero especificado.
print(chr(1))

# Compila el código fuente en un objeto de código o en una representación en bytes.
codigo_fuente = """
def saludar():
    print("Hola, mundo!")

saludar()
"""
# Compilamos el código fuente en un objeto de código
codigo_compilado = compile(codigo_fuente, '<string>', 'exec')

# Ejecutamos el código compilado
exec(codigo_compilado)

# Crea un número complejo.
print(complex(1))

# Elimina un atributo de un objeto.
class Objeto:
    def __init__(self, atributo):
        self.atributo = str(atributo)
        self.uno = 1

mari = Objeto(1)
print(mari.atributo)
delattr(mari, "atributo")

# Crea un nuevo diccionario.
print(dict([("1a", "a1")]))

# Devuelve la lista de nombres en el ámbito local actual o el listado de atributos de un objeto.
print(dir(mari))

# Devuelve el cociente y el resto de la división de dos números.
print(divmod(3156, 5))

# Devuelve un objeto enumerado que contiene tuplas de índice y valor de un iterable.
colores = ['rojo', 'verde', 'azul', 'amarillo']
for indice, elemento in enumerate(colores):
    print(f"El color en el índice {indice} es: {elemento}")

# Evalúa una expresión Python dada como una cadena y devuelve el resultado.
print(eval("3 + 5 * 4"))

# Ejecuta código Python dinámicamente.
exec("for x in range(2): print(x)")

# Filtra elementos de un iterable utilizando una función.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def es_par(numero):
    return numero % 2 == 0
print(list(filter(es_par, numeros)))

# Convierte un número o una cadena en un número de punto flotante.
print(float(13))

# Formatea un valor utilizando una especificación de formato.
cadena = "Hola {}, me llamo {} y soy {}"
print(cadena.format("Paco", "Uriel", "nuevo"))

# Crea un nuevo conjunto inmutable.
print(frozenset([1, 2, 3]))

# Devuelve el valor de un atributo de un objeto.
print(getattr(mari, "uno"))

# Devuelve un diccionario que representa el ámbito global actual.
print(globals())

# Devuelve True si un objeto tiene un atributo con el nombre especificado, False en caso contrario.
print(hasattr(mari, "uno"))

# Devuelve el valor hash de un objeto.
print(hash(cadena))

# Muestra la documentación de ayuda.
help(abs)

# Aplicar una función a cada elemento de uno o más iterables
def cuadrado(x):
    return x ** 2
numeros = [1, 2, 3, 4, 5]
print(list(map(cuadrado, numeros)))

# Convierte un número entero en una cadena hexadecimal.
print(hex(112133512))

# Devuelve el identificador único de un objeto.
print(id(cadena))

# Lee una entrada desde el usuario.
entrada_usuario = input("Introduce algo: ")
print(entrada_usuario)

# Convierte un valor en un número entero.
print(int(3.14))

# Comprueba si un objeto es una instancia de una clase dada.
print(isinstance(3, int))

# Comprueba si una clase es una subclase de otra clase.
print(issubclass(int, object))

# Crea un iterador.
mi_lista = [1, 2, 3, 4, 5]
mi_iterador = iter(mi_lista)
for elemento in mi_iterador:
    print(elemento)

# Devuelve la longitud de un objeto.
print(len(mi_lista))

# Devuelve el elemento más grande de un iterable o el mayor de dos o más argumentos.
print(max(5, 10, 20))

# Devuelve el elemento más pequeño de un iterable o el menor de dos o más argumentos.
print(min(5, 10, 20))

# Devuelve el valor de x a la potencia y (x^y).
print(pow(2, 3))

# Devuelve un número flotante redondeado al número de dígitos especificado.
print(round(3.14159265359, 2))

# Crea un objeto de "rebanada" que puede ser usado para acceder a una porción de una secuencia (por ejemplo, una lista, tupla o cadena).
mi_lista = [1, 2, 3, 4, 5]
mi_rebanada = slice(2)
print(mi_lista[mi_rebanada])

# Devuelve una nueva lista ordenada a partir de los elementos de un iterable.
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(sorted(mi_lista))

# Devuelve la suma de los elementos de un iterable.
mi_lista = [1, 2, 3, 4, 5]
print(sum(mi_lista))

# Convierte un número entero en una cadena octal.
print(oct(8))

# Devuelve el valor entero Unicode para un carácter Unicode de un solo carácter.
print(ord('A'))

# Establece el valor de un atributo de un objeto.
class Objeto:
    def __init__(self, atributo):
        self.atributo = str(atributo)
        self.uno = 1

mari = Objeto(1)
print(mari.atributo)
setattr(mari, "atributo", "nuevo_atributo")
print(mari.atributo)

# Convierte un objeto en una representación de cadena.
print(str(123))

# Convierte un iterable en una tupla.
print(tuple([1, 2, 3]))
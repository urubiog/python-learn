# Métodos especiales (dunder methods):

# __init__: Método especial utilizado para inicializar objetos.
class MiClase:
    def __init__(self, valor):
        self.valor = valor

objeto = MiClase(10)

# __str__: Método especial que devuelve una representación en forma de cadena del objeto.
class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Valor: {self.valor}"

objeto = MiClase(10)
print(objeto)

# __len__: Método especial que devuelve la longitud de un objeto.
mi_lista = [1, 2, 3, 4, 5]
print(len(mi_lista))

# __getitem__: Método especial que permite acceder a elementos de un objeto mediante índices.
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[2])

# __setitem__: Método especial que permite asignar valores a elementos de un objeto mediante índices.
mi_lista = [1, 2, 3, 4, 5]
mi_lista[2] = 10
print(mi_lista)

# Atributos especiales:

# __doc__: Atributo especial que almacena la cadena de documentación del objeto.
class MiClase:
    """Esta es la documentación de la clase MiClase."""
    pass

print(MiClase.__doc__)

# __name__: Atributo especial que almacena el nombre del módulo o clase.
print(__name__)

# __class__: Atributo especial que almacena una referencia a la clase de un objeto.
class MiClase:
    pass

objeto = MiClase()
print(objeto.__class__)

# __dict__: Atributo especial que almacena un diccionario con los atributos del objeto.
class MiClase:
    def __init__(self, valor):
        self.valor = valor

objeto = MiClase(10)
print(objeto.__dict__)

# __repr__: Devuelve la representación "oficial" de un objeto como una cadena.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

# __len__: Devuelve la longitud de un objeto.
class ListaPersonalizada:
    def __init__(self, lista):
        self.lista = lista

    def __len__(self):
        return len(self.lista)

# __getitem__ y __setitem__: Permite acceder y modificar elementos de un objeto como si fuera una secuencia.
class MiDiccionario:
    def __init__(self):
        self.datos = {}

    def __getitem__(self, clave):
        return self.datos[clave]

    def __setitem__(self, clave, valor):
        self.datos[clave] = valor

# __iter__ y __next__: Permite que un objeto sea iterable y define su comportamiento de iteración.
class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.valor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor < self.limite:
            self.valor += 1
            return self.valor
        else:
            raise StopIteration

# __del__: Define el comportamiento cuando un objeto es eliminado.
class Ejemplo:
    def __del__(self):
        print("El objeto ha sido eliminado")

objeto = Ejemplo()
del objeto

# __contains__: Verifica si un objeto contiene un elemento específico.
class ListaPersonalizada:
    def __init__(self, lista):
        self.lista = lista

    def __contains__(self, elemento):
        return elemento in self.lista

# __add__, __sub__, __mul__, __truediv__: Sobrecarga de operadores matemáticos para objetos.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x, self.y + otro_punto.y)

punto1 = Punto(1, 2)
punto2 = Punto(3, 4)
resultado = punto1 + punto2

# __eq__, __ne__, __lt__, __gt__, __le__, __ge__: Sobrecarga de operadores de comparación.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
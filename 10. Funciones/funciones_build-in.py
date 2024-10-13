# Devuelve 5, el valor absoluto de -5.
abs_value = abs(-5)
print(abs_value)  

class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
# Elimina el atributo "name" del objeto p.
delattr(p, "name")
print(p.__dict__)  # Output: {}

# Devuelve el valor hash de la cadena "hello".
hash_value = hash("hello")
print(hash_value)

# Crea un objeto de vista de memoria para el bytes "example".
mv = memoryview(b"example")
print(mv[0])  # Output: 101

# Crea un conjunto {1, 2, 3}.
s = set([1, 2, 3])
print(s)

# Devuelve False ya que hay un elemento Falso en la lista.
all_true = all([True, False, True])
print(all_true)

# Crea un diccionario {'a': 1, 'b': 2}.
d = dict({"a": 1, "b": 2})
print(d)

# Muestra la documentación del tipo de datos dict.
help_dict = help(dict)
print(help_dict)

# Devuelve 3, el valor mínimo entre 5, 3 y 8.
min_value = min(5, 3, 8)
print(min_value)

# Establece el atributo "age" en el objeto p con el valor 30.
setattr(p, "age", 30)
print(p.__dict__)  # Output: {'age': 30}

# Devuelve True ya que hay un elemento Verdadero en la lista.
any_true = any([False, False, True])
print(any_true)

# Devuelve la lista de los atributos y métodos del tipo de datos list.
dir_list = dir(list)
print(dir_list[:5])  # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__']

# Devuelve '0xff', la representación hexadecimal de 255.
hex_value = hex(255)
print(hex_value)

# Devuelve 1, el primer elemento del iterable.
next_value = next(iter([1, 2, 3]))
print(next_value)

# Crea un objeto de corte que representa los índices de 0 a 3.
s = slice(0, 3)
print(s)

# Devuelve "'h\\xebllo'", la representación ASCII de "hëllo".
ascii_value = ascii("hëllo")
print(ascii_value)

# Devuelve (3, 1), el cociente y el resto de la división de 10 por 3.
divmod_value = divmod(10, 3)
print(divmod_value)

# Devuelve el identificador único del objeto p.
id_value = id(p)
print(id_value)

# Crea un nuevo objeto base.
obj = object()
print(obj)

# Devuelve [1, 2, 3], la lista ordenada de los elementos.
sorted_list = sorted([3, 1, 2])
print(sorted_list)

# Devuelve '0b1010', la representación binaria de 10.
bin_value = bin(10)
print(bin_value)

# Devuelve un iterador que enumera los elementos.
enum = enumerate(["a", "b", "c"])
print(list(enum))

# Lee una entrada desde la entrada estándar.
user_input = input("Enter your name: ")
print("Hello, " + user_input)

# Devuelve '0o10', la representación octal de 8.
oct_value = oct(8)
print(oct_value)

# Convierte una función en un método estático.
@staticmethod
def static_method(x):
    return x + 1
print(static_method(5))

# Devuelve True, ya que 1 es evaluado como Verdadero.
bool_value = bool(1)
print(bool_value)

# Evalúa la expresión y devuelve el resultado.
eval_result = eval("3 + 5")
print(eval_result)

# Convierte la cadena "10" en un entero.
int_value = int("10")
print(int_value)

# Abre el archivo "file.txt" en modo lectura.
with open("file.txt", "r") as f:
    content = f.read()
print(content)

# Convierte el entero 123 en una cadena.
str_value = str(123)
print(str_value)

# Invoca el depurador interactivo.
breakpoint()

# Ejecuta la cadena como código Python.
exec("print('Hello, world!')")

# Comprueba si p es una instancia de Person.
is_instance = isinstance(p, Person)
print(is_instance)

# Devuelve 65, el valor ASCII de 'A'.
ascii_value = ord('A')
print(ascii_value)

# Devuelve 6, la suma de los elementos de la lista.
sum_value = sum([1, 2, 3])
print(sum_value)

# Crea un objeto bytearray desde la cadena de bytes "hello".
ba = bytearray(b"hello")
print(ba)

# Filtra los elementos mayores que 5 en la lista.
filtered = filter(lambda x: x > 5, [3, 6, 9])
print(list(filtered))

# Comprueba si bool es una subclase de int.
is_subclass = issubclass(bool, int)
print(is_subclass)

# Devuelve 8, el resultado de elevar 2 a la potencia de 3.
pow_value = pow(2, 3)
print(pow_value)

# Crea un objeto bytes a partir de una lista de enteros.
bytes_obj = bytes([65, 66, 67])
print(bytes_obj)

# Convierte el entero 3 en un flotante.
float_value = float(3)
print(float_value)

# Devuelve un iterador para la lista [1, 2, 3].
iter_list = iter([1, 2, 3])
print(list(iter_list))

# Imprime "Hello, world!" en la salida estándar.
print("Hello, world!")

# Crea una tupla (1, 2, 3) a partir de una lista.
tuple_value = tuple([1, 2, 3])
print(tuple_value)

# Devuelve True, ya que la función lambda es "llamable".
callable_value = callable(lambda x: x + 1)
print(callable_value)

# Formatea el flotante como un porcentaje.
formatted = format(0.5, "%")
print(formatted)

# Devuelve 5, la longitud de la cadena "hello".
len_value = len("hello")
print(len_value)

# Crea una propiedad de solo lectura para el atributo _name.
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("John")
name_property = p.name
print(name_property)

# Devuelve <class '__main__.Person'>, el tipo de objeto p.
type_value = type(p)
print(type_value)

# Devuelve 'A', el carácter correspondiente al valor ASCII 65.
chr_value = chr(65)
print(chr_value)

# Crea un conjunto inmutable {1, 2, 3}.
fs = frozenset({1, 2, 3})
print(fs)

# Crea una lista [1, 2, 3] a partir de una tupla.
list_value = list((1, 2, 3))
print(list_value)

# Crea un rango de números del 0 al 4.
r = range(5)
print(list(r))

# Devuelve {'name': 'John', 'age': 30}, los atributos de objeto p.
vars_value = vars(p)
print(vars_value)

# Convierte una función en un método de clase.
class MyClass:
    @classmethod
    def my_method(cls):
        print("Hello from MyClass")

MyClass.my_method()

# Obtiene el valor de un atributo de un objeto.
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
name_value = getattr(p, "name")
print(name_value)

# Devuelve un diccionario que representa el alcance local actual.
locals_value = locals()
print(locals_value)

# Devuelve una representación de cadena de un objeto.
repr_value = repr(p)
print(repr_value)

# Combina elementos de varios iterables en tuplas.
z = zip([1, 2, 3], ['a', 'b', 'c'])
print(list(z))

# Compila una cadena en un objeto de código Python.
code_obj = compile('print("Hello, world!")', '', 'exec')
exec(code_obj)

# Devuelve un diccionario que representa el alcance global actual.
globals_value = globals()
print(globals_value)

# Aplica una función a cada elemento de un iterable.
mapped = map(lambda x: x * 2, [1, 2, 3])
print(list(mapped))

# Devuelve un iterador que invierte un iterable.
reversed_list = reversed([1, 2, 3])
print(list(reversed_list))

# Importa un módulo.
import math
print(math.sqrt(25))

# Crea un número complejo.
c = complex(3, 4)
print(c)

# Comprueba si p tiene un atributo llamado "name".
has_attr = hasattr(p, "name")
print(has_attr)

# Devuelve 9, el valor máximo de la lista.
max_value = max([5, 3, 9])
print(max_value)

# Redondea 3.14159 al número entero más cercano.
rounded = round(3.14159)
print(rounded)
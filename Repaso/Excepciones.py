# Built-in expecions

# Todas derivan de BaseException

# NameError
# Se produce cuando se utiliza una variable no definida.
print(x)

# IndexError
# Se produce cuando se intenta acceder a un índice fuera del rango de una lista.
my_list = [1, 2, 3]
print(my_list[4])

# KeyError
# Se produce cuando se intenta acceder a una clave que no existe en un diccionario.
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])

# ImportError
# Se produce cuando se intenta importar un módulo que no existe.
import some_module

# ValueError
# Se produce cuando una función recibe un argumento del tipo correcto, pero con un valor inapropiado.
int('abc')

# ZeroDivisionError
# Se produce cuando se intenta dividir un número por cero.
print(1 / 0)

# AttributeError
# Se produce cuando se intenta acceder a un atributo que no existe en un objeto.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list.upper())

# AssertionError
# Se produce cuando una afirmación (assert) falla.
assert False

# Exception
# Esta es la clase base para todas las excepciones en Python.

# OSError
# Se produce cuando se produce un error relacionado con el sistema operativo.
open('non_existent_file.txt')

# OverflowError
# Se produce cuando un cálculo aritmético excede los límites de representación.
print(2 ** 1000000)

# TypeError
# Se produce cuando se realiza una operación sobre un tipo incorrecto de objeto.
print('5' + 5)

# IndentationError
# Se produce cuando la indentación no es correcta en el código Python.
def my_function():
print('IndentationError')

# KeyboardInterrupt
# Se produce cuando el usuario interrumpe la ejecución del programa (generalmente con Ctrl+C).
while True:
    pass

# NotImplementedError
# Se produce cuando una clase o método no ha sido implementado todavía.
class MyClass:
    def my_method(self):
        raise NotImplementedError

# EOFError
# Se produce cuando se alcanza el final del archivo (end of file) sin que se haya leído la información esperada.
input('Enter something: ')

# FloatingPointError
# Se produce cuando ocurre un error en una operación de punto flotante.
print(1.0 / 0.0)

# ArithmeticError
# Esta es la clase base para errores aritméticos.

# StopIteration
# Se produce cuando se itera sobre un iterador y no hay más elementos disponibles.
iterator = iter([1, 2, 3])
while True:
    print(next(iterator))
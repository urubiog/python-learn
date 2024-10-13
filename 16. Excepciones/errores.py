# SyntaxError
print("Hola mundo"  # Falta cerrar paréntesis

# IndentationError
def mi_funcion():
print("Hola")  # Falta indentación

# NameError
print(variable_no_definida)  # La variable no está definida

# TypeError
resultado = 10 + "5"  # No se pueden sumar un entero y una cadena

# ValueError
entero = int("hola")  # No se puede convertir "hola" a entero

# ZeroDivisionError
resultado = 10 / 0  # No se puede dividir por cero

# IndexError
mi_lista = [1, 2, 3]
print(mi_lista[3])  # Índice fuera de rango

# KeyError
mi_diccionario = {"clave": "valor"}
print(mi_diccionario["otra_clave"])  # Clave no existe en el diccionario

# FileNotFoundError
with open("archivo_inexistente.txt", "r") as archivo:
    contenido = archivo.read()  # Archivo no encontrado

# IOError
# Simulación de un error de E/S al intentar abrir un archivo que no se tiene permiso de acceso

# AttributeError
class MiClase:
    pass

objeto = MiClase()
print(objeto.atributo_inexistente)  # El atributo no existe en el objeto

# ImportError
import notexistingmodule # Error al importar un módulo que no existe

# ModuleNotFoundError
import notfoundmodule # Error al intentar importar un módulo que no existe

# KeyboardInterrupt
# No se puede simular en este contexto

# MemoryError
# No se puede simular en este contexto

# OverflowError
numerogrande = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999...

# RecursionError
def recursion_infinita():
    recursion_infinita()

# StopIteration
# No se puede simular en este contexto

# TypeError (otro ejemplo)
# No se puede simular en este contexto

# UnboundLocalError
def funcion():
    print(x)
    x = 10

funcion()  # Referencia a variable local no definida

# List comprehension para obtener el cuadrado de los números del 1 al 10
cuadrados = [x ** 2 for x in range(1, 11)]

# List comprehension para filtrar solo los números pares del 1 al 10
pares = [x for x in range(1, 11) if x % 2 == 0]

# List comprehension para combinar elementos de dos listas
combinacion = [(x, y) for x in ['a', 'b', 'c'] for y in [1, 2, 3]]

# List comprehension para transformar una cadena a una lista de caracteres
cadena = "Hola mundo"
caracteres = [char for char in cadena]

# List comprehension para aplicar una operación sobre una lista
numeros = [1, 2, 3, 4, 5]
doble = [x * 2 for x in numeros]

# Genera una lista de los cuadrados de los números pares del 0 al 9
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # Output: [0, 4, 16, 36, 64]

# Crea una matriz 3x3 inicializada con ceros
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)  
# Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Genera una lista de números pares, y si son divisibles por 3, se les suma 1, de lo contrario se les resta 1
numbers = [x + 1 if x % 3 == 0 else x - 1 for x in range(10) if x % 2 == 0]
print(numbers)  
# Output: [1, 1, 3, -1, 5, -1, 7, 7, 9, -1]

# Genera una lista de números si son pares y divisibles por 3, de lo contrario, los convierte en 0
numbers = [x if x % 2 == 0 else 0 for x in range(20) if x % 3 == 0]
print(numbers)  
# Output: [0, 0, 6, 0, 12, 0, 18, 0]

# Genera una lista de las letras en minúsculas de una cadena, si son vocales, las convierte a mayúsculas
word = "hello world"
letters = [char.upper() if char in 'aeiou' else char for char in word if char.isalpha()]
print(letters)  
# Output: ['h', 'E', 'l', 'l', 'O', ' ', 'w', 'O', 'r', 'l', 'd']
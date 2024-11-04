# Ejemplo de desempaquetado
coordenadas = (3, 5)  # Una tupla que representa coordenadas x, y

x, y = coordenadas  # Desempaquetamos la tupla en dos variables

print("La coordenada x es:", x)
print("La coordenada y es:", y)

# Desempaquetado de una lista
numeros = [1, 2, 3]

a, b, c = numeros

print("El primer número es:", a)
print("El segundo número es:", b)
print("El tercer número es:", c)

# Desempaquetado con estructuras anidadas
datos_personales = ("Juan", "Perez", (1990, 5, 15))

nombre, apellido, (anio, mes, dia) = datos_personales

print("Nombre:", nombre)
print("Apellido:", apellido)
print("Fecha de nacimiento:", f"{dia}/{mes}/{anio}")

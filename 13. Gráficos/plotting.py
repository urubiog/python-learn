# Importación de la biblioteca matplotlib
import matplotlib.pyplot as plt

# Datos para graficar
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creación de una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Trazado de una línea simple
ax.plot(x, y, label='Datos', color='blue', marker='o')

# Adición de etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de Línea Básico')

# Adición de una leyenda
ax.legend()

# Mostrar el gráfico
plt.show()

# Crear un gráfico de barras
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 2, 4]

fig, ax = plt.subplots()

# Trazado de un gráfico de barras
ax.bar(categorias, valores, color='green')

# Adición de etiquetas y título
ax.set_xlabel('Categorías')
ax.set_ylabel('Valores')
ax.set_title('Gráfico de Barras Básico')

# Mostrar el gráfico
plt.show()

# Crear un gráfico de dispersión
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

fig, ax = plt.subplots()

# Trazado de un gráfico de dispersión
ax.scatter(x, y, color='red', label='Puntos')

# Adición de etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Gráfico de Dispersión Básico')
ax.legend()

# Mostrar el gráfico
plt.show()

# Crear un histograma
datos = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]

fig, ax = plt.subplots()

# Trazado de un histograma
ax.hist(datos, bins=10, color='purple', edgecolor='black')

# Adición de etiquetas y título
ax.set_xlabel('Rango')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma Básico')

# Mostrar el gráfico
plt.show()

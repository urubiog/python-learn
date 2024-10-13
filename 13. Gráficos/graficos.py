# Uso de librerías
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

#...............................................................

# Gráfico lineal

df = pd.read_csv("data/creatina.csv")  # El archivo es una tabla de dos valores (fecha y consumiciones)

# Creando el gráfico
sns.lineplot(x="fecha", y="consumiciones", data=df)

# Creando un punto en los momentos de fallo
plt.plot("01-03", 0, "o")
plt.plot("01-06", 2, "o")

# Mostrar gráfico
plt.show()

# Repetir el gráfico lineal con puntos en todos los días
sns.lineplot(x="fecha", y="consumiciones", data=df)

plt.plot("01-01", 1, "o")
plt.plot("01-02", 1, "o")
plt.plot("01-03", 0, "o")
plt.plot("01-04", 1, "o")
plt.plot("01-05", 1, "o")
plt.plot("01-06", 2, "o")
plt.plot("01-07", 1, "o")

plt.show()

#................................................................

# Gráfico de barras

df = pd.read_csv("data/ingresos.csv")  # El archivo es una tabla de dos valores (fuente e ingreso_mes)

sns.barplot(x="fuente", y="ingreso_mes", data=df)

# Imprimiendo el total de ingresos
total_ingreso = df["ingreso_mes"].sum()

print(f"El total de ingresos es de: {total_ingreso}€")

plt.show()

#................................................................

# Gráfico dispersión

df = pd.read_csv("data/dispersion.csv")  # El archivo es una tabla de dos valores (tiempo y dinero)

sns.scatterplot(x="tiempo", y="dinero", data=df)

plt.show()

#................................................................

# Gráfico de bigotes

df = pd.read_csv("data/bigotes.csv")  # El archivo es una tabla de dos valores (categoria y valor)

sns.boxplot(x="categoria", y="valor", data=df)

plt.title("Boxplot")

plt.show()

#................................................................

# Histograma

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/datos.csv')

# Crear el histograma
plt.figure(figsize=(10, 6))

plt.hist(data['edad'], bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

#................................................................

# Gráfico de sectores

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/ventas.csv')

# Crear el gráfico de sectores
plt.figure(figsize=(8, 8))
plt.pie(data['ventas'], labels=data['producto'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
plt.title('Distribución de Ventas por Producto')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#................................................................

# Gráfico de área 

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/ventas_mensuales.csv')

# Establecer el índice como la columna 'mes'
data.set_index('mes', inplace=True)

# Crear el gráfico de áreas apiladas
plt.figure(figsize=(10, 6))
data.plot(kind='area', stacked=True, alpha=0.5)
plt.title('Ventas Mensuales por Producto')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.legend(title='Productos')
plt.grid(True)
plt.show()

#................................................................

# Gráfico de contorno

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/contorno.csv')

# Pivotar el DataFrame para obtener matrices adecuadas para la gráfica de contorno
x = data['x'].unique()
y = data['y'].unique()
z = data.pivot(index='y', columns='x', values='z').values  # Corrección con palabras clave

# Crear el gráfico de contorno
plt.figure(figsize=(10, 6))
cp = plt.contourf(x, y, z, cmap='viridis')
plt.colorbar(cp)  # Añadir la barra de color
plt.title('Gráfico de Contorno de $z = x^2 + y^2$')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#................................................................

# Gráfico de densidad

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/densidad.csv')

# Crear el gráfico de densidad
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data, x='x', y='y', cmap='viridis', fill=True, thresh=0, levels=100)
plt.title('Gráfico de Densidad')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#................................................................

# Gráfico de calor

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/calor.csv')

# Pivotar el DataFrame para obtener una matriz adecuada para el heatmap
heatmap_data = data.pivot(index='y', columns='x', values='valor')  # Corrección con palabras clave

# Crear el gráfico de calor
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='viridis')
plt.title('Gráfico de Calor')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#................................................................

# Gráfico de vectores

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/vectores.csv')

# Crear el gráfico de vectores
plt.figure(figsize=(8, 8))
plt.quiver(data['x'], data['y'], data['u'], data['v'])
plt.title('Gráfico de Vectores')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#................................................................

# Gráfico de Tallo

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/tallo.csv')

# Crear el gráfico de tallo
plt.figure(figsize=(10, 6))
plt.stem(data['x'], data['y'], linefmt='-', markerfmt='o', basefmt='-')
plt.title('Gráfico de Tallo')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#................................................................

# Gráfico de error

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/error_bars.csv')

# Crear el gráfico de barras de error
plt.figure(figsize=(10, 6))
plt.errorbar(data['x'], data['y'], yerr=data['error'], fmt='o', ecolor='red', capsize=5)
plt.title('Gráfico de Barras de Error')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#................................................................

# Gráfico de radar

import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data/radar.csv')

# Número de variables
categories = list(data['variable'])
N = len(categories)

# Valores
values_A = data['valor_A'].values.flatten().tolist()
values_B = data['valor_B'].values.flatten().tolist()

# Repetir el primer valor para cerrar el círculo
values_A += values_A[:1]
values_B += values_B[:1]

# Ángulos para el gráfico de radar
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Crear el gráfico
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
plt.xticks(angles[:-1], categories)

ax.plot(angles, values_A, linewidth=1, linestyle='solid', label='Valor A')
ax.fill(angles, values_A, 'b', alpha=0.1)
ax.plot(angles, values_B, linewidth=1, linestyle='solid', label='Valor B')
ax.fill(angles, values_B, 'r', alpha=0.1)

plt.title('Gráfico de Radar')
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()

#................................................................

# Gráfico de tarta apilada

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/tarta_apilada.csv')

# Crear el gráfico de barras apiladas
plt.figure(figsize=(10, 6))
plt.bar(data['categoria'], data['parte_A'], label='Parte A')
plt.bar(data['categoria'], data['parte_B'], bottom=data['parte_A'], label='Parte B')
plt.bar(data['categoria'], data['parte_C'], bottom=data['parte_A']+data['parte_B'], label='Parte C')

plt.title('Gráfico de Tarta Apilada')
plt.xlabel('Categoría')
plt.ylabel('Valores')
plt.legend()
plt.show()

#................................................................

# Gráfico de violin

# Leer los datos desde el archivo CSV
data = pd.read_csv('data/violin.csv')

# Crear el gráfico de violin
plt.figure(figsize=(10, 6))
sns.violinplot(x='categoria', y='valor', data=data)
plt.title('Gráfico de Violín')
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.show()


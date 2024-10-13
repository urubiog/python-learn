import matplotlib.pyplot as plt

# Crear una figura con una cuadrícula de 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Figura con Subplots (2x2)', fontsize=16)

# Primer subplot
axs[0, 0].text(0.5, 0.5, 'Subplot 1', fontsize=12, ha='center')
axs[0, 0].set_title('Subplot 1')

# Segundo subplot
axs[0, 1].text(0.5, 0.5, 'Subplot 2', fontsize=12, ha='center')
axs[0, 1].set_title('Subplot 2')

# Tercer subplot
axs[1, 0].text(0.5, 0.5, 'Subplot 3', fontsize=12, ha='center')
axs[1, 0].set_title('Subplot 3')

# Cuarto subplot
axs[1, 1].text(0.5, 0.5, 'Subplot 4', fontsize=12, ha='center')
axs[1, 1].set_title('Subplot 4')

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# Crear una figura con un subplot individual usando plt.subplot()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)  # 1 fila, 1 columna, primer subplot
ax.text(0.5, 0.5, 'Subplot Individual', fontsize=12, ha='center')
ax.set_title('Subplot Individual')
plt.show()

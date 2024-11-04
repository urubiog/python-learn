# Para acceder a la función saludar desde su módulo
import Paquete.function_saludos as saludar # Importamos el módulo con el nombre de carpeta + "." + el nombre de archivo y as para darle nombre

# saludar es un objeto namespace: contenedor abstracto en el que un grupo de uno o más identificadores únicos pueden existir.
print(saludar.saludo("Lucas")) # Para usar la función del otro módulo usamos el nombre del módulo mas "." y el nombre de la función ("saludo")

print(saludar.__name__) # Aquí cambia la cosa ya que saludo viene de saludito que es el nombre dado a saludos

import sys

print(f"\n{sys.path}")

sys.path.append("C:\\Users\\Mi Pc\\Desktop\\Onedrive\\Hacking Y Programación\\Python\\Curso\\Modules")

print(f"\n{sys.path}")

# Importando desde paquete una function de un modulo (function_hola)

from Paquete.function_hola import hola # Solo importo la función

print(hola())

# Importando desde paquete de otra manera un modulo

import Paquete.function_saludos as saludar # En function saludos

print(saludar.saludo("Uriel"))

print(saludar.saludito("Hiper"))
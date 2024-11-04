# Ejemplo de mal uso de Python
dispositivo1_marca = "Samsung"
dispositivo2_marca = "Apple"
dispositivo3_marca = "Huawei"

dispositivo1_modelo = "S23"
dispositivo2_modelo = "iPhone 15 Pro"
dispositivo3_modelo = "P20 Pro"

dispositivo1_camT = "48MP"
dispositivo2_camT = "48MP"
dispositivo3_camT = "12MP"

# Todo esto NO es práctico, Python está orientado de otra manera

#----------------------------------------------------------------

# Para crear una clase
class NombreClase(): # Se usa PascalCase
    propiedad1 = "Valor 1"
    propiedad2 = "Valor 2"
    propiedad3 = "Valor 3"

class Dispositivo():
    marca = "Samsung"
    modelo = "S23"
    camT = "48MP"

# Para crear un objeto
dispositivo1 = Dispositivo()

print(dispositivo1.marca) # Esto accede a sus propiedades (En concreto, marca)

#----------------------------------------------------------------

# En Python, los atributos son características de un objeto y los métodos son funciones asociadas a un objeto.

class Dispositivo:
    def __init__(self, marca, modelo, camara):
        # Atributos
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara

Phone1 = Dispositivo("Apple", "iPhone X", "32MP")
Phone2 = Dispositivo("Samsung", "S23", "48MP")

print(Phone1.marca)
print(Phone2.marca)

#----------------------------------------------------------------

class Dispositivo:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self): # Método para llamar
        print(f"Estás llamando a alguien desde {self.modelo}.")

    def colgar(self): # Método para colgar
        print("Has colgado.")

Phone1 = Dispositivo("Apple", "iPhone X", "32MP")
Phone2 = Dispositivo("Samsung", "S23", "12MP")

Phone1.llamar()
Phone1.colgar()

Phone2.llamar()
Phone2.colgar()
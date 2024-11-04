# Creando un diccionario
data = {
    "nombre" : "Uriel",
    "apellido" : "Rubio",
    "edad" : 16
}

# Iterando un diccionario por claves
for keys in data:
    print(keys)
    
# Iterando un diccionario por llave y valor
for elementos in data.items():
    key = elementos[0]
    value = elementos[1]
    print(f"Key de data: {key}, Value: {value}")
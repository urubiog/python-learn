# Creamos la lista
animales = ["perro","gato","cocodrilo"]

# Creamos un bucle for que imprima los elementos de la lista
for animal in animales:
    print(animal)
    
# Para iterar dos listas al mismo tiempo usando zip() del mismo tamaño
primos  = [1,2,3,5,7,11]
lista_divi = [100, 200, 300]

for multi, divi in zip(primos ,lista_divi):
    print(f"Resultados multi: {int(multi*10)}")
    print(f"Resultados divi: {int(divi/10)}")
    
# Iterando con la función range, numeros pares hasta el 48
for par in range(2,50,2):
    print(par)
    
# Recorrer una lista por su indice
for num in enumerate(primos):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}")
    
# Usando else
for numero in primos:
    print(f"valor actual:{numero}")
else:
    print("bucle acabado")
# Iterando un lista haciendo que salte a banana
frutas = ["manzana","pera","banana","ciruela"]

for fruta in frutas:
    if fruta == "banana":
        continue # Este continue lo que hace es que la iteración siga pero como no ha llegado al print banana no saldrá
    print(f"Me voy a comer una {fruta}")
    
# Para anular el bucle usando break
for fruta in frutas:
    if fruta == "banana":
        print("Me comí una banana y ahora me lele pancha, no como mas")
        break
    print(f"Me comí una {fruta}")
print("bucle terminado , terminado de comer")

# Iterar una cadena de texto, se iteran caracter por caracter
texto = "Hola lector"

for letra in texto:
    print(letra)
    
# Creando una lista a partir de otra pero iterada con codigo
numeros_pares = [2,4,6,8,10,12,14,16] # Lista a iterar y añadir en otra lista
numeros_pares_entre_2 = list() # Creando la lista iterada

for pares in numeros_pares: # Para los elementos de la lista de pares
    numeros_pares_entre_2.append(int(pares/2)) # Añadir pares entre dos a la lista nueva

print(numeros_pares_entre_2)

# En una linea de codigo
numeros_pares_entre_2 = [int(x/2) for x in numeros_pares]

print(numeros_pares_entre_2)

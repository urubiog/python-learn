# Creando funciones anónimas
multiplicar_2 = lambda x : x*2 # Esta está almacenada en una variable

lambda x : x # Lambda es una palabra clave, que sirve para ahorra bloques de funciones

print(multiplicar_2(6)) # Devuelve un 12

# No hace falta ningún return y es útil para funciones simples


numeros = [1,2,3,4,5,6,7,8,9,10]

# Sacando números pares con lambda
numeros_pares = list(filter(lambda num:num % 2 == 0, numeros)) # Crea una lista con los valores que salen como True 
print(numeros_pares)

# Sacando números impares
numeros_impares = list(filter(lambda num:num % 2 == 1, numeros)) # Ahora si el residuo es 1 dividiendo el número entre 2 devuelve True
print(numeros_impares)
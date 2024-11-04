# Creando una función
def saludar(): # Aquí va def y el nombre de la function con ():
    print("Hola a todos!") # Aquí va el code
    
saludar() # Ejecutar la función

# Función con parámetros
def saludando(nombre, sexo): # Introducimos los parámetros
    sexo = sexo.lower()
    if sexo == "femenino": # Creamos condiciones para el sexo (guapo,guapa)
        print(f"Hola {nombre}, guapa, como estás?")
    else:
        print(f"Hola {nombre}, guapo, como estás?")
    
#saludando("Lector","masc") # Ejecutamos la función con los parámetros adecuados

# Función con parámetros
def calificativos(nombre, sexo): # Introducimos los parámetros
    sexo = sexo.lower()
    if sexo == "femenino":
        adjetivo = "guapísima"
    elif sexo == "masculino":
        adjetivo = "feo"
    else:
        adjetivo = "desconcertade"
    print(f"Hola {nombre}, {adjetivo}, como estás?")
    
calificativos("Miriam", "None")

# Función con valores
def contraseña_random(num):
    chars = "jafhjf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 1
    contra = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    num = int(num_entero[0])
    num * 2
    print(contra)
    
contraseña_random(4234332) # El valor de () será (num) en la función

import random

# Creando otra función intentando aproximarse a 8 con 987654321 / 123456789
def aproximaciones_8(numero_inicial): # Numero incial podrá ser editado desde fuera de la function.
    num_random = random.randint(123456789,123456795) # Genera un numero random
    result = numero_inicial / num_random
    
    return result # La función devuelve el valor de result

aproximación = aproximaciones_8(numero_inicial=987654321) # aproximación es igual a lo que retorno de la función (result).

print(aproximación)

# Ahora voy a añadir otra variable retornada desde la función
def aproximaciones_8(numero_inicial): 
    num_random = random.randint(123456789,123456795)
    
    primer_digito = str(num_random)[0]  # Esto será el primer digito de el numero random
    
    result = numero_inicial / num_random
    
    return result,primer_digito # Retorno también el primer digito

aproximación, primer_digito = aproximaciones_8(numero_inicial=987654321)

print(f"La aproximación es {aproximación} y el primer digito del num random es {primer_digito}")

# Creando una function que se puedan pasar indefinidos valores con args (parámetro)
def suma(nombre,*numeros): # Lo más importante aquí es (*) en numeros
    return f"Hola {nombre}, la suma de tu numeros es: {sum(numeros)}"

print(suma("Marc",1,2,3,4,5,6)) # Aquí la función lee que (nombre,*numeros) nombre solo puede ser un valor y va el primero y después va 1 o más numeros

# Otra manera más optima de hacerlo para que se puedan añadir parámetros tras el parámetro *args
def suma(nombre,numeros, edad): # Lo más importante aquí es (*) en numeros
    return f"Hola {nombre}, de edad {edad} años, la suma de tu numeros es: {sum([*numeros])}" # Debe de ir entre parentesis

print(suma("Paco",[1,2,3,4,5,6],16)) # Aquí numeros se introduce como una lista y luego va la edad

# También se puede definir que variable es cada valor que se le atribuye
def suma(nombre = "desconocido",numeros = 0, edad = "sin edad específica"): # Aquí definí primero que da la funcióm como salida si no se especifica.
    return f"Hola {nombre}, de edad {edad} años, la suma de tu numeros es: {sum([*numeros])}" # Debe de ir entre parentesis

print(suma(numeros = [2,4,5,6,12] , edad = 16)) # Aquí cada parámetro de la función (sus variables) están definidas excepto nombre y no hace falta respetar el orden pero si definirlas todas

# Por defecto el parámetro nombre está definido como desconocido a no ser que lo substituyamos en el print
print(suma(numeros = [2,4,5,6,12] , edad = 16 , nombre="Uriel"))